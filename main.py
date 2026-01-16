from text_extractor import extract_text
from keyword_extractor import extract_keywords
from pubmed_fetcher import fetch_pubmed_papers
from scholar_fallback import fetch_scholar

def main():
    text = extract_text("sample.pdf")  # change file name
    keywords = extract_keywords(text)
    query = " ".join(keywords)

    papers = fetch_pubmed_papers(query)

    if len(papers) < 3:
        papers.extend(fetch_scholar(query))

    for i, paper in enumerate(papers[:3], start=1):
        print(f"\nPaper {i}")
        print(paper)

if __name__ == "__main__":
    main()
