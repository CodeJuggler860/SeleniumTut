import requests
from datetime import datetime

def fetch_pubmed_papers(query):
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    
    search_url = f"{base}esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 3,
        "sort": "pub+date",
        "retmode": "json"
    }

    r = requests.get(search_url, params=params).json()
    ids = r["esearchresult"]["idlist"]

    results = []

    for pid in ids:
        fetch_url = f"{base}efetch.fcgi"
        data = {
            "db": "pubmed",
            "id": pid,
            "retmode": "xml"
        }
        paper = requests.get(fetch_url, params=data).text
        results.append({
            "id": pid,
            "link": f"https://pubmed.ncbi.nlm.nih.gov/{pid}/",
            "abstract": paper[:500]  # simplified
        })

    return results
