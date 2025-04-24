import typer
from pubmed_fetcher.api import search_pubmed, fetch_details
from pubmed_fetcher.parser import extract_papers_from_xml
from pubmed_fetcher.export import write_to_csv

app = typer.Typer()

@app.command()
def fetch(
    query: str,
    file: str = typer.Option(None, "--file", "-f", help="Output CSV file"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output")
):
    if debug:
        print(f"Searching for: {query}")
    ids = search_pubmed(query)
    if debug:
        print(f"Found {len(ids)} papers.")
    xml_data = fetch_details(ids)
    papers = extract_papers_from_xml(xml_data)
    if file:
        write_to_csv(papers, file)
        print(f"Saved {len(papers)} results to {file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    app()
