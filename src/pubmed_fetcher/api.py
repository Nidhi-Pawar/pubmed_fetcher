import requests
import certifi
from typing import List

NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
HEADERS = {"User-Agent": "pubmed-fetcher/1.0"}

def search_pubmed(query: str, max_results: int = 100) -> List[str]:
    url = f"{NCBI_BASE}esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(url, params=params, headers=HEADERS, verify=certifi.where())
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]

def fetch_details(pubmed_ids: List[str]) -> str:
    url = f"{NCBI_BASE}efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params, headers=HEADERS, verify=certifi.where())
    response.raise_for_status()
    return response.text
