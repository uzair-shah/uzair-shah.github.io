"""Everything on your website lives in this file.

Edit the text below, then run:  python3 build.py
That rewrites index.html. To preview it:  python3 build.py --serve
"""

NAME = "Syed Uzair Shah Bukhari"
SHORT_NAME = "Home"  # text of the top-left link back to the homepage
PRONOUNS = "He/Him"  # shown after your name; set to "" to hide
HEADLINE = "Product manager who builds with data"
LOCATION = "Adelaide, Australia"

# Visitor counter (GoatCounter, free, no cookies). Put your GoatCounter code here,
# e.g. "uzair-shah" for uzair-shah.goatcounter.com. Set to "" to turn it off.
GOATCOUNTER = "uzair-shah"

# Font for headings. "Newsreader" gives a serif, editorial look; set to "" to use Inter everywhere.
HEADING_FONT = ""

# Small "open to work" badge above your name. Set to "" to hide (the location shows instead).
OPEN_TO = ""

# Your path at Retailo, shown as a timeline under Experience. (role, dates)
CAREER_STEPS = [
    ("Analyst, Warehousing", "Oct 2021 – Jan 2022"),
    ("Associate Product Manager, Operations", "Feb 2022 – Sep 2022"),
    ("Product Manager, Finance and Data", "Oct 2022 – Mar 2024"),
]

# Big numbers shown under your intro. (number, label). Keep to 4.
STATS = [
    ("$17.5M+", "monthly purchasing run through Stockflo"),
    ("97% → 99%", "inventory accuracy after launch"),
    ("$20K/mo", "invoice discrepancy traced and fixed"),
    ("3 countries", "Saudi Arabia, Pakistan and the UAE"),
]

# Your CV, offered as a download button next to LinkedIn and GitHub. Set to "" to hide.
CV_FILE = ""

# Shown at the top, under your name. Keep it to 2-3 short sentences.
INTRO = (
    "I spent 2.5 years building products at Retailo, a B2B marketplace startup in "
    "Saudi Arabia, Pakistan and the UAE. "
    "Seeing how much good product decisions depend on data, I completed a Master of "
    "Data Science at the University of Adelaide in 2026."
)

# The three things you want people to remember. Title + one line each.
PILLARS = [
    ("Startups", "Built products under real constraints, from first wireframe to rollout in three countries."),
    ("Product", "Turned messy operational problems into specs engineers could build and teams actually used."),
    ("Data and AI", "SQL, Python, machine learning and AI tools to find problems early and prove what worked."),
]

# Your current block, shown above Retailo with the same kind of timeline. (step, dates)
CURRENT_TITLE = "University of Adelaide and freelance"
CURRENT_META = "Study, tutoring and data work · Sep 2024 – Present · Adelaide, Australia"
CURRENT_STEPS = [
    ("Master of Data Science, University of Adelaide", "Sep 2024 – Aug 2026"),
    ("Mathematics Tutor, Maths Learning Centre", "Apr 2025 – Present"),
    ("Freelance data work", "Present"),
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
        "image": "assets/wh-racking.jpg",
        "title": "Stockflo: replacing Odoo with our own warehouse management system",
        "title_link": ("Odoo", "https://www.odoo.com"),
        "subtitle": "Building an in-house warehouse management system around how our teams actually worked.",
        "meta": "Retailo · Associate Product Manager · 2022 · Saudi Arabia, Pakistan and the UAE",
        "sections": [
            ("Target audience", [
                "Commercial buyers, who provide vendors, ask for quotations and raise purchase orders, and their "
                "leads, who approve those purchase orders.",
                "Warehouse associates and leads, who receive goods, handle returns and move stock.",
                "Finance, who approve suppliers and need a clear view of what came in and at what cost.",
                "The MIS (management information systems) team, the warehouse team's tech arm, who make sure stock "
                "on the ground matches stock in the system, set up warehouse locations and make stock adjustments.",
            ]),
            ("Discovery", [
                "I spent time in the warehouses watching how goods were bought, received, moved and adjusted, "
                "and mapped every step from vendor to stock on the shelf.",
                "I spoke with each team that touched stock: Commercial buyers and their leads, warehouse "
                "associates and leads, Finance and the MIS team, to see where Odoo and our admin panel let them down.",
                "I traced the wrong stock counts behind failed morning orders back to their causes: transactions "
                "in Odoo that never reached the admin panel, receiving with no formal procedure, and adjustments "
                "anyone could make without a trace.",
                "What discovery decided: rather than keep patching the Odoo integration, build our own system "
                "around how the teams actually worked.",
            ]),
            ("Customer pain points", [
                ("Why we needed Odoo in the first place", [
                    "Our admin panel could not create or approve requests for quotation, had no user permissions, and "
                    "kept no record of when purchase orders were created or approved.",
                    "Receiving goods had no formal procedure, returns to suppliers went unrecorded, and anyone could "
                    "move or adjust stock without a trace.",
                    "That made reconciliation hard and left Finance without a clear view of what came in and at what cost.",
                ]),
                ("Why we built Stockflo despite having Odoo", [
                    "Odoo could not keep up with how fast Retailo was growing, and its worker-based pricing made it "
                    "expensive at our scale.",
                    "Integrating it with our own systems kept breaking: transactions done in Odoo did not show up in "
                    "other integrated systems such as our admin panel.",
                    "Wrong stock counts hit the morning orders: items customers had ordered were not there, which left "
                    "both customers and drivers unhappy.",
                    "We lacked access controls for specific steps, such as who could approve a purchase order before "
                    "its goods were received, and that had to change.",
                ]),
            ]),
            ("Clear objectives", [
                "Know exactly how much stock we have at any time, so orders can be planned around it.",
                "Retire Odoo without losing any operation the warehouses depended on.",
                "Give every team the right permissions, so the wrong people cannot carry out the wrong tasks, and keep "
                "a record of every change.",
                "Give Finance a reliable view of what was received and at what cost.",
            ]),
            ("My role", [
                "I mapped how purchasing, receiving and stock movements actually worked in the warehouses, then "
                "wrote the product requirements: user stories and acceptance criteria for vendors, purchasing, "
                "receiving and inventory.",
                "I worked with designers to go from Excel wireframes to full Figma screens, and with engineering to build it.",
                "I led the rollout across Saudi Arabia, Pakistan and the UAE, training warehouse staff through "
                "presentations and video walkthroughs.",
            ]),
            ("Two very different warehouses", {
                "intro": "Stockflo had to work for two quite different ways of running a warehouse.",
                "cards": [
                    ("Saudi Arabia: machinery-led",
                     "Forklifts and pallet racking did most of the work. Stock was concentrated in a smaller number "
                     "of products, each held in large quantities."),
                    ("Pakistan: labour-led",
                     "Many lower-value products, handled mostly by hand, because labour there costs less than machinery."),
                ],
                "outro": "The same system had to support both, from a few big pallets to many small, hand-picked items.",
            }),
            ("In the warehouse", {
                "photos": [
                    ("assets/wh-inbound-returns.jpg", "Inbound and return area, where goods are received against purchase orders and returns are logged."),
                    ("assets/wh-outbound-staging.jpg", "Outbound and staging area, where picked orders wait for delivery."),
                    ("assets/wh-bin-locations.jpg", "Every rack position has its own labelled location code."),
                    ("assets/wh-racking.jpg", "Pallet racking in one of our warehouses."),
                ],
            }),
            ("Prioritisation framework", [
                "We prioritised by impact on the biggest problem: inventory accuracy. Wrong stock counts broke the "
                "morning orders and upset customers and drivers, so knowing our real stock at any moment came first.",
                "Inside the build, the same rule applied: anything not needed to retire Odoo and keep stock accurate waited.",
            ]),
            ("The MVP", {
                "intro": "The test for the first version was simple: could the warehouses switch Odoo off and keep "
                         "running? That meant five things had to work from day one.",
                "cards": [
                    ("Users", "Roles and permissions, so each person can only do their own job."),
                    ("Vendors", "Added by Commercial, approved by Finance before they can be used."),
                    ("Buying", "Quotations and purchase orders, locked once approved."),
                    ("Receiving", "Goods received against the order, with backorders and returns."),
                    ("Stock", "Adjustments with a reason, and one view of every stock movement."),
                ],
            }),
            ("What I left out, on purpose", {
                "intro": "Anything not needed to retire Odoo waited for a later version:",
                "tags": [
                    "Product photos on receipts",
                    "Units of measure and bundles",
                    "Lot tracking",
                    "Detailed payment terms",
                    "Sending orders over WhatsApp",
                ],
                "outro": "For payment terms, a simple credit or advance option covered the first version.",
            }),
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
             "Each adjustment must state why it happened, such as a stock count, damages or expired stock. The "
             "screen shows the system quantity next to the counted one, and large changes can be uploaded in bulk "
             "from a spreadsheet."),
            ("A history of changes",
             "Vendor creation and edits are logged and visible on screen, and purchase orders and receipts keep "
             "their timestamps. Because we could see who changed what, we could correct specific behaviours by "
             "working directly with the people involved, which gave us much better governance over stock."),
        ],
        "after": [
            ("Risks", [
                "Switching Odoo off while warehouses kept running: the MVP covered every operation needed to "
                "retire it before anything new was added.",
                "Getting staff in three countries to change how they worked: I ran presentations and sent out "
                "video walkthroughs during the rollout.",
                "Stock changing without anyone knowing why: role permissions, a reason on every adjustment and a "
                "full change history.",
                "Different tax rules in each country: supplier fields that change format by country.",
            ]),
            ("Product analytics", [
                "Trust in the new system came first. For the first month or so, warehouse staff checked after every "
                "update that the stock Stockflo sent matched the stock on the admin panel.",
                "Our logs showed exactly when every inventory change was made, and we reconciled those against the "
                "changes orders made on the admin panel, tracked on a dashboard.",
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
        "thumb": "catalog",
        "title": "Discovery: one product catalog for the whole company",
        "subtitle": "Working out how to move product records from per-warehouse copies to a single company catalog with variants.",
        "meta": "Retailo · Product Manager · Discovery for an electronics retail client",
        "sections": [
            ("Problem statement", {
                "intro": "Our catalog created every product separately for each warehouse, so one product ended up "
                         "with many codes, no variants, and no history once its pack size changed. An electronics "
                         "retail client needed one catalog for the whole company, with colour and storage options, "
                         "products released only to chosen companies, and bulk updates. Most of that was not possible.",
            }),
            ("Key terms", {
                "intro": "A master catalog is the single source of truth for products. Each SKU identifies one "
                         "product, variants capture differences such as colour or storage, and stock sits at "
                         "locations and stores that all read from the same catalog.",
                "photos": [("assets/case-studies/master-catalog-vocabulary.webp",
                            "Core inventory vocabulary around a master catalog.")],
                "natural": True,
                "source": ("Ecorn: Multi Store Inventory Management, A Practical Guide",
                           "https://www.ecorn.agency/blog/multi-store-inventory-management"),
            }),
            ("Discovery", [
                "I led the discovery: mapped every step it took to set up a catalog today, worked through the "
                "client's use cases with them, and ran a gap analysis of each need against what our system could do.",
                "I studied how ERP systems and competitors structure their catalogs, trialled off-the-shelf "
                "product information tools, and wrote the requirements and scope for the first release.",
            ]),
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
        "thumb": "payments",
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
            ("Discovery", [
                "I followed a supplier payment from start to finish: the request form Commercial filled in, the "
                "email approval from a Commercial Manager, the payment by Finance and the proof sent back.",
                "I sat with Commercial buyers, Commercial managers and Finance's payment executives to see where "
                "each handover slowed down or got lost.",
                "I reviewed the spreadsheets and accounting records used to track payments. They showed why "
                "statements and reconciliation were so hard: nothing linked a payment back to its purchase order.",
                "What discovery decided: build payments into Stockflo, on the purchase orders that already lived "
                "there, instead of improving the spreadsheet.",
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
    {
        "slug": "cash-collection",
        "thumb": "cash",
        "title": "Cash collection: closing out the delivery day",
        "subtitle": "Making end-of-day cash deposits faster to record and easier to check.",
        "meta": "Retailo · Operations · End-of-day cash and returns",
        "sections": [
            ("Target audience", [
                "Delivery agents, who bring back the day's cash and any returned stock.",
                "Cash counter staff, who take and record deposits.",
                "Dock executives and stock sorters, who check returned stock.",
                "The logistics team, who resolve any gap between cash expected and cash deposited.",
            ]),
            ("Customer pain points", [
                "Every deposit was entered into a long table by hand, which was slow, easy to get wrong and kept "
                "agents waiting in line.",
                "The cash an agent deposited did not always match the cash the logistics app said they had collected.",
                "Returns were a common source of gaps: too few returned could mean a weak morning check, stock "
                "dropped off by mistake or theft; too many usually meant a partial delivery was marked as complete, "
                "so the cash came up short.",
            ]),
            ("Clear objectives", [
                "Get every agent's cash deposited and recorded quickly at the end of the day.",
                "Make recording a deposit fast and consistent, with no long table to scroll through.",
                "Catch cash and returns mismatches and send them to the right team to resolve.",
            ]),
            ("My role", [
                "I mapped the end-of-day cash and returns process from arrival to final check, including where "
                "mismatches came from.",
                "I built a simple Google Sheets entry form for deposits: it writes each entry into the shared "
                "table on its own and clears itself, ready for the next agent.",
            ]),
            ("The MVP", [
                "A form on top of the Google Sheet the team already used, automated with Apps Script. No new app, "
                "no training on new software, and it worked from day one.",
            ]),
        ],
        "flow_title": "The agent's end-of-day flow",
        "diagram": [
            ("Agent returns to the warehouse", "Delivery agent",
             "Comes back at the end of the route with the day's cash, and either no stock left or some returns.",
             ("If there are returns", "The van docks at the gate, where an executive checks the agent's returns "
              "slip against the physical stock and files it with the morning sheet.")),
            ("Count the cash", "Delivery agent",
             "Takes paper and rubber bands from the deposit counter, sorts the cash by note, and writes down the "
             "total for each.", None),
            ("Cash deposit machine", "Delivery agent",
             "Enters their agent app ID and deposits the cash. The machine shows how much it accepted and hands "
             "back any notes it rejects.", None),
            ("Deposit counter", "Agent and counter staff",
             "The agent queues and deposits the rejected notes. The counter logs the deposit in the Google Sheets "
             "form, which saves it to the shared table and clears itself for the next agent.", None),
            ("Check against the app", "Logistics team",
             "The cash deposited is compared with the cash the logistics app says the agent collected.",
             ("If the amounts don't match", "The logistics team decides whether the agent is genuinely short or "
              "the system made a mistake.")),
        ],
        "flow_note": "",
        "decisions_title": "What made it work",
        "decisions": [
            ("A form, not a long table",
             "Staff fill in a few fields instead of finding the right row in a long table. The sheet records the "
             "entry and resets the form, so the next agent can be served straight away."),
            ("Machine first, counter second",
             "The deposit machine takes most of the cash and records it against the agent's app ID, so only the "
             "notes it rejects go to the counter queue."),
            ("Check returns at the dock",
             "Returned stock is checked against the agent's slip as soon as the van arrives, which is where short "
             "and over returns show up."),
            ("Separate real shortfalls from system errors",
             "A mismatch goes to the logistics team, who decide whether the agent is short or the app recorded "
             "the wrong amount, so agents are not blamed for system errors."),
        ],
        "after": [
            ("Risks", [
                "Over-returns hiding partial deliveries: the returns record from the dock made these visible, "
                "since they showed up as cash shortfalls.",
                "On-the-spot discounts given through customer care did not fit the flow; the plan was to phase "
                "them out rather than build around them.",
                "Typing errors and overwritten rows: a fixed form with the same fields every time, cleared after "
                "each entry.",
            ]),
        ],
        "outcome_title": "Outcome",
        "outcome": "Deposits were logged through a short form instead of a long table, every entry landed in the "
                   "shared sheet automatically, and the form was ready for the next agent straight away. Mismatches "
                   "had a clear path to the logistics team for resolution.",
    },
]

# Project pages: each becomes its own page at projects/<slug>.html (written from each GitHub repo's actual files).
PROJECT_PAGES = [{'slug': 'rag-app',
  'title': 'Ask-a-PDF Question Answering (RAG) with Model Comparison',
  'subtitle': "A small app that answers questions about a research paper using only the paper's text, then "
              'tests how accurately and quickly two AI models do it.',
  'meta': 'Python · Sentence-Transformers (all-MiniLM-L6-v2) · ChromaDB · Gemini (gemini-3-flash-preview) · '
          'DeepSeek-R1 via Ollama · FastAPI · Docker',
  'github': 'https://github.com/uzair-shah/rag-app',
  'sections': [('What it does',
                ["Answers plain-English questions about one PDF: Gregory Warrington's 2005 maths paper "
                 "'Juggling Probabilities' (American Mathematical Monthly).",
                 'Uses retrieval-augmented generation (RAG): it first finds the most relevant passages, then '
                 'asks an AI model to answer using only those passages.',
                 "The model is told to say so honestly when the paper doesn't contain the answer, rather "
                 'than making something up.',
                 'Compares a cloud model (Google Gemini) against a model running locally on a laptop '
                 '(DeepSeek-R1 via Ollama) on accuracy and response time.',
                 'Also exposes the pipeline as a web API: POST a question to /ask/ and get an answer back '
                 '(FastAPI).']),
               ('The data',
                ['Input is a single PDF stored in the repo: Warrington-JugglingProbabilities-2005.pdf.',
                 'Text is extracted page by page, then cleaned with regular expressions to strip licence '
                 'lines, journal headers, null characters and blank lines.',
                 'The cleaned text is cut into 800-character chunks that overlap by 100 characters so ideas '
                 "aren't split mid-thought.",
                 'The saved vector database (chroma_db/) holds 50 embedded chunks in a collection named '
                 "'juggling_paper'."])],
  'flow_title': 'How it works',
  'diagram': [('Read the PDF',
               'pypdf · pdf_to_text()',
               'Extracts text from every page of the juggling paper into one string.',
               None),
              ('Clean the text',
               're · clean_text()',
               'Removes licence boilerplate, journal headers, null characters and empty lines.',
               None),
              ('Chunk',
               'chunk_text(text, 800, 100)',
               'Splits text into 800-character pieces overlapping by 100 characters (50 chunks stored).',
               None),
              ('Embed & store',
               'all-MiniLM-L6-v2 · ChromaDB (./chroma_db)',
               'Turns each chunk into a vector and saves it locally; skipped if the collection already has '
               'data.',
               None),
              ('Retrieve',
               'search()',
               'Embeds the question and fetches the closest chunks (top 3 in evaluation, top 5 in the API).',
               None),
              ('Answer',
               'ask_llm_gemini() / ask_llm_deep_seek()',
               'Sends the passages plus the question to an LLM told to answer only from the context.',
               ('If Gemini',
                'Cloud call to gemini-3-flash-preview with a pause and up to 3 retries; otherwise '
                'DeepSeek-R1 runs locally via Ollama.')),
              ('Score',
               'score_query() · run_eval()',
               'Checks each answer for expected keywords (or refusal phrases for trick questions) and '
               'records response time.',
               None)],
  'after': [("How it's evaluated",
             {'intro': 'A hand-written test set of 12 questions (test_queries.txt) checks both correct '
                       'answers and correct refusals.',
              'cards': [['10 answerable questions',
                         'Across categories: easy facts (author, year), metadata (references, page count), '
                         "definitions, a theorem explanation, a synthesis comparison, a vague 'main idea' "
                         'question and a specific historical fact.'],
                        ['2 trick questions',
                         "'Banana sandwich recipe' and 'Did the egg come before the chicken?' — the model "
                         "passes only if it refuses (e.g. says the context 'does not' contain it)."],
                        ['Keyword scoring',
                         'An answerable question passes if the reply contains at least one expected keyword '
                         "(e.g. 'Warrington' or 'Gregory' for the author)."],
                        ['Timing',
                         'Each model call is timed; for Gemini, a deliberate 20-second rate-limit pause is '
                         'subtracted from the measured time.']]}),
            ('Results',
             {'intro': 'Saved notebook output from one run of all 12 test questions (top 3 retrieved '
                       'passages per question):',
              'cards': [['Gemini: 10 / 12 passed',
                         "Missed 'What are the references' and 'What's the main idea?'. Correctly refused "
                         'both trick questions.'],
                        ['DeepSeek-R1: 9 / 12 passed',
                         "Missed the same two questions, and failed to refuse 'Banana sandwich recipe'."],
                        ['Gemini: 4.76 s average response', 'Ranged from 2.57 s to 8.22 s per question.'],
                        ['DeepSeek-R1: 31.37 s average response',
                         'Ranged from 15.54 s to 59.92 s per question, about 6.6× slower than Gemini on a '
                         'local laptop.']],
              'outro': "The author's own takeaways: local models work end-to-end on a laptop; quality drops "
                       'depend on question type; reasoning models like DeepSeek-R1 trade a lot of latency '
                       "for thinking and aren't always right for RAG; Gemini Flash performed better than "
                       'DeepSeek-R1 8B.'}),
            ('Inside the code',
             {'cards': [['Retrieval',
                         'Question and chunks are embedded with all-MiniLM-L6-v2; ChromaDB returns the '
                         'nearest chunks by distance score.'],
                        ['Embed once',
                         'Embeddings are only computed when the ChromaDB collection is empty, so reruns skip '
                         're-encoding.'],
                        ['Grounded prompt',
                         "Retrieved chunks are joined under a 'Context:' header followed by the 'Question:', "
                         'with a system instruction to use only that context.'],
                        ['Retry with backoff',
                         'Gemini calls retry up to 3 times with exponential backoff on API errors.']]}),
            ('Tech used',
             {'tags': ['Python',
                       'pypdf',
                       'Regex text cleaning',
                       'Sentence-Transformers',
                       'ChromaDB',
                       'Google Gemini API',
                       'Ollama',
                       'DeepSeek-R1',
                       'FastAPI',
                       'Pydantic',
                       'Docker',
                       'Jupyter']}),
            ('Limitations (noted by the author)',
             ["Keyword scoring isn't fully reliable: DeepSeek said an answer wasn't in the context but "
              "answered anyway, and the test didn't catch it.",
              'DeepSeek-R1 may need more parameters to perform better.'])]},
 {'slug': 'logistics-research',
  'title': 'Modelling truck traffic at a logistics hub',
  'subtitle': 'A Master of Data Science research project that uses the mathematics of juggling to study when '
              'trucks pile up at a hub, and what extra unloading bays are worth.',
  'meta': 'MATLAB · Markov chains · Monte Carlo simulation · Combinatorics (multiplex juggling) · LaTeX · '
          'Excel',
  'github': 'https://github.com/uzair-shah/logistics-hub-juggling-model',
  'sections': [('The question',
                ['In a hub-and-spoke network, goods from many locations go through one central hub instead '
                 'of travelling point to point.',
                 'This keeps costs down, but the hub can only unload so many trucks at once, so simultaneous '
                 'arrivals cause waiting.',
                 'Waiting trucks delay goods further down the supply chain and cost logistics companies '
                 'money.',
                 'The project asks: how do the number of unloading bays and truck travel times affect cost, '
                 'revenue and profit at the hub?']),
               ('The idea in plain English',
                {'intro': 'A juggler throws balls so they land on future beats. A dispatcher sends trucks so '
                          "they return to the hub at future hours. The project borrows the juggler's maths "
                          'to describe the hub.',
                 'cards': [['Trucks are balls',
                            'Each of up to three trucks is treated like a ball being juggled.'],
                           ['Hours are beats',
                            'Time moves in one-hour steps, just as juggling is counted in beats.'],
                           ['Travel time is throw height',
                            "A truck that returns to the hub in 3 hours is a '3-throw', like a ball thrown "
                            'high enough to land 3 beats later.'],
                           ['States are arrival schedules',
                            'A code like 110 means one truck arrives now, one arrives in an hour, and none '
                            'in two hours. 200 means two trucks arrive at once.'],
                           ['Multiplex juggling',
                            "Ordinary juggling allows one catch per beat; 'multiplex' juggling allows "
                            'several, which mirrors several trucks reaching the hub together.'],
                           ['Adding and dropping',
                            'Trucks can be added (e.g. extra demand) or removed (e.g. breakdown or '
                            'refuelling), like a juggler adding or dropping a ball.']],
                 'photos': [['assets/projects/logistics-research/hub-and-spoke-network.png',
                             'The modelled network: a central hub served by three trucks travelling to and '
                             'from three spokes.']]})],
  'flow_title': 'How the model works',
  'diagram': [('Describe the hub as juggling',
               'Multiplex juggling model J(≤b, h, B)',
               'Trucks become balls, hours become beats and travel time becomes throw height; b trucks, max '
               'height h, B unloading bays.',
               None),
              ('Generate every state',
               'CreateStMatrix_1Bay.m (and _2Bay, _3Bay, _1Bay_6H)',
               'A queue-based search lists every reachable arrival schedule and the throws, adds and drops '
               'that connect them.',
               ('If more trucks arrive than there are bays',
                'the extra trucks are thrown 1 hour ahead, i.e. delayed.')),
              ('Build the transition matrix',
               'Uniform probabilities (Markov chain)',
               'Every allowed move out of a state gets equal probability, e.g. 1/4 for each of four options.',
               None),
              ('Compute the long-run behaviour',
               'Eigenvector of the transposed matrix, normalised',
               'Gives the theoretical stationary distribution: the long-run share of time spent in each '
               'state.',
               None),
              ('Simulate and track money',
               'SimRun_1Bay.m, SimRun_2Bay.m, SimRun_3Bay.m, SimRun_1Bay_6H.m',
               '100,000 steps from every starting state across 30 seeds, adding bay, delay and fixed costs '
               'and revenue per unloaded truck.',
               None),
              ('Check and compare',
               'RSSQ convergence plots; Cost Results.xlsx',
               'Simulated and theoretical distributions are compared, then average cost, revenue and profit '
               'are compared across the four experiments.',
               None)],
  'after': [('How it was modelled',
             {'intro': 'The main model, written J(≤3, 3, 1), has at most 3 trucks, a maximum travel time of '
                       '3 hours and 1 unloading bay.',
              'bullets': ['With one bay, if two trucks arrive together, one is unloaded and the other is '
                          'pushed back one hour, which incurs a delay cost.',
                          'MATLAB code generated every possible arrival state and the moves between them: 20 '
                          'states for the main model.',
                          'Each allowed move from a state was given equal probability, turning the state '
                          'graph into a Markov chain (the next state depends only on the current one).',
                          "The chain's 'stationary distribution' gives the long-run share of time the hub "
                          'spends in each state; it was computed from an eigenvector of the transition '
                          'matrix.',
                          'A Monte Carlo simulation ran 100,000 steps from every starting state over 30 '
                          'random seeds, tallying cost and revenue at each step.',
                          'Cost = fixed hub cost + bay cost per truck unloaded + delay cost per truck kept '
                          'waiting; revenue = base revenue per truck unloaded.'],
              'photos': [['assets/projects/logistics-research/juggling-state-graph.png',
                          'The state graph for J(≤3,3,1): each circle is an arrival schedule, each arrow a '
                          "possible move labelled with its 'throw height'. Dotted and dashed arrows add or "
                          'remove a truck.']]}),
            ('Four experiments',
             {'cards': [['Experiment 1', '1 bay, travel time up to 3 hours (the base model).'],
                        ['Experiment 2', '2 bays, travel time up to 3 hours, higher bay cost.'],
                        ['Experiment 3', '3 bays, travel time up to 3 hours, highest bay cost.'],
                        ['Experiment 4', '1 bay, maximum travel time doubled to 6 hours (84 states).']]}),
            ('Results',
             {'bullets': ['The simulation matched the theory: the error (RSSQ) for the base model fell to '
                          '3.37 × 10⁻⁸ after 100,000 iterations.',
                          'One bay produced the largest loss, about 0.16 million (−155,314.67), driven by '
                          'frequent two-truck arrivals and delay costs.',
                          'Two bays gave the only profit, about 0.20 million (198,257.35).',
                          'A third bay added little: three trucks rarely arrive together, so it sat largely '
                          'unused while its cost was still paid (−3,139.73).',
                          'Doubling travel time lowered both cost and revenue; the loss shrank (−49,628.70), '
                          'but idle hours with fixed costs kept one bay unprofitable.',
                          'Caveat from the report: the model has not been calibrated or validated against '
                          'any real hub-and-spoke network, so it cannot yet support real-world '
                          'recommendations.'],
              'photos': [['assets/projects/logistics-research/simultaneous-arrivals-by-experiment.png',
                          'Share of time with 0, 1, 2 or 3 trucks arriving at once, per experiment. '
                          'Three-truck arrivals are the rarest in every case.'],
                         ['assets/projects/logistics-research/profit-by-experiment.png',
                          'Average profit per experiment: only the two-bay setup (Experiment 2) is '
                          'profitable.']],
              'outro': 'The report also notes the model is small (three trucks, up to three bays) and '
                       'assumes trucks are dispatched at random, whereas real dispatching is scheduled.'}),
            ('Inside the code',
             ['CreateStMatrix_*.m scripts explore states with a queue: from each state they try every add, '
              'drop and throw, recording new states and the throw heights linking them.',
              "SimRun_*.m scripts hold each experiment's transition matrix, compute the theoretical "
              'stationary distribution, run the seeded simulation and plot convergence.',
              'Next states are sampled by inverse transform sampling: a random number is matched against '
              'cumulative probabilities.',
              "TotalStateCount.m checks state counts with the 'stars and bars' counting formula.",
              'Outputs were saved to Excel for summary charts; the write-up is a LaTeX report with a '
              'compiled PDF.']),
            ('Tools',
             {'tags': ['MATLAB',
                       'Markov chains',
                       'Stationary distributions / eigenvectors',
                       'Monte Carlo simulation',
                       'Inverse transform sampling',
                       'Combinatorics (stars and bars)',
                       'Juggling state graphs',
                       'Excel',
                       'LaTeX / Overleaf']})]},
 {'slug': 'text-detector',
  'title': 'AI vs Human Text Detector',
  'subtitle': 'A neural network that scores each sentence of a paragraph and averages the scores to estimate '
              'whether the paragraph was written by a human or by AI.',
  'meta': 'Python · TensorFlow / Keras · scikit-learn · NumPy · pandas · Matplotlib · seaborn · Jupyter',
  'github': 'https://github.com/uzair-shah/ai-vs-human-text-classifier',
  'sections': [('What it does',
                ['Takes a paragraph that has already been turned into numbers (embeddings) and outputs a '
                 'probability that it was written by AI.',
                 'Scores every sentence separately with a trained neural network, then averages the sentence '
                 'scores into one paragraph score.',
                 'Reached a paragraph-level AUC of 0.90 on the provided validation set.',
                 'Writes predictions for the test set to a CSV file with columns id and y_prob, ready for '
                 'submission.']),
               ('The data',
                {'intro': 'The text arrives pre-embedded: each sentence is a 100 × 768 grid of numbers (up '
                          'to 100 tokens, 768 values per token), padded with zeros for shorter sentences.',
                 'cards': [['Human sentences',
                            '8,161 real human sentences plus 5 synthetic human sentences, all labelled 0.'],
                           ['AI sentences',
                            '8,161 AI-written sentences plus 1,340 synthetic AI sentences, all labelled 1.'],
                           ['Combined set',
                            '17,667 sentences in total, shuffled and split 80/20 into 14,133 for training '
                            'and 3,534 for checking the model.'],
                           ['Paragraph files',
                            'Separate validation and test files hold whole paragraphs as lists of sentence '
                            'embeddings; the validation file also has the true label.']]})],
  'flow_title': 'How it works',
  'diagram': [('Load embeddings',
               'NumPy',
               'Loads human, AI and synthetic sentence embeddings (each 100 × 768) and labels human 0, AI 1, '
               'giving 17,667 sentences.',
               None),
              ('Explore sentence lengths',
               'Matplotlib',
               'Counts real (non-padding) tokens per sentence and compares human vs AI length distributions.',
               None),
              ('Split the data',
               'scikit-learn',
               'Shuffles and splits 80/20 into 14,133 training and 3,534 validation sentences.',
               None),
              ('Train sentence classifier',
               'Keras feed-forward network',
               'Flatten → Dense 300 → Dense 100 → sigmoid, trained with Nadam, an exponential learning-rate '
               'schedule and early stopping; the model is saved.',
               ('If validation loss stops improving for 2 epochs',
                'training halts and the best weights are restored (stopped after epoch 18).')),
              ('Score paragraphs',
               'predict_paragraphs',
               'Each sentence in a paragraph gets an AI probability; the probabilities are averaged into one '
               'paragraph score.',
               None),
              ('Evaluate and export',
               'scikit-learn, pandas',
               'Computes paragraph-level ROC AUC on the validation set (0.90) and writes test predictions to '
               'a CSV with id and y_prob.',
               None)],
  'after': [('Exploring the data',
             {'intro': 'Before modelling, the notebook counts the non-padding tokens in each sentence to '
                       'compare sentence lengths for human and AI text.',
              'photos': [['assets/projects/text-detector/human-sentence-lengths.png',
                          'Human-written training sentences: histogram and boxplot of sentence length '
                          '(tokens). Lengths spread widely, with many long outliers.'],
                         ['assets/projects/text-detector/ai-sentence-lengths.png',
                          'AI-written training sentences: same plots. The median is slightly higher and '
                          'lengths are more tightly grouped, with fewer long outliers.']]}),
            ('The model',
             {'intro': 'A feed-forward neural network built in Keras that classifies a single sentence.',
              'cards': [['Architecture',
                         'Flatten (76,800 inputs) → Dense 300 (ReLU) → Dense 100 (ReLU) → Dense 1 (sigmoid). '
                         '23,070,501 trainable parameters.'],
                        ['Training setup',
                         'Binary cross-entropy loss, Nadam optimiser, batch size 32, up to 20 epochs, AUC '
                         'tracked as the metric, random seed 42.'],
                        ['Learning-rate schedule',
                         'Exponential schedule starting at 0.0000001 and growing 10× every 5 epochs.'],
                        ['Early stopping',
                         'Stops when validation loss fails to improve for 2 epochs and restores the best '
                         'weights. Training stopped after epoch 18.']]}),
            ('Results',
             {'bullets': ['Sentence level: best validation AUC 0.9524 (epoch 16, lowest validation loss '
                          '0.2848), on the 3,534 held-out sentences.',
                          'Paragraph level: AUC 0.90 on the separate validation paragraphs, after averaging '
                          'sentence scores.',
                          'Training and validation curves track closely, so the model is not heavily '
                          'overfitting; validation loss starts rising after epoch 16, triggering early '
                          'stopping.'],
              'photos': [['assets/projects/text-detector/training-curves.png',
                          'Training history: train/validation AUC rise to about 0.95 while train/validation '
                          'loss fall, until validation loss turns upward near the end.']]}),
            ('Inside the code',
             {'cards': [['loading_data',
                         'Loads the four .npy embedding files, stacks them and builds the 0/1 labels.'],
                        ['sentence_length_plot',
                         'Counts non-zero token vectors per sentence and draws a histogram and boxplot.'],
                        ['model_factory / do_all',
                         'Builds and compiles the network for given layer sizes, activation, optimiser and '
                         'learning rate, then trains it and returns the best validation AUC.'],
                        ['predict_paragraphs',
                         'Runs the model on each sentence of each paragraph and averages the probabilities '
                         'into one paragraph score.'],
                        ['plot_history', 'Plots training and validation loss and AUC per epoch.']]}),
            ('Tech used',
             {'tags': ['Python',
                       'TensorFlow',
                       'Keras',
                       'scikit-learn',
                       'NumPy',
                       'pandas',
                       'Matplotlib',
                       'seaborn',
                       'Jupyter Notebook',
                       'Binary classification',
                       'ROC AUC']})]},
 {'slug': 'book-scraper',
  'title': 'Book Catalogue Scraper',
  'subtitle': 'A Python script that reads every book on a practice bookshop website and stores the details '
              'in a searchable database.',
  'meta': 'Python · requests · BeautifulSoup · pandas · SQLite · Jupyter',
  'github': 'https://github.com/uzair-shah/book-catalogue-scraper',
  'sections': [('What it does',
                ['Visits books.toscrape.com, a website built for practising web scraping, and reads its '
                 'catalogue page by page.',
                 'Pulls out the name, price, stock status, star rating and cover image link for each book.',
                 "Keeps going until a page no longer exists, so it doesn't need to know the page count in "
                 'advance.',
                 'Saves all 1,000 books to a SQLite database file (books.db) and runs a test query on it.']),
               ('What it collects',
                {'intro': 'Each book becomes one row in a table called books, with five columns:',
                 'cards': [['name', "The book's full title, taken from the link's title attribute (TEXT)."],
                           ['price',
                            'Price in pounds, with the £ sign removed and stored as a number (REAL).'],
                           ['in_stock', 'The availability text shown on the site, e.g. "In stock" (TEXT).'],
                           ['rating',
                            'Star rating converted from words ("One"…"Five") to a number 1–5 (INTEGER).'],
                           ['link',
                            "Full web address of the cover image, built from the page's relative link "
                            '(TEXT).']]})],
  'flow_title': 'How it works',
  'diagram': [('Request a page',
               'requests',
               'Builds the URL catalogue/page-N.html, starting at N = 1, and downloads it.',
               ("If the response isn't 200 (OK)",
                'Print where it stopped and leave the loop. The saved run stopped at page 51 (404).')),
              ('Find the books',
               'BeautifulSoup',
               'Parses the HTML and collects every product_pod article on the page (20 per page).',
               None),
              ('Extract and clean fields',
               'Python',
               'Reads name, price (strips £, makes it a number), stock text, rating (word to 1–5) and the '
               'full image URL.',
               None),
              ('Wait, then next page',
               'time.sleep',
               'Pauses 0.5 seconds to go easy on the site, adds 1 to N and loops back to step 1.',
               None),
              ('Build a table', 'pandas', 'Turns the list of 1,000 book records into a DataFrame.', None),
              ('Save to database',
               'SQLite',
               'Writes the DataFrame to the books table in books.db, replacing any earlier copy.',
               None),
              ('Check with SQL',
               'pandas + SQL',
               'Runs a query for books under £20, sorted by price, and prints the first five.',
               None)],
  'after': [('The data',
             {'intro': 'Figures below come straight from the saved books.db file in the repo.',
              'cards': [['1,000 books', 'Collected from 50 catalogue pages, 20 books per page.'],
                        ['£10.00 – £59.99', 'Cheapest to most expensive price; average £35.07.'],
                        ['196 under £20', 'Books matching the sample query; 42 of them have 5 stars.'],
                        ['All in stock', 'Every one of the 1,000 rows reads "In stock".']],
              'photos': [['assets/projects/book-scraper/books-by-rating.png',
                          'Ratings are spread fairly evenly: 226 one-star, 196 two-star, 203 three-star, 179 '
                          'four-star, 196 five-star.'],
                         ['assets/projects/book-scraper/price-distribution.png',
                          'Prices are spread evenly between £10 and £60, roughly 80–115 books in every £5 '
                          'band.']]}),
            ('Being polite to the website',
             ["Pauses for half a second (time.sleep(0.5)) after each page so it doesn't flood the server "
              'with requests.',
              'Stops cleanly when the site answers with anything other than success (HTTP 200). The saved '
              'notebook run ended at page 51 with a 404.']),
            ('Querying the data',
             {'intro': 'Once the data is saved, the script checks it with a real SQL query: books under £20, '
                       'cheapest first.',
              'cards': [['An Abundance of Katherines', '£10.00 · 5 stars'],
                        ['The Origin of Species', '£10.01 · 4 stars'],
                        ['The Tipping Point: How Little Things Can Make a Big Difference',
                         '£10.02 · 2 stars'],
                        ['Patience', '£10.16 · 3 stars'],
                        ['Greek Mythic History', '£10.23 · 5 stars']],
              'outro': 'SELECT * FROM books WHERE price < 20 ORDER BY price returns 196 rows; these are the '
                       'first five, matching the output saved in the notebook.'}),
            ('Inside the code',
             ['requests downloads each page; BeautifulSoup finds every <article class="product_pod"> block, '
              'one per book.',
              'A small lookup table turns the rating CSS class (e.g. "Three") into a number; anything '
              'unknown becomes 0.',
              'urljoin turns relative image paths into full URLs that work outside the site.',
              'Rows go into a pandas DataFrame, then df.to_sql writes it to SQLite, replacing the table on '
              'every run.',
              'The Jupyter notebook shows the work step by step: one book first, then one page, then the '
              'full loop.']),
            ('Tech used',
             {'tags': ['Python',
                       'requests',
                       'BeautifulSoup',
                       'pandas',
                       'SQLite',
                       'SQL',
                       'Jupyter Notebook',
                       'Web scraping']})]}]

# Projects. Each: title, one-line description, tags, link.
PROJECTS = [
    {
        "title": "Document Q&A with AI (RAG)",
        "text": "Answers questions about a research paper using only the paper itself, with an "
                "evaluation set that checks correct answers and correct refusals. Compares Gemini "
                "with a locally run DeepSeek model.",
        "tags": ["Python", "LLMs", "ChromaDB", "Docker"],
        "url": "https://github.com/uzair-shah/rag-app",
        "page": "projects/rag-app.html",
    },
    {
        "title": "Modelling logistics hubs",
        "text": "Master's research: modelled a hub-and-spoke truck network as a Markov chain and "
                "simulated cost and revenue. A second unloading bay paid off; a third barely did.",
        "tags": ["MATLAB", "Markov chains", "Simulation"],
        "url": "https://github.com/uzair-shah/logistics-hub-juggling-model",
        "page": "projects/logistics-research.html",
    },
    {
        "title": "AI vs human text detector",
        "text": "Neural network that flags AI-written text, benchmarked against SVM baselines. "
                "About 0.95 validation AUC per sentence and 0.90 per paragraph on Kaggle.",
        "tags": ["TensorFlow", "scikit-learn", "Kaggle"],
        "url": "https://github.com/uzair-shah/ai-vs-human-text-classifier",
        "page": "projects/text-detector.html",
    },
    {
        "title": "Book catalogue scraper",
        "text": "Scraped about 1,000 books across 50 pages with polite rate limiting, stored them "
                "in a SQL database and queried the results.",
        "tags": ["Python", "BeautifulSoup", "SQL"],
        "url": "https://github.com/uzair-shah/book-catalogue-scraper",
        "page": "projects/book-scraper.html",
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
