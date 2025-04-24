from lxml import etree
from typing import List, Dict

NON_ACADEMIC_KEYWORDS = ["Pharma", "Biotech","Pharmaceutic", "Therapeutics", "Biosciences","Pharmaceutical", "Healthcare", 
                         "Inc.", "Corp.", "Ltd.", "Llc", "gmbh", "Co.", "Company", "Corporation"]
ACADEMIC_KEYWORDS = ["University", "Institute", "College", "Hospital", "School", "Lab", "Laboratory", "Hospital", 
                     "Medical Center", "Clinic","Department of", "Faculty of"]


def extract_papers_from_xml(xml_data: str) -> List[Dict]:
    root = etree.fromstring(xml_data.encode())
    papers = []

    for article in root.xpath("//PubmedArticle"):
        pmid = article.xpath(".//PMID/text()")[0]
        title = article.xpath(".//ArticleTitle/text()")[0]
        pub_date = article.xpath(".//PubDate/Year/text()") or ["Unknown"]

        authors_info = article.xpath(".//AuthorList/Author")
        non_academic_authors = []
        companies = []
        email = "Not found"

        for author in authors_info:
            affiliation_nodes = author.xpath(".//AffiliationInfo/Affiliation/text()")
            if not affiliation_nodes:
                continue
            affiliation = affiliation_nodes[0]

            if any(word in affiliation for word in NON_ACADEMIC_KEYWORDS) and not any(word in affiliation for word in ACADEMIC_KEYWORDS):
                lastname = author.xpath("./LastName/text()")
                firstname = author.xpath("./ForeName/text()")
                name = f"{firstname[0]} {lastname[0]}" if firstname and lastname else "Unknown"
                non_academic_authors.append(name)
                companies.append(affiliation)

                # Extract email
                if "@" in affiliation:
                    email = affiliation.split()[-1] 

        if non_academic_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date[0],
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(set(companies)),
                "Corresponding Author Email": email
            })

    return papers
