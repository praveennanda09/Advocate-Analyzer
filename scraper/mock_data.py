# Mock data representing eCourts India lawyer profiles and cases for testing and sandbox execution.

LAWYER_PROFILES = {
    "kuchi-rajeswara-sastry": """
<!DOCTYPE html>
<html>
<head>
    <title>Advocate Profile - Kuchi Rajeswara Sastry</title>
</head>
<body>
    <div class="profile-container">
        <h1>Advocate: Kuchi Rajeswara Sastry</h1>
        <div class="advocate-meta">
            <p><strong>Registration Number:</strong> AP/1042/1971</p>
            <p><strong>Bar Council:</strong> Bar Council of Andhra Pradesh</p>
            <p><strong>Primary Courts:</strong> Senior Civil Court Amalapuram, Junior Civil Court Amalapuram, Rajahmundry Courts</p>
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
                    <td>Krishna Coconut Company, Kuchi Rajeswara Sastry and Sons Vs. East Godavari Coconut and Tobacco Market Committee</td>
                    <td>10-10-1974</td>
                    <td><span class="status-disposed">Disposed</span></td>
                </tr>
            </tbody>
        </table>
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

CASE_DETAILS = {
    "APGD050012342021": """
<!DOCTYPE html>
<html>
<head>
    <title>Case Details - APGD050012342021</title>
</head>
<body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 104/2021</h2>
        <table class="details-table">
            <tr>
                <td><strong>CNR Number:</strong></td>
                <td><span id="cnr_number">APGD050012342021</span></td>
            </tr>
            <tr>
                <td><strong>Filing Date:</strong></td>
                <td>15-04-2021</td>
            </tr>
            <tr>
                <td><strong>Registration Date:</strong></td>
                <td>18-04-2021</td>
            </tr>
            <tr>
                <td><strong>Disposal Date:</strong></td>
                <td>12-10-2023</td>
            </tr>
            <tr>
                <td><strong>Current Stage:</strong></td>
                <td>Case Disposed</td>
            </tr>
            <tr>
                <td><strong>Status:</strong></td>
                <td>Disposed (Allowed / Decreed with Relief)</td>
            </tr>
            <tr>
                <td><strong>Court:</strong></td>
                <td>Senior Civil Court, Amalapuram</td>
            </tr>
            <tr>
                <td><strong>Judge:</strong></td>
                <td>Sri K. Sree Rama Murthy</td>
            </tr>
            <tr>
                <td><strong>Case Category:</strong></td>
                <td>Original Suit (O.S.)</td>
            </tr>
        </table>
        
        <h3>Acts and Sections</h3>
        <table class="acts-table">
            <thead>
                <tr>
                    <th>Act</th>
                    <th>Section</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Code of Civil Procedure, 1908</td>
                    <td>Section 26, Order VII Rule 1 (Plaint filing for partition suit)</td>
                </tr>
            </tbody>
        </table>
        
        <h3>Parties & Advocates</h3>
        <table class="parties-table">
            <tr>
                <td><strong>Petitioner:</strong></td>
                <td>Garapati Venkata Nagendra Prasad</td>
            </tr>
            <tr>
                <td><strong>Petitioner Advocate:</strong></td>
                <td>Kuchi Rajeswara Sastry</td>
            </tr>
            <tr>
                <td><strong>Respondent:</strong></td>
                <td>Garapati Venkta Ramakrishna Rao</td>
            </tr>
            <tr>
                <td><strong>Respondent Advocate:</strong></td>
                <td>P.S. Rao</td>
            </tr>
        </table>

        <h3>Hearing History</h3>
        <table class="history-table">
            <thead>
                <tr>
                    <th>Hearing Date</th>
                    <th>Stage</th>
                    <th>Business Conducted</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>10-05-2021</td>
                    <td>First Hearing</td>
                    <td>Summons ordered to respondent</td>
                </tr>
                <tr>
                    <td>15-06-2021</td>
                    <td>Appearance of Defendant</td>
                    <td>Vakalat filed by P.S. Rao</td>
                </tr>
                <tr>
                    <td>12-10-2023</td>
                    <td>Final Argument</td>
                    <td>Suit Decreed with costs. Petitioner partition claim allowed.</td>
                </tr>
            </tbody>
        </table>

        <h3>Orders & Judgments</h3>
        <table class="orders-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Description</th>
                    <th>Order PDF</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>12-10-2023</td>
                    <td>Final Judgement & Decree</td>
                    <td><a href="/orders/final_order_apgd050012342021.pdf">final_order_apgd050012342021.pdf</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
""",
    "APGD050024682022": """
<!DOCTYPE html>
<html>
<head>
    <title>Case Details - APGD050024682022</title>
</head>
<body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 45/2022</h2>
        <table class="details-table">
            <tr>
                <td><strong>CNR Number:</strong></td>
                <td><span id="cnr_number">APGD050024682022</span></td>
            </tr>
            <tr>
                <td><strong>Filing Date:</strong></td>
                <td>12-05-2022</td>
            </tr>
            <tr>
                <td><strong>Registration Date:</strong></td>
                <td>15-05-2022</td>
            </tr>
            <tr>
                <td><strong>Disposal Date:</strong></td>
                <td>-</td>
            </tr>
            <tr>
                <td><strong>Current Stage:</strong></td>
                <td>Defendant Written Statement</td>
            </tr>
            <tr>
                <td><strong>Status:</strong></td>
                <td>Pending</td>
            </tr>
            <tr>
                <td><strong>Court:</strong></td>
                <td>Junior Civil Court, Amalapuram</td>
            </tr>
            <tr>
                <td><strong>Judge:</strong></td>
                <td>Smt. M. Rajani</td>
            </tr>
            <tr>
                <td><strong>Case Category:</strong></td>
                <td>Original Suit (O.S.)</td>
            </tr>
        </table>
        
        <h3>Acts and Sections</h3>
        <table class="acts-table">
            <thead>
                <tr>
                    <th>Act</th>
                    <th>Section</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Specific Relief Act, 1963</td>
                    <td>Section 38 (Permanent Injunction Suit)</td>
                </tr>
            </tbody>
        </table>
        
        <h3>Parties & Advocates</h3>
        <table class="parties-table">
            <tr>
                <td><strong>Petitioner:</strong></td>
                <td>Konda Surya Rao</td>
            </tr>
            <tr>
                <td><strong>Petitioner Advocate:</strong></td>
                <td>Kuchi Rajeswara Sastry</td>
            </tr>
            <tr>
                <td><strong>Respondent:</strong></td>
                <td>Konda Naga Lakshmi</td>
            </tr>
            <tr>
                <td><strong>Respondent Advocate:</strong></td>
                <td>M.S. Prasad</td>
            </tr>
        </table>

        <h3>Hearing History</h3>
        <table class="history-table">
            <thead>
                <tr>
                    <th>Hearing Date</th>
                    <th>Stage</th>
                    <th>Business Conducted</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>06-06-2022</td>
                    <td>Admit Stage</td>
                    <td>Notice issued to Respondent</td>
                </tr>
                <tr>
                    <td>14-07-2026</td>
                    <td>Hearing</td>
                    <td>Awaiting written statement from Defendant</td>
                </tr>
            </tbody>
        </table>

        <h3>Orders & Judgments</h3>
        <table class="orders-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Description</th>
                    <th>Order PDF</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>06-06-2022</td>
                    <td>Interim Order</td>
                    <td><a href="/orders/interim_order_apgd050024682022.pdf">interim_order_apgd050024682022.pdf</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
""",
    "APHC010045671974": """
<!DOCTYPE html>
<html>
<head>
    <title>Case Details - APHC010045671974</title>
</head>
<body>
    <div class="case-details-container">
        <h2>Case Details: W.P. 5678/1974</h2>
        <table class="details-table">
            <tr>
                <td><strong>CNR Number:</strong></td>
                <td><span id="cnr_number">APHC010045671974</span></td>
            </tr>
            <tr>
                <td><strong>Filing Date:</strong></td>
                <td>10-10-1974</td>
            </tr>
            <tr>
                <td><strong>Registration Date:</strong></td>
                <td>12-10-1974</td>
            </tr>
            <tr>
                <td><strong>Disposal Date:</strong></td>
                <td>22-11-1976</td>
            </tr>
            <tr>
                <td><strong>Current Stage:</strong></td>
                <td>Case Disposed</td>
            </tr>
            <tr>
                <td><strong>Status:</strong></td>
                <td>Disposed (Writ Petition Allowed - Assessment Quashed)</td>
            </tr>
            <tr>
                <td><strong>Court:</strong></td>
                <td>High Court of Andhra Pradesh</td>
            </tr>
            <tr>
                <td><strong>Judge:</strong></td>
                <td>Justice O. Chinnappa Reddy</td>
            </tr>
            <tr>
                <td><strong>Case Category:</strong></td>
                <td>Writ Petition (W.P.)</td>
            </tr>
        </table>
        
        <h3>Acts and Sections</h3>
        <table class="acts-table">
            <thead>
                <tr>
                    <th>Act</th>
                    <th>Section</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Central Sales Tax Act, 1956</td>
                    <td>Section 8, Section 9 (Challenge to tax assessment of market committee fees on coconuts)</td>
                </tr>
            </tbody>
        </table>
        
        <h3>Parties & Advocates</h3>
        <table class="parties-table">
            <tr>
                <td><strong>Petitioner:</strong></td>
                <td>Krishna Coconut Company, Kuchi Rajeswara Sastry and Sons</td>
            </tr>
            <tr>
                <td><strong>Petitioner Advocate:</strong></td>
                <td>Kuchi Rajeswara Sastry</td>
            </tr>
            <tr>
                <td><strong>Respondent:</strong></td>
                <td>East Godavari Coconut and Tobacco Market Committee</td>
            </tr>
            <tr>
                <td><strong>Respondent Advocate:</strong></td>
                <td>Government Pleader for Commercial Taxes</td>
            </tr>
        </table>

        <h3>Hearing History</h3>
        <table class="history-table">
            <thead>
                <tr>
                    <th>Hearing Date</th>
                    <th>Stage</th>
                    <th>Business Conducted</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>12-11-1976</td>
                    <td>Final Argument</td>
                    <td>Arguments concluded by Kuchi Rajeswara Sastry</td>
                </tr>
                <tr>
                    <td>22-11-1976</td>
                    <td>Pronouncement of Order</td>
                    <td>Writ allowed. Assessment declared void.</td>
                </tr>
            </tbody>
        </table>

        <h3>Orders & Judgments</h3>
        <table class="orders-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Description</th>
                    <th>Order PDF</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>22-11-1976</td>
                    <td>Final Judgment</td>
                    <td><a href="/orders/final_judgment_aphc010045671974.pdf">final_judgment_aphc010045671974.pdf</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
""",
    "MHMC010098762020": """
<!DOCTYPE html>
<html>
<head>
    <title>Case Details - MHMC010098762020</title>
</head>
<body>
    <div class="case-details-container">
        <h2>Case Details: O.S. 50/2020</h2>
        <table class="details-table">
            <tr>
                <td><strong>CNR Number:</strong></td>
                <td><span id="cnr_number">MHMC010098762020</span></td>
            </tr>
            <tr>
                <td><strong>Filing Date:</strong></td>
                <td>01-01-2020</td>
            </tr>
            <tr>
                <td><strong>Registration Date:</strong></td>
                <td>03-01-2020</td>
            </tr>
            <tr>
                <td><strong>Disposal Date:</strong></td>
                <td>15-12-2020</td>
            </tr>
            <tr>
                <td><strong>Current Stage:</strong></td>
                <td>Case Disposed</td>
            </tr>
            <tr>
                <td><strong>Status:</strong></td>
                <td>Disposed (Dismissed for Default)</td>
            </tr>
            <tr>
                <td><strong>Court:</strong></td>
                <td>District Court, Mumbai</td>
            </tr>
            <tr>
                <td><strong>Judge:</strong></td>
                <td>Sri R.K. Mehta</td>
            </tr>
            <tr>
                <td><strong>Case Category:</strong></td>
                <td>Original Suit (O.S.)</td>
            </tr>
        </table>
        
        <h3>Acts and Sections</h3>
        <table class="acts-table">
            <thead>
                <tr>
                    <th>Act</th>
                    <th>Section</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Code of Civil Procedure, 1908</td>
                    <td>Order IX Rule 8</td>
                </tr>
            </tbody>
        </table>
        
        <h3>Parties & Advocates</h3>
        <table class="parties-table">
            <tr>
                <td><strong>Petitioner:</strong></td>
                <td>Alpha Corp</td>
            </tr>
            <tr>
                <td><strong>Petitioner Advocate:</strong></td>
                <td>John Doe</td>
            </tr>
            <tr>
                <td><strong>Respondent:</strong></td>
                <td>Beta Ltd</td>
            </tr>
            <tr>
                <td><strong>Respondent Advocate:</strong></td>
                <td>Jane Smith</td>
            </tr>
        </table>

        <h3>Hearing History</h3>
        <table class="history-table">
            <thead>
                <tr>
                    <th>Hearing Date</th>
                    <th>Stage</th>
                    <th>Business Conducted</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>15-12-2020</td>
                    <td>Hearing</td>
                    <td>Plaintiff absent, suit dismissed for default</td>
                </tr>
            </tbody>
        </table>

        <h3>Orders & Judgments</h3>
        <table class="orders-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Description</th>
                    <th>Order PDF</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>15-12-2020</td>
                    <td>Dismissal Order</td>
                    <td><a href="/orders/dismissal_order_mhmc010098762020.pdf">dismissal_order_mhmc010098762020.pdf</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
"""
}
