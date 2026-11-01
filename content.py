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
    ("Supplier payments", "Brought about USD 350K of untracked supplier payments under a simple "
                          "request-and-approval workflow between Commercial and Finance."),
    ("Inventory visibility", "Set up data pipelines and a real-time inventory dashboard that cut "
                             "out-of-stock SKUs by 5%."),
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

# Contact links shown at the top and bottom. Leave a value as "" to hide it.
EMAIL = "s.uzair.shah01@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/syed-uzair-shah-bukhari/"
GITHUB = "https://github.com/uzair-shah"

# Main accent colour (any CSS colour).
ACCENT = "#2f6fed"
