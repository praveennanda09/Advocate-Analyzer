from bs4 import BeautifulSoup
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class HTMLParser:
    """Parses raw HTML templates of lawyer profiles and case details into structured dictionaries."""
    
    @staticmethod
    def parse_lawyer_profile(html_content: str) -> Dict[str, Any]:
        """Parse the advocate profile page and return profile details along with case listings."""
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Parse basic advocate metadata
        name = ""
        reg_number = ""
        bar_council = ""
        primary_courts = ""
        
        h1_tag = soup.find("h1")
        if h1_tag:
            name = h1_tag.text.replace("Advocate:", "").strip()
            
        meta_div = soup.find("div", class_="advocate-meta")
        if meta_div:
            for p in meta_div.find_all("p"):
                text = p.text
                if "Registration Number:" in text:
                    reg_number = text.replace("Registration Number:", "").strip()
                elif "Bar Council:" in text:
                    bar_council = text.replace("Bar Council:", "").strip()
                elif "Primary Courts:" in text:
                    primary_courts = text.replace("Primary Courts:", "").strip()
                    
        # Parse case list table
        cases = []
        table = soup.find("table", class_="case-list-table")
        if table:
            tbody = table.find("tbody")
            if tbody:
                for row in tbody.find_all("tr", class_="case-row"):
                    cols = row.find_all("td")
                    if len(cols) >= 7:
                        cnr = cols[1].text.strip()
                        case_num = cols[2].text.strip()
                        court = cols[3].text.strip()
                        parties = cols[4].text.strip()
                        filing_date = cols[5].text.strip()
                        status = cols[6].text.strip()
                        
                        cases.append({
                            "cnr": cnr,
                            "case_number": case_num,
                            "court": court,
                            "parties": parties,
                            "filing_date_raw": filing_date,
                            "status": status
                        })
                        
        # Parse pagination links
        pagination_links = []
        pagination_div = soup.find("div", class_="pagination")
        if pagination_div:
            for a in pagination_div.find_all("a", href=True):
                pagination_links.append(a["href"])
                
        return {
            "name": name,
            "registration_number": reg_number,
            "bar_council": bar_council,
            "primary_courts": primary_courts,
            "cases": cases,
            "pagination_links": pagination_links
        }


    @staticmethod
    def parse_case_details(html_content: str) -> Dict[str, Any]:
        """Parse the individual case details page into a structured format."""
        soup = BeautifulSoup(html_content, "html.parser")
        details: Dict[str, Any] = {}
        
        # 1. Parse main case details table
        details_table = soup.find("table", class_="details-table")
        if details_table:
            for row in details_table.find_all("tr"):
                cols = row.find_all("td")
                if len(cols) == 2:
                    key = cols[0].text.replace(":", "").strip().lower().replace(" ", "_")
                    val = cols[1].text.strip()
                    details[key] = val
                    
        # Extract specific structured metadata from details mapping
        cnr = details.get("cnr_number")
        if not cnr:
            # Try to get from span
            cnr_span = soup.find(id="cnr_number")
            cnr = cnr_span.text.strip() if cnr_span else ""
            
        case_number = details.get("case_number", "")
        if not case_number:
            h2_tag = soup.find("h2")
            if h2_tag and "Case Details:" in h2_tag.text:
                case_number = h2_tag.text.replace("Case Details:", "").strip()

        # 2. Parse Acts and Sections
        acts = []
        acts_table = soup.find("table", class_="acts-table")
        if acts_table:
            tbody = acts_table.find("tbody")
            if tbody:
                for row in tbody.find_all("tr"):
                    cols = row.find_all("td")
                    if len(cols) >= 2:
                        acts.append({
                            "act": cols[0].text.strip(),
                            "section": cols[1].text.strip()
                        })

        # 3. Parse Parties and Advocates
        parties = {
            "petitioner": "",
            "petitioner_advocate": "",
            "respondent": "",
            "respondent_advocate": ""
        }
        parties_table = soup.find("table", class_="parties-table")
        if parties_table:
            for row in parties_table.find_all("tr"):
                cols = row.find_all("td")
                if len(cols) == 2:
                    key = cols[0].text.replace(":", "").strip().lower().replace(" ", "_")
                    val = cols[1].text.strip()
                    if key in parties:
                        parties[key] = val

        # 4. Parse Hearing History
        hearing_history = []
        history_table = soup.find("table", class_="history-table")
        if history_table:
            tbody = history_table.find("tbody")
            if tbody:
                for row in tbody.find_all("tr"):
                    cols = row.find_all("td")
                    if len(cols) >= 3:
                        hearing_history.append({
                            "hearing_date": cols[0].text.strip(),
                            "stage": cols[1].text.strip(),
                            "business": cols[2].text.strip()
                        })

        # 5. Parse Orders and Judgments
        orders = []
        orders_table = soup.find("table", class_="orders-table")
        if orders_table:
            tbody = orders_table.find("tbody")
            if tbody:
                for row in tbody.find_all("tr"):
                    cols = row.find_all("td")
                    if len(cols) >= 3:
                        date = cols[0].text.strip()
                        desc = cols[1].text.strip()
                        pdf_link = cols[2].find("a")
                        pdf_url = pdf_link["href"] if pdf_link and "href" in pdf_link.attrs else ""
                        
                        orders.append({
                            "date": date,
                            "description": desc,
                            "pdf_url": pdf_url
                        })

        return {
            "cnr": cnr,
            "case_number": case_number,
            "filing_date_raw": details.get("filing_date", ""),
            "registration_date_raw": details.get("registration_date", ""),
            "disposal_date_raw": details.get("disposal_date", ""),
            "current_stage": details.get("current_stage", ""),
            "status": details.get("status", ""),
            "court": details.get("court", ""),
            "judge": details.get("judge", ""),
            "case_category": details.get("case_category", ""),
            "acts": acts,
            "petitioner": parties["petitioner"],
            "petitioner_advocate": parties["petitioner_advocate"],
            "respondent": parties["respondent"],
            "respondent_advocate": parties["respondent_advocate"],
            "hearing_history": hearing_history,
            "orders": orders
        }
