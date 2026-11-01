"""Everything on your website lives in this file.

Edit the text below, then run:  python3 build.py
That rewrites index.html. To preview it:  python3 build.py --serve
"""

NAME = "Syed Uzair Shah Bukhari"
SHORT_NAME = "Uzair"
HEADLINE = "Product manager who builds with data"
LOCATION = "Adelaide, Australia"

# Shown at the top, under your name. Keep it to 2-3 short sentences.
INTRO = (
    "I spent 2.5 years building products at Retailo, a B2B marketplace startup in "
    "Saudi Arabia, Pakistan and the UAE, through fast growth, layoffs and a pivot to SaaS. "
    "Seeing how much good product decisions depend on data, I completed a Master of "
    "Data Science at the University of Adelaide in 2026."
)

# The three things you want people to remember. Title + one line each.
PILLARS = [
    ("Startups", "Built products under real constraints, from first wireframe to rollout in three countries."),
    ("Product", "Turned messy operational problems into specs engineers could build and teams actually used."),
    ("Data", "SQL, Python and machine learning to find problems early and prove what worked."),
]

# Work highlights. Keep each to one or two sentences with a real result.
EXPERIENCE_TITLE = "Retailo Technologies"
EXPERIENCE_META = "Product & data roles · Oct 2021 – Mar 2024 · KSA, UAE & Pakistan"
HIGHLIGHTS = [
    ("Stockflo", "Led our in-house warehouse and inventory system from concept to launch across "
                 "Saudi Arabia, Pakistan and the UAE. It handled $17.5M+ of monthly purchasing and "
                 "raised inventory accuracy from 97% to 99%."),
    ("Tax compliance", "Traced a $20K/month invoice discrepancy across the app, invoices and database "
                       "with SQL, and got engineering to align all three: 100% ZATCA compliance."),
    ("Supplier payments", "Replaced spreadsheet tracking and email approvals for supplier payments "
                          "with a tracked request-and-approval flow between Commercial and Finance.",
     "case-studies/inventory-payments.html"),
    ("Inventory visibility", "Set up data pipelines and a real-time inventory dashboard that cut "
                             "out-of-stock SKUs by 5%."),
]

# Case studies: each becomes its own page at case-studies/<slug>.html.
# Keep internal company figures out of these; the full documents stay private.
CASE_STUDIES = [
    {
        "slug": "inventory-payments",
        "title": "Inventory payments in Stockflo",
        "subtitle": "Turning supplier payments from spreadsheets and email threads into a tracked approval flow.",
        "meta": "Retailo · Product Manager · 2023 · Saudi Arabia, later extended to Pakistan",
        "sections": [
            ("The problem", [
                "Supplier payments were tracked in spreadsheets and the accounting tool, with no checks "
                "on the data, so the records were hard to trust.",
                "10–15 purchase orders were raised every day. Each payment needed a form filled in by the "
                "Commercial team and an approval by email from a Commercial Manager, which was slow and hard to track.",
                "Teams spent time chasing each other for proof that payments had gone out, and Finance "
                "struggled to produce supplier statements and reconcile accounts.",
            ]),
            ("The goal", [
                "Record every payment against its purchase order inside Stockflo, our warehouse and "
                "inventory system, so supplier statements and reconciliation become easy.",
                "Make the payment flow lighter for the people doing it every day.",
            ]),
            ("My role", [
                "I wrote the product requirements document, defined the user stories and acceptance "
                "criteria, and worked with engineering to build the feature in Stockflo.",
                "It launched for Saudi Arabia first. A later update extended it to Pakistan.",
            ]),
        ],
        "flow_title": "How a payment moves",
        "flow": [
            ("Request", "Commercial buyer"),
            ("Approve", "Commercial manager"),
            ("Initiated", "Ready to pay"),
            ("Paid", "Payment executive"),
        ],
        "flow_note": "A manager can reject a request, and a payment that was recorded wrongly or failed at "
                     "the bank is marked Void with a reason.",
        "decisions_title": "Key decisions",
        "decisions": [
            ("Pay only on locked purchase orders",
             "The request button stays disabled until the purchase order is locked, so nobody pays against "
             "an order that can still change."),
            ("Show the balance before approving",
             "When a manager approves, they first see total purchases from that supplier, how much has been "
             "paid and the balance left, so approvals are made with the full picture."),
            ("Proof of payment, or a reason",
             "Marking a payment as paid needs the bank reference and a proof attachment. If there is no "
             "attachment, the user picks a reason from a list."),
            ("A record of who did what",
             "The system stores who created, approved, paid or voided every payment, giving Finance a full "
             "audit trail."),
            ("Tax handled in the flow",
             "Withholding tax is set per supplier and calculated automatically on each request. Finance can "
             "exclude it, but only by giving a reason that stays visible on the payments screen."),
            ("Credit and advance terms",
             "Requests record whether a payment is on credit or in advance; the due date is worked out from "
             "the credit days, and the payments list flags what is due."),
        ],
        "scope_title": "What I left out, on purpose",
        "scope": "Reversing a payment after it was marked paid stayed out of the first release. Payments "
                 "that went wrong are marked Void with a reason instead, which kept the first version simple.",
        "outcome_title": "Outcome",
        "outcome": "Supplier payments moved out of spreadsheets and email threads into one tracked flow with "
                   "clear owners at each step. Finance could see what had been paid and what was due, and "
                   "the procedure was documented for every team involved.",
        "footer_note": "",
    },
]

# Projects. Each: title, one-line description, tags, link.
PROJECTS = [
    {
        "title": "Document Q&A with AI (RAG)",
        "text": "Answers questions about a research paper using only the paper itself, with an "
                "evaluation set that checks correct answers and correct refusals. Compares Gemini "
                "with a locally run DeepSeek model.",
        "tags": ["Python", "LLMs", "ChromaDB", "Docker"],
        "url": "https://github.com/uzair-shah/rag_app",
    },
    {
        "title": "Modelling logistics hubs",
        "text": "Master's research: modelled a hub-and-spoke truck network as a Markov chain and "
                "simulated cost and revenue. A second unloading bay paid off; a third barely did.",
        "tags": ["MATLAB", "Markov chains", "Simulation"],
        "url": "https://github.com/uzair-shah/Research-Report",
    },
    {
        "title": "AI vs human text detector",
        "text": "Neural network that flags AI-written text, benchmarked against SVM baselines. "
                "About 0.95 validation AUC per sentence and 0.90 per paragraph on Kaggle.",
        "tags": ["TensorFlow", "scikit-learn", "Kaggle"],
        "url": "https://github.com/uzair-shah/AI-vs-Human-Text-Detector",
    },
    {
        "title": "Book catalogue scraper",
        "text": "Scraped about 1,000 books across 50 pages with polite rate limiting, stored them "
                "in a SQL database and queried the results.",
        "tags": ["Python", "BeautifulSoup", "SQL"],
        "url": "https://github.com/uzair-shah/WebScrapingProject",
    },
]

# Your photo (square works best). Set to "" to hide it.
PHOTO = "assets/photo.jpg"

# Contact details shown at the top with small logos. Leave a value as "" to hide it.
EMAIL = "s.uzair.shah01@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/syed-uzair-shah-bukhari/"
GITHUB = "https://github.com/uzair-shah"

# Main accent colour (any CSS colour).
ACCENT = "#2f6fed"
