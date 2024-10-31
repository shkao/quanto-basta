import os
import re
import urllib.parse
from loguru import logger
import requests
from lxml import html
import gemmapy

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def download_gds_results(search_term):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)

    query = f'"{search_term}"[All Fields] AND "Homo sapiens"[porgn]'
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.ncbi.nlm.nih.gov/gds?term={encoded_query}&cmd=DetailsSearch"

    with webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    ) as driver:
        driver.get(url)

        elements_to_click = [
            (By.LINK_TEXT, "Send to:"),
            (By.ID, "dest_File"),
            (
                By.NAME,
                "EntrezSystem2.PEntrez.Gds.Gds_ResultsPanel.Gds_DisplayBar.SendToSubmit",
            ),
        ]

        for by, value in elements_to_click:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((by, value))
            ).click()

        download_path = os.path.expanduser("~/Downloads/gds_result.txt")
        destination_path = os.path.join(os.getcwd(), "gds_result.txt")

        WebDriverWait(driver, 15).until(lambda d: os.path.exists(download_path))
        os.rename(download_path, destination_path)

    return destination_path


def check_gse_in_gemma(gse_id):
    try:
        gemma_client = gemmapy.GemmaPy()
        response = gemma_client.get_datasets_by_ids([gse_id])
        return not response.empty
    except Exception as e:
        logger.error(f"Error checking GSE ID {gse_id} in Gemma: {e}", exc_info=True)
        return False


def get_pubmed_id_from_geo_series(gse_id):
    url = f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={gse_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        tree = html.fromstring(response.content)
        pubmed_id_element = tree.xpath("//span[@class='pubmed_id']/a/text()")

        return pubmed_id_element[0] if pubmed_id_element else None
    except requests.RequestException as e:
        logger.error(
            f"Request error occurred while fetching PubMed ID for {gse_id}: {e}",
            exc_info=True,
        )
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)
    return None


def process_and_export_filtered_gds_data(input_file, output_file):
    def parse_entry(entry):
        fields = {
            "title": r"^\d+\.\s+(.*?)\n",
            "summary": r"\(Submitter supplied\) (.*?)\n",
            "organism": r"Organism:\s+(.*?)\n",
            "method": r"Type:\s+(.*?)\n",
            "platform": r"Platform:\s+(\S+)\s+(\d+)\s+Samples",
            "access": r"Series\s+Accession:\s+(GSE\d+)\s+ID:\s+(\d+)",
        }

        return {
            key: (
                re.search(pattern, entry, re.MULTILINE).group(1)
                if re.search(pattern, entry, re.MULTILINE)
                else "N/A"
            )
            for key, pattern in fields.items()
        }

    with open(input_file, "r") as file:
        entries = file.read().strip().split("\n\n")

    header = (
        "Title\tSummary\tOrganism\tMethod\tPlatform ID\tSamples\tGSE ID\tGDS ID\t"
        "Pubmed ID\tIn Gemma"
    )
    processed_entries = [header]

    valid_methods = {
        "Expression profiling by high throughput sequencing",
        "Expression profiling by array",
    }

    for entry in entries:
        parsed_data = parse_entry(entry)
        pubmed_id = (
            get_pubmed_id_from_geo_series(parsed_data["access"])
            if parsed_data["access"] != "N/A"
            else "N/A"
        )

        if parsed_data["method"] in valid_methods:
            in_gemma = "Unknown"
            if parsed_data["access"] != "N/A":
                try:
                    in_gemma = (
                        "Yes" if check_gse_in_gemma(parsed_data["access"]) else "No"
                    )
                    logger.info(
                        f"GSE ID {parsed_data['access']} is "
                        f"{'in' if in_gemma == 'Yes' else 'not in'} Gemma."
                    )
                except Exception as e:
                    logger.error(
                        f"Error checking Gemma status for GSE ID {parsed_data['access']}: {e}",
                        exc_info=True,
                    )

            processed_entries.append(
                f"{parsed_data['title']}\t{parsed_data['summary']}\t{parsed_data['organism']}\t"
                f"{parsed_data['method']}\t{parsed_data['platform']}\t{parsed_data['access']}\t"
                f"{pubmed_id}\t{in_gemma}"
            )

    with open(output_file, "w") as file:
        file.write("\n".join(processed_entries))


if __name__ == "__main__":
    search_term = "pediatric brain tumor"
    downloaded_file_path = download_gds_results(search_term)
    logger.info(f"The GDS results were downloaded to: {downloaded_file_path}")

    # Ensure the output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Create a TSV filename that includes the search term
    search_term_filename = search_term.replace(" ", "_")
    tsv_file_name = f"{search_term_filename}_gds_results.tsv"
    tsv_file_path = os.path.join(output_dir, tsv_file_name)

    # Process the downloaded data and save it as a TSV file in the output directory
    process_and_export_filtered_gds_data(downloaded_file_path, tsv_file_path)
    logger.info(
        f"The GDS results were converted to TSV format and saved to: {tsv_file_path}"
    )

    # Remove the downloaded file
    os.remove(downloaded_file_path)
    logger.info(f"The downloaded file {downloaded_file_path} has been removed.")
