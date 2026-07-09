# Mock data representing eCourts India lawyer profiles and cases, including paginated outputs.

LAWYER_PROFILES = {
    "kuchi-rajeswara-sastry": """
<!DOCTYPE html>
<html>
<head>
    <title>Advocate Profile - Kuchi Rajeswara Sastry (Page 1)</title>
</head>
<body>
    <div class="profile-container">
        <h1>Advocate: Kuchi Rajeswara Sastry</h1>
        <div class="advocate-meta">
            <p><strong>Registration Number:</strong> AP/1042/1971</p>
            <p><strong>Bar Council:</strong> Bar Council of Andhra Pradesh</p>
            <p><strong>Primary Courts:</strong> Senior Civil Court Amalapuram, Junior Civil Court Amalapuram, Rajahmundry Courts</p>
        </div>
        
        <h2>Case List - Page 1</h2>
        <table class="case-list-table">
            <thead>
                <tr>
                    <th>S.No</th>
                    <th>CNR Number</th>
                    <th>Case Number</th>
                    <th>Court Name</th>
                    <th>Parties</th>
                    <th>Filing Date</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr class="case-row" data-cnr="APGD050012342021">
                    <td>1</td>
                    <td><a href="/case/APGD050012342021">APGD050012342021</a></td>
                    <td>O.S. 104/2021</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Garapati Venkata Nagendra Prasad Vs. Garapati Venkta Ramakrishna Rao</td>
                    <td>15-04-2021</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050024682022">
                    <td>2</td>
                    <td><a href="/case/APGD050024682022">APGD050024682022</a></td>
                    <td>O.S. 45/2022</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>Konda Surya Rao Vs. Konda Naga Lakshmi</td>
                    <td>12-05-2022</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APHC010045671974">
                    <td>3</td>
                    <td><a href="/case/APHC010045671974">APHC010045671974</a></td>
                    <td>W.P. 5678/1974</td>
                    <td>High Court of Andhra Pradesh</td>
                    <td>Krishna Coconut Company Vs. Market Committee</td>
                    <td>10-10-1974</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050011112023">
                    <td>4</td>
                    <td><a href="/case/APGD050011112023">APGD050011112023</a></td>
                    <td>O.S. 12/2023</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Venkata Prasad Vs. Ramakrishna Rao</td>
                    <td>10-01-2023</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050022222023">
                    <td>5</td>
                    <td><a href="/case/APGD050022222023">APGD050022222023</a></td>
                    <td>O.S. 88/2023</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>Surya Rao Vs. Naga Lakshmi</td>
                    <td>12-03-2023</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APHC010033331976">
                    <td>6</td>
                    <td><a href="/case/APHC010033331976">APHC010033331976</a></td>
                    <td>W.P. 1234/1976</td>
                    <td>High Court of Andhra Pradesh</td>
                    <td>Sastry and Sons Vs. Market Committee</td>
                    <td>15-08-1976</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050044442024">
                    <td>7</td>
                    <td><a href="/case/APGD050044442024">APGD050044442024</a></td>
                    <td>O.S. 11/2024</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Rao Vs. Sastry</td>
                    <td>01-02-2024</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050055552024">
                    <td>8</td>
                    <td><a href="/case/APGD050055552024">APGD050055552024</a></td>
                    <td>O.S. 15/2024</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>Plaintiff A Vs. Defendant B</td>
                    <td>15-03-2024</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050066662024">
                    <td>9</td>
                    <td><a href="/case/APGD050066662024">APGD050066662024</a></td>
                    <td>O.S. 22/2024</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Client X Vs. Opponent Y</td>
                    <td>10-04-2024</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050077772024">
                    <td>10</td>
                    <td><a href="/case/APGD050077772024">APGD050077772024</a></td>
                    <td>O.S. 35/2024</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>User Alpha Vs. User Beta</td>
                    <td>20-05-2024</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
            </tbody>
        </table>
        
        <div class="pagination">
            <span class="current-page">1</span>
            <a class="page-link" href="https://ecourtsindia.com/lawyer/kuchi-rajeswara-sastry?page=2">2</a>
        </div>
    </div>
</body>
</html>
""",
    "kuchi-rajeswara-sastry?page=2": """
<!DOCTYPE html>
<html>
<head>
    <title>Advocate Profile - Kuchi Rajeswara Sastry (Page 2)</title>
</head>
<body>
    <div class="profile-container">
        <h1>Advocate: Kuchi Rajeswara Sastry</h1>
        <div class="advocate-meta">
            <p><strong>Registration Number:</strong> AP/1042/1971</p>
            <p><strong>Bar Council:</strong> Bar Council of Andhra Pradesh</p>
        </div>
        
        <h2>Case List - Page 2</h2>
        <table class="case-list-table">
            <thead>
                <tr>
                    <th>S.No</th>
                    <th>CNR Number</th>
                    <th>Case Number</th>
                    <th>Court Name</th>
                    <th>Parties</th>
                    <th>Filing Date</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr class="case-row" data-cnr="APGD050088882025">
                    <td>11</td>
                    <td><a href="/case/APGD050088882025">APGD050088882025</a></td>
                    <td>O.S. 40/2025</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Seller S Vs. Buyer B</td>
                    <td>05-01-2025</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050099992025">
                    <td>12</td>
                    <td><a href="/case/APGD050099992025">APGD050099992025</a></td>
                    <td>O.S. 45/2025</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>Owner O Vs. Tenant T</td>
                    <td>12-02-2025</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050010102025">
                    <td>13</td>
                    <td><a href="/case/APGD050010102025">APGD050010102025</a></td>
                    <td>O.S. 50/2025</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Petitioner G Vs. Respondent H</td>
                    <td>18-03-2025</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050011122025">
                    <td>14</td>
                    <td><a href="/case/APGD050011122025">APGD050011122025</a></td>
                    <td>O.S. 60/2025</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>Husband H Vs. Wife W</td>
                    <td>25-04-2025</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050012132025">
                    <td>15</td>
                    <td><a href="/case/APGD050012132025">APGD050012132025</a></td>
                    <td>O.S. 70/2025</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Partner P Vs. Partner D</td>
                    <td>30-05-2025</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050013142025">
                    <td>16</td>
                    <td><a href="/case/APGD050013142025">APGD050013142025</a></td>
                    <td>O.S. 80/2025</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>Creditor C Vs. Debtor D</td>
                    <td>15-06-2025</td>
                    <td><span class="status-pending">Pending</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050014152026">
                    <td>17</td>
                    <td><a href="/case/APGD050014152026">APGD050014152026</a></td>
                    <td>O.S. 90/2026</td>
                    <td>Senior Civil Court, Amalapuram</td>
                    <td>Lender L Vs. Borrower B</td>
                    <td>10-01-2026</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
                <tr class="case-row" data-cnr="APGD050015162026">
                    <td>18</td>
                    <td><a href="/case/APGD050015162026">APGD050015162026</a></td>
                    <td>O.S. 100/2026</td>
                    <td>Junior Civil Court, Amalapuram</td>
                    <td>Brother A Vs. Sister B</td>
                    <td>22-02-2026</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
            </tbody>
        </table>
        
        <div class="pagination">
            <a class="page-link" href="https://ecourtsindia.com/lawyer/kuchi-rajeswara-sastry">1</a>
            <span class="current-page">2</span>
        </div>
    </div>
</body>
</html>
""",
    "john-doe": """
<!DOCTYPE html>
<html>
<head>
    <title>Advocate Profile - John Doe</title>
</head>
<body>
    <div class="profile-container">
        <h1>Advocate: John Doe</h1>
        <div class="advocate-meta">
            <p><strong>Registration Number:</strong> MH/2045/1995</p>
            <p><strong>Bar Council:</strong> Bar Council of Maharashtra</p>
            <p><strong>Primary Courts:</strong> District Court Mumbai</p>
        </div>
        
        <h2>Case List</h2>
        <table class="case-list-table">
            <thead>
                <tr>
                    <th>S.No</th>
                    <th>CNR Number</th>
                    <th>Case Number</th>
                    <th>Court Name</th>
                    <th>Parties</th>
                    <th>Filing Date</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr class="case-row" data-cnr="MHMC010098762020">
                    <td>1</td>
                    <td><a href="/case/MHMC010098762020">MHMC010098762020</a></td>
                    <td>O.S. 50/2020</td>
                    <td>District Court, Mumbai</td>
                    <td>Alpha Corp Vs. Beta Ltd</td>
                    <td>01-01-2020</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
"""
}

# Detailed case templates for all 18 cases
CASE_DETAILS = {
    "APGD050012342021": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 104/2021</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050012342021</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>15-04-2021</td></tr>
            <tr><td><strong>Registration Date:</strong></td><td>18-04-2021</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>12-10-2023</td></tr>
            <tr><td><strong>Current Stage:</strong></td><td>Case Disposed</td></tr>
            <tr><td><strong>Status:</strong></td><td>Disposed (Allowed / Decreed with Relief)</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Sri K. Sree Rama Murthy</td></tr>
            <tr><td><strong>Case Category:</strong></td><td>Original Suit (O.S.)</td></tr>
        </table>
        <h3>Parties & Advocates</h3>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Garapati Venkata Nagendra Prasad</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Garapati Venkta Ramakrishna Rao</td></tr>
            <tr><td><strong>Respondent Advocate:</strong></td><td>P.S. Rao</td></tr>
        </table>
        <h3>Hearing History</h3>
        <table class="history-table">
            <tbody>
                <tr><td>10-05-2021</td><td>First Hearing</td><td>Summons ordered</td></tr>
                <tr><td>12-10-2023</td><td>Final Argument</td><td>Suit Decreed with costs.</td></tr>
            </tbody>
        </table>
    </div>
</body></html>
""",
    "APGD050024682022": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 45/2022</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050024682022</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>12-05-2022</td></tr>
            <tr><td><strong>Registration Date:</strong></td><td>15-05-2022</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>-</td></tr>
            <tr><td><strong>Current Stage:</strong></td><td>Defendant Written Statement</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Smt. M. Rajani</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Konda Surya Rao</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Konda Naga Lakshmi</td></tr>
            <tr><td><strong>Respondent Advocate:</strong></td><td>M.S. Prasad</td></tr>
        </table>
    </div>
</body></html>
""",
    "APHC010045671974": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: W.P. 5678/1974</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APHC010045671974</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>10-10-1974</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>22-11-1976</td></tr>
            <tr><td><strong>Status:</strong></td><td>Disposed (Allowed / Quashed)</td></tr>
            <tr><td><strong>Court:</strong></td><td>High Court of Andhra Pradesh</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Justice O. Chinnappa Reddy</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Krishna Coconut Company</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Market Committee</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050011112023": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 12/2023</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050011112023</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>10-01-2023</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>15-09-2024</td></tr>
            <tr><td><strong>Status:</strong></td><td>Disposed (Allowed / Decreed)</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Sri K. Sree Rama Murthy</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Venkata Prasad</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Ramakrishna Rao</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050022222023": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 88/2023</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050022222023</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>12-03-2023</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Smt. M. Rajani</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Surya Rao</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Naga Lakshmi</td></tr>
        </table>
    </div>
</body></html>
""",
    "APHC010033331976": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: W.P. 1234/1976</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APHC010033331976</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>15-08-1976</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>10-12-1978</td></tr>
            <tr><td><strong>Status:</strong></td><td>Disposed (Allowed / Quashed)</td></tr>
            <tr><td><strong>Court:</strong></td><td>High Court of Andhra Pradesh</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Justice O. Chinnappa Reddy</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Sastry and Sons</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Market Committee</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050044442024": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 11/2024</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050044442024</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>01-02-2024</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Sri K. Sree Rama Murthy</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Rao</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Sastry</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050055552024": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 15/2024</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050055552024</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>15-03-2024</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Smt. M. Rajani</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Plaintiff A</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Defendant B</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050066662024": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 22/2024</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050066662024</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>10-04-2024</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Sri K. Sree Rama Murthy</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Client X</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Opponent Y</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050077772024": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 35/2024</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050077772024</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>20-05-2024</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
            <tr><td><strong>Judge:</strong></td><td>Smt. M. Rajani</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>User Alpha</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>User Beta</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050088882025": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 40/2025</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050088882025</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>05-01-2025</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Seller S</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Buyer B</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050099992025": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 45/2025</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050099992025</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>12-02-2025</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Owner O</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Tenant T</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050010102025": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 50/2025</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050010102025</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>18-03-2025</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Petitioner G</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Respondent H</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050011122025": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 60/2025</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050011122025</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>25-04-2025</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Husband H</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Wife W</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050012132025": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 70/2025</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050012132025</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>30-05-2025</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Partner P</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Partner D</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050013142025": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 80/2025</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050013142025</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>15-06-2025</td></tr>
            <tr><td><strong>Status:</strong></td><td>Pending</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Creditor C</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Debtor D</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050014152026": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 90/2026</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050014152026</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>10-01-2026</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>15-05-2026</td></tr>
            <tr><td><strong>Status:</strong></td><td>Disposed (Allowed / Decreed)</td></tr>
            <tr><td><strong>Court:</strong></td><td>Senior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Lender L</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Borrower B</td></tr>
        </table>
    </div>
</body></html>
""",
    "APGD050015162026": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 100/2026</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">APGD050015162026</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>22-02-2026</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>20-06-2026</td></tr>
            <tr><td><strong>Status:</strong></td><td>Disposed (Allowed / Decreed)</td></tr>
            <tr><td><strong>Court:</strong></td><td>Junior Civil Court, Amalapuram</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Brother A</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>Kuchi Rajeswara Sastry</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Sister B</td></tr>
        </table>
    </div>
</body></html>
""",
    "MHMC010098762020": """
<!DOCTYPE html>
<html><body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 50/2020</h2>
        <table class="details-table">
            <tr><td><strong>CNR Number:</strong></td><td><span id="cnr_number">MHMC010098762020</span></td></tr>
            <tr><td><strong>Filing Date:</strong></td><td>01-01-2020</td></tr>
            <tr><td><strong>Disposal Date:</strong></td><td>15-12-2020</td></tr>
            <tr><td><strong>Status:</strong></td><td>Disposed (Dismissed for Default)</td></tr>
            <tr><td><strong>Court:</strong></td><td>District Court, Mumbai</td></tr>
        </table>
        <table class="parties-table">
            <tr><td><strong>Petitioner:</strong></td><td>Alpha Corp</td></tr>
            <tr><td><strong>Petitioner Advocate:</strong></td><td>John Doe</td></tr>
            <tr><td><strong>Respondent:</strong></td><td>Beta Ltd</td></tr>
        </table>
    </div>
</body></html>
"""
}
