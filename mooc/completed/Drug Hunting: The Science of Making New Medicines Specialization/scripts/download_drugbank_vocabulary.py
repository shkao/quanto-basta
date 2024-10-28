import os
import requests
import zipfile
import pandas as pd


def download_drugbank_vocabulary():
    url = "https://go.drugbank.com/releases/5-1-12/downloads/all-drugbank-vocabulary"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers, allow_redirects=True)

    if response.status_code == 200:
        zip_path = "drugbank_vocabulary.zip"
        with open(zip_path, "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(".")
            os.rename("drugbank vocabulary.csv", "drugbank_vocabulary.csv")

            df = pd.read_csv("drugbank_vocabulary.csv")
            df = df[["DrugBank ID", "Common name"]]
            df.to_csv("drugbank_vocabulary.csv", index=False)

        os.remove(zip_path)
        return "drugbank_vocabulary.csv"
    else:
        raise Exception(f"Failed to download data. Status code: {response.status_code}")


if __name__ == "__main__":
    download_drugbank_vocabulary()
