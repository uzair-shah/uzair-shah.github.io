"""Everything on your website lives in this file.

Edit the text below, then run:  python3 build.py
That rewrites index.html. To preview it:  python3 build.py --serve
"""

NAME = "Syed Uzair Shah Bukhari"
SHORT_NAME = "Home"  # text of the top-left link back to the homepage
PRONOUNS = "He/Him"  # shown after your name; set to "" to hide
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

# Extra groups shown under the main highlights, each with its own heading.
EXPERIENCE_GROUPS = [
    ("SaaS", [
        ("Master Catalog", "Led discovery for an electronics retail client: mapped where our per-warehouse "
                           "catalog fell short, compared build-versus-buy options, and scoped a single "
                           "company-wide catalog with product variants.",
         "case-studies/master-catalog.html"),
    ]),
]

# Case studies: each becomes its own page at case-studies/<slug>.html.
# Keep internal company figures out of these; the full documents stay private.
CASE_STUDIES = [
    {
        "slug": "stockflo-wms",
        "title": "Stockflo: replacing Odoo with our own warehouse management system",
        "title_link": ("Odoo", "https://www.odoo.com"),
        "subtitle": "Building an in-house warehouse management system around how our teams actually worked.",
        "meta": "Retailo · Associate Product Manager · 2022 · Saudi Arabia, Pakistan and the UAE",
        "sections": [
            ("Target audience", [
                "Commercial buyers and leads, who add suppliers, ask for quotations and raise purchase orders.",
                "Warehouse associates and leads, who receive goods, handle returns and move stock.",
                "Finance, who approve suppliers and need a clear view of what came in and at what cost.",
                "The MIS team, who set up warehouse locations and make stock adjustments.",
            ]),
            ("Customer pain points", [
                "Odoo, our warehouse software, could not keep up with how fast Retailo was growing, and "
                "integrating it with our own systems kept breaking: transactions done in Odoo did not always show up elsewhere.",
                "Our processes had to bend to fit Odoo's way of working instead of our own operating procedures.",
                "Without Odoo, our admin panel could not create or approve requests for quotation, had no user "
                "permissions, and kept no record of when purchase orders were created or approved.",
                "Receiving goods had no formal procedure, returns to suppliers went unrecorded, and anyone could "
                "move or adjust stock without a trace, which made reconciliation hard and left Finance without a "
                "clear view of inbound costs.",
                "Wrong stock counts hit the morning orders: items customers had ordered were not there, which left "
                "both customers and drivers unhappy.",
            ]),
            ("Clear objectives", [
                "Know exactly how much stock we have at any time, so orders can be planned around it.",
                "Retire Odoo without losing any operation the warehouses depended on.",
                "Work the way our own operating procedures say, not the way the software allows.",
                "Give every team the right permissions and a record of every change.",
                "Give Finance a reliable view of what was received and at what cost.",
            ]),
            ("Competitive landscape", [
                "The incumbent was Odoo, an off-the-shelf ERP: strong out of the box, but costly at our scale, "
                "hard to integrate and rigid about how work had to be done.",
                "Building in-house meant the system could follow our own procedures and plug straight into the "
                "rest of our platform, and we borrowed ideas from an existing purchasing portal so the screens felt familiar.",
            ]),
            ("My role", [
                "I mapped how purchasing, receiving and stock movements actually worked in the warehouses, then "
                "wrote the product requirements: user stories and acceptance criteria for vendors, purchasing, "
                "receiving and inventory.",
                "I worked with designers to go from Excel wireframes to full Figma screens, and with engineering to build it.",
                "I led the rollout across Saudi Arabia, Pakistan and the UAE and trained warehouse staff to use it.",
            ]),
            ("Prioritisation framework", [
                "We prioritised by impact on the biggest problem: inventory accuracy. Wrong stock counts broke the "
                "morning orders and upset customers and drivers, so knowing our real stock at any moment came first.",
                "Inside the build, the same rule applied: anything not needed to retire Odoo and keep stock accurate waited.",
            ]),
            ("The MVP", [
                "In the first version: user roles and permissions, suppliers with Finance approval, quotations and "
                "purchase orders with lock and unlock, receiving with backorders and returns, stock adjustments "
                "with reasons, and one view of every stock movement.",
                "The test for the MVP was simple: could the warehouses switch Odoo off and keep running.",
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
        "after": [
            ("Risks", [
                "Switching Odoo off while warehouses kept running: the MVP covered every operation needed to "
                "retire it before anything new was added.",
                "Getting staff in three countries to change how they worked: simple screens, and hands-on "
                "training during the rollout.",
                "Stock changing without anyone knowing why: role permissions, a reason on every adjustment and a "
                "full change history.",
                "Different tax rules in each country: supplier fields that change format by country.",
            ]),
            ("Product analytics", [
                "We tracked failed calls between Stockflo and our other systems, the problem that had made Odoo "
                "unreliable. They went from a few a month to zero, and we kept monitoring them so none slipped through.",
            ]),
            ("Feedback loops", [
                "Warehouse staff were our main customer, so we kept a very open line with them: weekly check-ins, "
                "a support channel for reporting issues, and phone calls whenever something went wrong.",
                "We visited the warehouses in person and, because we had a good working relationship, could drop "
                "in any time to see problems first-hand and get them fixed.",
            ]),
        ],
        "outcome_title": "Outcome",
        "outcome": "Stockflo replaced Odoo across Saudi Arabia, Pakistan and the UAE. Purchasing gained formal "
                   "approvals and records, receiving and stock adjustments became traceable, inventory accuracy "
                   "improved, and the platform became the base for later features such as inventory payments.",
    },
    {
        "slug": "master-catalog",
        "title": "Discovery: one product catalog for the whole company",
        "subtitle": "Working out how to move product records from per-warehouse copies to a single company catalog with variants.",
        "meta": "Retailo · Product Manager · Discovery for an electronics retail client",
        "sections": [
            ("Target audience", [
                "The immediate client: an electronics retailer selling phones and tablets through its own app.",
                "The wider market for our software: FMCG distributors who sell through field sales agents, where "
                "most products come in several sizes and pack types.",
                "Internal users: the commercial and catalog teams who create and maintain products.",
            ]),
            ("Customer pain points", [
                "Our catalog created every product at warehouse level. The same product sold in another city "
                "had to be created again, with a different product code, so one item ended up with many codes.",
                "Codes were typed by hand, so a separate team had to keep checking for duplicates.",
                "There was no idea of variants or pack sizes: each colour, size or carton had to be its own "
                "product, so nobody could see how a whole product line was performing.",
                "Changing how something was sold, for example from cartons to single pieces, meant creating a new "
                "product and losing its buying and selling history.",
                "The client wanted to show phones with colour and storage options, release products only to "
                "certain companies, manage virtual stock and update products in bulk, and most of that was not possible.",
            ]),
            ("Clear objectives", [
                "A catalog that covers the client's use cases and works properly in their app.",
                "Create each product once for the whole company, with codes generated automatically.",
                "Report on a whole product line across regions, not one warehouse at a time.",
                "Be ready to connect to the ERP systems our clients already use.",
            ]),
            ("Competitive landscape", [
                "The ERP systems brands already use set the bar: product masters with variants, unit conversions, "
                "and products released only to chosen sites.",
                "Competitors ran rule-based promotion engines with price lists for different customer groups, "
                "while our promotions worked only at order level.",
                "I trialled off-the-shelf product information tools such as Akeneo and Apimio, and looked at others "
                "like Plytix, comparing product hierarchy, pack sizes, warehouse-level stock, promotions and how "
                "easily they would connect to client ERPs and our own apps.",
            ]),
            ("My role", [
                "I led the discovery: mapped every step it took to set up a catalog today, worked through the "
                "client's use cases with them, and ran a gap analysis of each need against what our system could do.",
                "I studied how ERP systems and competitors structure their catalogs, trialled off-the-shelf "
                "product information tools, and wrote the requirements and scope for the first release.",
            ]),
            ("Prioritisation framework", [
                "A gap analysis listed every need by where it lives (our admin portal or the customer app) and "
                "rated it as complete, partly handled or not handled today.",
                "Each gap got a priority from P0 (must have to launch) to P3 (nice to have), which turned a long "
                "wish list into a clear order of work.",
            ]),
            ("The MVP", [
                "In the first release: a company-level catalog with automatic codes, product variants, releasing "
                "products to chosen companies, attributes that fit the type of product, simple discounts, "
                "multilingual names, and bulk creation and updates.",
                "Left for later: product bundles, rule-based promotions and customer price lists, pack-size "
                "conversions on transfers, and moving stock between warehouses.",
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
        ],
        "after": [
            ("Risks", [
                "Complexity: a fully flexible attribute model means more tables and more calls between them, so "
                "templates and switched-off variants kept it in check.",
                "Integration cost: building or buying both meant connecting to client ERPs and our own apps, with "
                "open questions on sync timing and whether a middleware layer was needed.",
                "App compatibility: older versions of the customer app might need a forced update to show variants.",
                "Inventory: moving to company-level products meant changing how inventory works, whichever option "
                "we chose.",
            ]),
            ("Product analytics", [
                "Reporting was one of the main reasons for the change: the new structure lets a brand see how a "
                "whole product line performs across regions, instead of stitching together separate codes from "
                "each warehouse.",
            ]),
            ("Feedback loops", [
                "We used the client's own app and hands-on demos of ready-made products to see which approaches "
                "made sense and where our catalog fell short.",
                "We also drew on in-house experience: having run our own warehouses, the team knew how ERP systems "
                "handle products in practice, and we used that to test every option.",
            ]),
        ],
        "outcome_title": "Outcome",
        "outcome": "Discovery gave the team a shared picture of where the catalog fell short, a prioritised list of "
                   "what the client needed first, a recommended product structure, and a scoped plan for the first "
                   "release, along with a clear view of the build-versus-buy options.",
    },
    {
        "slug": "inventory-payments",
        "title": "Inventory payments in Stockflo",
        "subtitle": "Turning supplier payments from spreadsheets and email threads into a tracked approval flow.",
        "meta": "Retailo · Product Manager · 2023 · Saudi Arabia, later extended to Pakistan",
        "sections": [
            ("Target audience", [
                "Commercial buyers, who raise a payment request for each purchase order.",
                "Commercial managers, who approve or reject those requests.",
                "Payment executives in Finance, who make the payment and record the proof.",
                "Finance as a whole, who need supplier statements and clean reconciliation.",
            ]),
            ("Customer pain points", [
                "Supplier payments were tracked in spreadsheets and the accounting tool, with no checks "
                "on the data, so the records were hard to trust.",
                "10–15 purchase orders were raised every day. Each payment needed a form filled in by the "
                "Commercial team and an approval by email from a Commercial Manager, which was slow and hard to track.",
                "Teams spent time chasing each other for proof that payments had gone out, and Finance "
                "struggled to produce supplier statements and reconcile accounts.",
            ]),
            ("Clear objectives", [
                "Record every payment against its purchase order inside Stockflo, our warehouse and inventory system.",
                "Make supplier statements and reconciliation easy to produce.",
                "Cut the forms and email back-and-forth from the payment flow.",
                "Know who created, approved, paid or voided every payment.",
            ]),
            ("Competitive landscape", [
                "This was an internal tool, so the real competitor was the old way of working: spreadsheets, the "
                "accounting tool and email approvals. The new flow had to be easier than that, or people would keep "
                "using it.",
            ]),
            ("My role", [
                "I wrote the product requirements document, defined the user stories and acceptance "
                "criteria, and worked with engineering to build the feature in Stockflo.",
                "It launched for Saudi Arabia first. A later update extended it to Pakistan.",
            ]),
            ("Prioritisation framework", [
                "We ranked it against other work by financial impact. It came out on top: gaps in payment tracking "
                "had already cost money, and fixing them would keep paying off long after launch.",
            ]),
            ("The MVP", [
                "In the first version: payment requests on locked purchase orders, manager approval or rejection, "
                "marking a payment as paid with its bank reference and proof, voiding a payment with a reason, and "
                "a payments view that shows what is due.",
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
        "after": [
            ("Risks", [
                "Payments marked as paid with no evidence: a bank reference and proof are required, or a reason "
                "chosen from a list.",
                "Approvals made without context: the manager sees the supplier's running balance first.",
                "Mistakes that cannot be taken back: payments are voided with a reason rather than deleted, and "
                "every step records who did it.",
                "Two teams with different needs: Commercial and Finance often wanted different things, and each "
                "held off using it until its own requests were met.",
            ]),
            ("Product analytics", [
                "We did not set formal metrics. The change was visibility: for the first time every payment, and "
                "its status, sat in one place with a full record behind it.",
            ]),
            ("Feedback loops", [
                "There was a lot of back-and-forth with Commercial and Finance while it was being built. One team "
                "would ask for one thing and the other for something different, and neither would adopt it until "
                "its needs were covered, so I worked through both sides' requests to land a flow both would use.",
                "The lesson I took: get both teams to agree on the requirements together before the build starts.",
            ]),
        ],
        "outcome_title": "Outcome",
        "outcome": "Supplier payments moved out of spreadsheets and email threads into one tracked flow with "
                   "clear owners at each step. Finance could see what had been paid and what was due, and "
                   "the procedure was documented for every team involved.",
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
