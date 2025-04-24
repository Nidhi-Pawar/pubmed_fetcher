# 🧪 PubMed Fetcher CLI

A Python CLI tool to fetch PubMed research papers matching a query and extract those with non-academic (industry/pharma/biotech) authors. Built using `requests`, `lxml`, `Typer`, and packaged with `Poetry`.

---

## 🚀 Features

- Search PubMed using full query syntax
- Filter papers by author affiliation 
- Export results to CSV or print to console
- Modular CLI interface built with `Typer`
- Poetry-managed

---
## 📜Project Structure

```
pubmed_fetcher/
├── api.py           # Handles querying PubMed
├── parser.py        # Parses XML + filters authors
├── export.py        # Writes CSV output
├── cli.py           # Typer CLI app
```
---

## 📦 Installation

```bash
git clone https://github.com/your-username/pubmed-fetcher.git
cd pubmed-fetcher
poetry install
poetry env activate
```
---

## ⚙️ Usage

```bash
get-papers-list "query" -f results.csv --debug

```
`query`: PubMed search query

`-f`, `--file`: CSV output path

`-d`, `--debug`: Print logs

---
## 🛠 Dev Notes

API: NCBI Entrez (via requests)

XML parsing: lxml

CLI: typer

CSV: csv.DictWriter

Typing: fully typed functions

Error handling: Skips missing affiliations or authors

---

## 🙌 Acknowledgements

NCBI Entrez Utilities

Typer

LXML

---

 
