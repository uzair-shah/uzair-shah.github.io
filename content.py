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
EXPERIENCE_PHOTO = "assets/retailo-truck.jpg"
EXPERIENCE_PHOTO_CAPTION = "On a work trip in Saudi Arabia with one of Retailo's delivery trucks."
HIGHLIGHTS = [
    ("Stockflo", "Led our in-house warehouse and inventory system from concept to launch across "
                 "Saudi Arabia, Pakistan and the UAE. It handled $17.5M+ of monthly purchasing and "
                 "raised inventory accuracy from 97% to 99%.",
     "case-studies/stockflo-wms.html"),
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
        "slug": "stockflo-wms",
        "title": "Stockflo: replacing Odoo with our own warehouse system",
        "subtitle": "Building an in-house warehouse management system around how our teams actually worked.",
        "meta": "Retailo · Associate Product Manager · 2022 · Saudi Arabia, Pakistan and the UAE",
        "sections": [
            ("The problem", [
                "Odoo, our warehouse software, could not keep up with how fast Retailo was growing, and "
                "integrating it with our own systems kept breaking: transactions done in Odoo did not always show up elsewhere.",
                "Our processes had to bend to fit Odoo's way of working instead of our own operating procedures.",
                "Without Odoo, our admin panel could not create or approve requests for quotation, had no user "
                "permissions, and kept no record of when purchase orders were created or approved.",
                "Receiving goods had no formal procedure, returns to suppliers went unrecorded, and anyone could "
                "move or adjust stock without a trace, which made reconciliation hard and left Finance without a clear view of inbound costs.",
            ]),
            ("The goal", [
                "An in-house system that follows our own procedures, integrates cleanly with the rest of our "
                "platform, and gives every team the right controls and a clear record of what happened.",
            ]),
            ("My role", [
                "I mapped how purchasing, receiving and stock movements actually worked in the warehouses, then "
                "wrote the product requirements: user stories and acceptance criteria for vendors, purchasing, "
                "receiving and inventory.",
                "I worked with designers to go from Excel wireframes to full Figma screens, and with engineering to build it.",
                "I led the rollout across Saudi Arabia, Pakistan and the UAE and trained warehouse staff to use it.",
            ]),
        ],
        "flow_title": "How stock comes in",
        "flow": [
            ("Vendor", "Created, then approved by Finance"),
            ("Quotation", "Commercial buyer"),
            ("Purchase order", "Locked by a lead"),
            ("Goods received", "Warehouse associate"),
        ],
        "flow_note": "If a supplier delivers only part of an order, the system creates a backorder for the rest, "
                     "and goods can be returned to the supplier straight from the receipt.",
        "decisions_title": "Key decisions",
        "decisions": [
            ("Permissions by role",
             "Each action, such as creating a vendor, locking a purchase order or approving a receipt, is a "
             "permission. Permissions are grouped into roles like Commercial Buyer, Warehouse Lead and Finance "
             "Associate, so access matches the job."),
            ("Lock to approve, unlock to edit",
             "Vendors and purchase orders only become usable once a lead locks them. To change one, the lead "
             "unlocks it, and the edit needs approval again."),
            ("Vendor details that fit each country",
             "The tax ID field switches between VAT for Saudi Arabia and the UAE and NTN for Pakistan, with the "
             "right format checks and registration rules for each country."),
            ("Receiving that handles real deliveries",
             "Partial deliveries create a backorder automatically, the warehouse cannot receive more than was "
             "ordered, and returns are subtracted from what was received."),
            ("Every stock adjustment needs a reason",
             "Adjustments pick a reason such as stock count, damages or expired stock, show the system quantity "
             "next to the counted one, and support bulk upload from a spreadsheet."),
            ("A history of changes",
             "Vendor creation and edits are logged and visible on screen, and purchase orders and receipts keep "
             "their timestamps, so every change can be traced."),
        ],
        "scope_title": "What I left out, on purpose",
        "scope": "The first version's job was to retire Odoo, so anything not needed for that waited: product "
                 "photos on receipts, units of measure and bundles, lot tracking, detailed payment terms (a simple "
                 "credit or advance option covered it for now), and sending purchase orders to suppliers over WhatsApp.",
        "outcome_title": "Outcome",
        "outcome": "Stockflo replaced Odoo across Saudi Arabia, Pakistan and the UAE. Purchasing gained formal "
                   "approvals and records, receiving and stock adjustments became traceable, inventory accuracy "
                   "improved, and the platform became the base for later features such as inventory payments.",
        "footer_note": "",
    },
    {
        "slug": "master-catalog",
        "title": "Discovery: one product catalog for the whole company",
        "subtitle": "Working out how to move product records from per-warehouse copies to a single company catalog with variants.",
        "meta": "Retailo · Product Manager · Discovery for an electronics retail client",
        "sections": [
            ("The problem", [
                "Our catalog created every product at warehouse level. The same product sold in another city "
                "had to be created again, with a different product code, so one item ended up with many codes.",
                "Codes were typed by hand, so a separate team had to keep checking for duplicates.",
                "There was no idea of variants or pack sizes: each colour, size or carton had to be its own "
                "product, so nobody could see how a whole product line was performing.",
                "Changing how something was sold, for example from cartons to single pieces, meant creating a new "
                "product and losing its buying and selling history.",
            ]),
            ("The client's need", [
                "An electronics retail client wanted to sell phones and tablets with variants such as colour and "
                "storage in their app, release products only to certain companies, manage virtual stock, and "
                "create and update products in bulk.",
                "Our existing catalog could not do most of this, so the question was what to change, in what "
                "order, and whether to build or buy.",
            ]),
            ("My role", [
                "I led the discovery: mapped every step it took to set up a catalog today, worked through the "
                "client's use cases with them, and ran a gap analysis of each need against what our system could do.",
                "I studied how ERP systems and competitors structure their catalogs, trialled off-the-shelf "
                "product information tools, and wrote the requirements and scope for the first release.",
            ]),
        ],
        "flow_title": "The new product structure",
        "flow": [
            ("Company", "One catalog for everyone"),
            ("Product master", "Brand, category, tax, units"),
            ("Variants", "Colour, storage, size"),
            ("Released", "To chosen companies and warehouses"),
        ],
        "flow_note": "Before, each warehouse kept its own copy of every product. In the new structure a product is "
                     "created once, its variants get their own codes automatically, and it is released where it should be sold.",
        "decisions_title": "What discovery decided",
        "decisions": [
            ("One catalog at company level",
             "Products, categories and brands live at company level with codes generated automatically, while "
             "customer-facing app categories stay local so each warehouse can still run its own promotions."),
            ("Product masters with variants",
             "A product master holds the shared details, and variants such as colour or storage hang off it, so a "
             "whole product line can be sold, searched and reported on together."),
            ("Units of measure on the product",
             "Conversions such as pieces to cartons sit on the product master, so stock can be bought in one unit and "
             "sold in another without creating a new product or losing its history."),
            ("Two data models, weighed openly",
             "I compared a flexible model built on product families and attribute templates with a simpler one that "
             "extends the existing screens. The trade-off was flexibility against complexity, so templates and "
             "variants that start switched off kept the flexible option manageable."),
            ("Build versus buy",
             "I trialled off-the-shelf product information tools such as Akeneo and Apimio against our needs: "
             "product hierarchy, pack sizes, warehouse-level stock, promotions and how easily they would connect "
             "to client ERPs and our own apps."),
            ("A prioritised gap analysis",
             "Every client need was rated as complete, partly handled or not handled today, and given a priority "
             "from P0 to P3, which turned a long wish list into a clear order of work."),
        ],
        "scope_title": "What I left out, on purpose",
        "scope": "The first release focused on the company catalog, variants, releasing products to chosen companies, "
                 "bulk updates and simple discounts. Product bundles, rule-based promotions and customer price lists, "
                 "pack-size conversions on transfers, and moving stock between warehouses were left for later.",
        "outcome_title": "Outcome",
        "outcome": "Discovery gave the team a shared picture of where the catalog fell short, a prioritised list of "
                   "what the client needed first, a recommended product structure, and a scoped plan for the first "
                   "release, along with a clear view of the build-versus-buy options.",
        "footer_note": "",
    },
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
