import os
from functools import lru_cache
import ollama
import requests
import xml.etree.ElementTree as ET
from iso4 import abbreviate
from loguru import logger
from pyzotero import zotero
from impact_factor.core import Factor


def create_zotero_instance(library_id=None, api_key=None):
    library_id = library_id or os.getenv("ZOTERO_LIBRARY_ID")
    library_type = "user"
    api_key = api_key or os.getenv("ZOTERO_API_KEY")
    if not library_id or not api_key:
        logger.error("Zotero library ID or API key is not set.")
        raise EnvironmentError("Zotero library ID or API key is not set.")
    return zotero.Zotero(library_id, library_type, api_key)


def get_collection_by_name(zot, collection_name=".Inbox"):
    logger.info(f"Fetching collection '{collection_name}' from Zotero.")
    try:
        collections = zot.everything(zot.collections())
        return next(
            (
                collection
                for collection in collections
                if collection["data"].get("name") == collection_name
            ),
            None,
        )
    except Exception as e:
        logger.error(f"Error fetching collections: {e}")
        return None


def retrieve_items(zot, collection_key, excluded_types=None, target_type=None):
    try:
        items = zot.collection_items(collection_key)
        if excluded_types:
            items = [
                item
                for item in items
                if item["data"].get("itemType") not in excluded_types
            ]
        if target_type:
            items = [
                item for item in items if item["data"].get("itemType") == target_type
            ]
        return items
    except Exception as e:
        logger.error(f"Error fetching items from collection: {e}")
        return []


def get_inbox_items(zot):
    inbox_collection = get_collection_by_name(zot)
    if not inbox_collection:
        logger.warning("'.Inbox' collection not found.")
        return []
    return retrieve_items(
        zot, inbox_collection["key"], excluded_types=["attachment", "note"]
    )


def get_items_by_type(zot, item_type):
    valid_item_types = {
        "book",
        "bookSection",
        "conferencePaper",
        "dictionaryEntry",
        "encyclopediaArticle",
        "journalArticle",
        "manuscript",
        "note",
        "report",
        "thesis",
        "webpage",
    }

    if item_type not in valid_item_types:
        logger.error(
            f"Invalid item type '{item_type}'. Supported types are: {valid_item_types}"
        )
        return []

    inbox_collection = get_collection_by_name(zot)
    if not inbox_collection:
        logger.warning("'.Inbox' collection not found.")
        return []

    return retrieve_items(zot, inbox_collection["key"], target_type=item_type)


def summarize_abstract(abstract):
    prompt = f"Summarize the following abstract in 3 sentences without any introductory phrases:\n\n{abstract}"
    try:
        response = ollama.chat(
            model="llama3.2", messages=[{"role": "user", "content": prompt}]
        )
        return response.get("message", {}).get("content", "")
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        return ""


def append_summary_notes(zot, inbox_items):
    for item in inbox_items:
        if has_existing_note(zot, item):
            continue

        abstract = get_abstract(item)
        if abstract:
            summary = summarize_abstract(abstract)
            if summary:
                add_summary_note(zot, item, summary)


def has_existing_note(zot, item):
    children = zot.children(item["key"])
    if any(child["data"].get("itemType") == "note" for child in children):
        logger.debug(
            f"Skipping item {item['data'].get('title', 'Untitled')} as it already has a note."
        )
        return True
    return False


def get_abstract(item):
    abstract = item["data"].get("abstractNote", "")
    if not abstract or len(abstract) <= 150:
        url = item["data"].get("url", "")
        if url and "pubs.acs.org" not in url:
            try:
                response = requests.get(url)
                response.raise_for_status()
                abstract = response.text[
                    :2500
                ]  # Limit retrieved text to 2500 characters
                logger.debug(
                    f"Retrieved text from URL for item '{item['data'].get('title', 'Untitled')}'."
                )
            except requests.exceptions.RequestException as e:
                logger.error(f"Error retrieving text from URL '{url}': {e}")
                return ""
    return abstract


def add_summary_note(zot, item, summary):
    note = {
        "itemType": "note",
        "parentItem": item["key"],
        "note": f"<p><b>Summary:</b> {summary}</p>",
    }
    try:
        zot.create_items([note])
        logger.info(
            f"Added summary note for item '{item['data'].get('title', 'Untitled')}'."
        )
    except Exception as e:
        logger.error(f"Error adding summary note: {e}")


def delete_items_by_type(zot, item_type):
    logger.info(f"Removing items of type '{item_type}' from the '.Inbox' collection.")
    while True:
        inbox_items = get_items_by_type(zot, item_type)
        logger.info(f"Retrieved {len(inbox_items)} items from the '.Inbox' collection.")
        items_to_remove = [
            item for item in inbox_items if item["data"].get("itemType") == item_type
        ]

        if not items_to_remove:
            break

        for item in items_to_remove:
            try:
                zot.delete_item(item)
                logger.info(
                    f"Removed item '{item['data'].get('title', 'Untitled')}' of type '{item_type}'."
                )
            except Exception as e:
                logger.error(
                    f"Error removing item '{item['data'].get('title', 'Untitled')}': {e}"
                )


def fill_missing_metadata(zot, inbox_items):
    for item in inbox_items:
        title = item["data"].get("title", "Untitled")
        doi = item["data"].get("DOI")
        if not doi:
            logger.warning(f"Item '{title}' has no DOI.")
            continue

        metadata = retrieve_data_by_doi(doi)
        if not metadata:
            logger.warning(f"Could not retrieve metadata for DOI '{doi}'.")
            continue

        item = zot.item(item["key"])  # Re-fetch the item to ensure latest version
        update_metadata_fields(zot, item, metadata, title)


def update_metadata_fields(zot, item, metadata, title):
    fields_to_update = {
        "journalAbbreviation": metadata.get("journalAbbreviation")
        or abbreviate(metadata.get("publicationTitle")),
    }
    for field, value in fields_to_update.items():
        update_field(zot, item, field, value, title, field)


def update_field(zot, item, field, value, title, field_name):
    if value and item["data"].get(field) != value:
        item["data"][field] = value
        try:
            zot.update_item(item)
            logger.info(f"Updated {field_name} for item '{title}'.")
        except Exception as e:
            if "modified since specified version" in str(e):
                logger.warning(
                    f"Version conflict for item '{title}', re-fetching and retrying update."
                )
                item = zot.item(
                    item["key"]
                )  # Re-fetch the item to get the latest version
                item["data"][field] = value
                zot.update_item(item)
                logger.info(
                    f"Successfully updated {field_name} for item '{title}' after retry."
                )
            else:
                logger.error(f"Error updating item '{title}': {e}")


@lru_cache(maxsize=None)
def retrieve_data_by_doi(doi):
    api_url = f"https://api.crossref.org/works/{doi}/transform/application/vnd.crossref.unixsd+xml"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        xml_data = response.content
    except requests.exceptions.RequestException as request_error:
        logger.error(f"Error retrieving data for DOI '{doi}': {request_error}")
        return None

    try:
        xml_root = ET.fromstring(xml_data)
        namespaces = {"ns": "http://www.crossref.org/xschema/1.1"}

        def extract_text(element, xpath):
            found_element = element.find(xpath, namespaces=namespaces)
            return found_element.text if found_element is not None else None

        article_title = extract_text(xml_root, ".//ns:title")
        article_authors = [
            f"{extract_text(person, 'ns:given_name')} {extract_text(person, 'ns:surname')}"
            for person in xml_root.findall(".//ns:person_name", namespaces=namespaces)
            if extract_text(person, "ns:given_name")
            and extract_text(person, "ns:surname")
        ]
        publication_year = extract_text(
            xml_root, './/ns:publication_date[@media_type="print"]/ns:year'
        )
        full_journal_title = extract_text(xml_root, ".//ns:full_title")
        abbreviated_journal_title = extract_text(xml_root, ".//ns:abbrev_title")
        citation_doi_list = [
            citation_doi.text
            for citation in xml_root.findall(".//ns:citation", namespaces=namespaces)
            if (citation_doi := citation.find("ns:doi", namespaces=namespaces))
            is not None
            and citation_doi.text
        ]

        return {
            "title": article_title,
            "creators": article_authors,
            "date": publication_year,
            "publicationTitle": full_journal_title,
            "journalAbbreviation": abbreviated_journal_title,
            "citationKeys": citation_doi_list,
        }
    except ET.ParseError as parse_error:
        logger.error(f"Error parsing XML for DOI '{doi}': {parse_error}")
        return None


def get_impact_factor(journal_name):
    factor_instance = Factor()
    search_results = factor_instance.search(journal_name)
    return search_results[0].get("factor", "") if search_results else None


def main():
    try:
        zot = create_zotero_instance()
        # delete_items_by_type(zot, "note")
        # print(retrieve_data_by_doi("10.1093/nar/gks725"))

        inbox_items = get_inbox_items(zot)
        fill_missing_metadata(zot, inbox_items)
        append_summary_notes(zot, inbox_items)
    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
