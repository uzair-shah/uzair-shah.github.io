"""Builds index.html from content.py. No extra packages needed.

    python3 build.py           # rebuild index.html
    python3 build.py --serve   # rebuild, then preview at http://localhost:8000
"""

import html
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import content as c  # noqa: E402
e = html.escape


ICONS = {
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
    "github": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .3a12 12 0 0 0-3.8 23.38c.6.12.83-.26.83-.57v-2.03c-3.34.73-4.04-1.6-4.04-1.6-.55-1.4-1.34-1.77-1.34-1.77-1.08-.74.09-.73.09-.73 1.2.09 1.83 1.24 1.83 1.24 1.07 1.83 2.8 1.3 3.49 1 .1-.78.42-1.3.76-1.6-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.12-3.18 0 0 1-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.3-1.55 3.3-1.23 3.3-1.23.66 1.66.25 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.61-2.8 5.62-5.48 5.92.43.37.82 1.1.82 2.22v3.29c0 .32.22.69.83.57A12 12 0 0 0 12 .3"/></svg>',
    "email": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M3 5h18v14H3z M3 6l9 7 9-7"/></svg>',
}


def contact_links() -> str:
    links = []
    if c.LINKEDIN:
        links.append(f'<a href="{e(c.LINKEDIN)}" target="_blank" rel="noopener">{ICONS["linkedin"]}LinkedIn</a>')
    if c.GITHUB:
        links.append(f'<a href="{e(c.GITHUB)}" target="_blank" rel="noopener">{ICONS["github"]}GitHub</a>')
    if c.EMAIL:
        links.append(f'<a href="mailto:{e(c.EMAIL)}">{ICONS["email"]}{e(c.EMAIL)}</a>')
    return "\n        ".join(links)


def photo() -> str:
    if not getattr(c, "PHOTO", ""):
        return ""
    return f'<img class="photo" src="{e(c.PHOTO)}" alt="Photo of {e(c.NAME)}" width="320" height="320">'


def pillars() -> str:
    return "\n".join(
        f'      <div class="pillar"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in c.PILLARS
    )


def highlights() -> str:
    rows = []
    for h in c.HIGHLIGHTS:
        t, d = h[0], h[1]
        link = f' <a class="more" href="{e(h[2])}">Read the case study &rarr;</a>' if len(h) > 2 and h[2] else ""
        rows.append(f'        <li><strong>{e(t)}</strong><span>{e(d)}{link}</span></li>')
    return "\n".join(rows)


def case_cards() -> str:
    cards = []
    for cs in getattr(c, "CASE_STUDIES", []):
        cards.append(
            f'''      <a class="card case" href="case-studies/{e(cs["slug"])}.html">
        <p class="case-meta">{e(cs["meta"])}</p>
        <h3>{e(cs["title"])}</h3>
        <p>{e(cs["subtitle"])}</p>
        <span class="more">Read the case study &rarr;</span>
      </a>'''
        )
    return "\n".join(cards)


def projects() -> str:
    cards = []
    for p in c.PROJECTS:
        tags = "".join(f"<span>{e(t)}</span>" for t in p.get("tags", []))
        cards.append(
            f'''      <a class="card" href="{e(p["url"])}" target="_blank" rel="noopener">
        <h3>{e(p["title"])} <span class="arrow">&#8599;</span></h3>
        <p>{e(p["text"])}</p>
        <div class="tags">{tags}</div>
      </a>'''
        )
    return "\n".join(cards)


STYLE = """  :root {{
    --bg: #fbfbfa; --fg: #16171a; --muted: #5f6370; --line: #e6e6e3; --card: #ffffff;
    --accent: {accent};
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: #111214; --fg: #ececec; --muted: #9a9ea8; --line: #24262b; --card: #17181b; }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--fg);
    font: 16px/1.65 Inter, system-ui, -apple-system, "Segoe UI", sans-serif;
    -webkit-font-smoothing: antialiased;
  }}
  .wrap {{ max-width: 760px; margin: 0 auto; padding: 0 20px; }}
  nav {{ display: flex; justify-content: space-between; align-items: center; padding: 28px 0; }}
  nav .brand {{ font-weight: 600; letter-spacing: -0.01em; }}
  nav .links a {{ margin-left: 20px; }}
  a {{ color: inherit; text-decoration: none; }}
  nav .links a, footer a, .contact a {{ color: var(--muted); transition: color .15s; }}
  nav .links a:hover, footer a:hover, .contact a:hover {{ color: var(--accent); }}
  header {{ padding: 48px 0 40px; display: grid; grid-template-columns: 1fr 180px; gap: 40px; align-items: center; }}
  .photo {{ width: 180px; height: 180px; border-radius: 50%; object-fit: cover; border: 1px solid var(--line); }}
  .eyebrow {{ color: var(--accent); font-weight: 500; font-size: 14px; margin: 0 0 12px; }}
  h1 {{ font-size: clamp(32px, 6vw, 46px); line-height: 1.12; letter-spacing: -0.025em; margin: 0 0 20px; font-weight: 600; }}
  .intro {{ color: var(--muted); font-size: 18px; max-width: 620px; margin: 0 0 28px; }}
  .contact {{ display: flex; gap: 22px; flex-wrap: wrap; font-weight: 500; }}
  .contact a {{ display: inline-flex; align-items: center; gap: 7px; }}
  .contact svg {{ width: 16px; height: 16px; flex: none; }}
  h1 .headline {{ display: block; font-size: 0.62em; font-weight: 500; color: var(--muted); letter-spacing: -0.015em; margin-top: 10px; }}
  section {{ padding: 44px 0; border-top: 1px solid var(--line); }}
  h2 {{ font-size: 13px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 500; margin: 0 0 24px; }}
  .pillars {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
  .pillar h3 {{ margin: 0 0 6px; font-size: 17px; font-weight: 600; }}
  .pillar p {{ margin: 0; color: var(--muted); font-size: 15px; }}
  .role h3 {{ margin: 0; font-size: 19px; font-weight: 600; }}
  .role .meta {{ color: var(--muted); font-size: 14px; margin: 2px 0 18px; }}
  .highlights {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 14px; }}
  .highlights li {{ display: grid; grid-template-columns: 170px 1fr; gap: 16px; }}
  .highlights strong {{ font-weight: 600; }}
  .highlights span {{ color: var(--muted); }}
  .cards {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }}
  .card {{
    display: block; padding: 22px; border: 1px solid var(--line); border-radius: 14px;
    background: var(--card); transition: transform .15s, border-color .15s;
  }}
  .card:hover {{ transform: translateY(-2px); border-color: var(--accent); }}
  .card h3 {{ margin: 0 0 8px; font-size: 17px; font-weight: 600; }}
  .card .arrow {{ color: var(--accent); }}
  .card p {{ margin: 0 0 14px; color: var(--muted); font-size: 15px; }}
  .tags {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .tags span {{ font-size: 12px; padding: 3px 9px; border-radius: 999px; border: 1px solid var(--line); color: var(--muted); }}
  footer {{ padding: 40px 0 56px; border-top: 1px solid var(--line); color: var(--muted); font-size: 14px;
           display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px; }}
  footer .contact {{ gap: 18px; }}
  @media (max-width: 640px) {{
    .pillars, .cards {{ grid-template-columns: 1fr; }}
    .highlights li {{ grid-template-columns: 1fr; gap: 2px; }}
    nav .links a {{ margin-left: 14px; }}
    header {{ padding-top: 28px; grid-template-columns: 1fr; gap: 24px; }}
    header .photo {{ order: -1; width: 120px; height: 120px; }}
  }}
  .cards.one {{ grid-template-columns: 1fr; }}
  .card .more {{ color: var(--accent); font-weight: 500; font-size: 15px; }}
  .case-meta {{ font-size: 13px !important; margin: 0 0 6px !important; }}
  .highlights .more {{ color: var(--accent); font-weight: 500; white-space: nowrap; }}
  .back {{ color: var(--muted); font-size: 14px; }}
  .back:hover {{ color: var(--accent); }}
  .cs-head {{ padding: 40px 0 36px; }}
  .cs-head h1 {{ margin-bottom: 14px; }}
  .cs-sub {{ color: var(--muted); font-size: 19px; margin: 0 0 10px; max-width: 640px; }}
  .cs-meta {{ color: var(--muted); font-size: 14px; margin: 0; }}
  .cs ul {{ margin: 0; padding-left: 20px; display: grid; gap: 8px; }}
  .cs p {{ margin: 0; }}
  .flow {{ display: flex; align-items: stretch; gap: 0; flex-wrap: wrap; margin: 0 0 16px; }}
  .step {{ flex: 1 1 120px; padding: 14px 16px; border: 1px solid var(--line); border-radius: 12px; background: var(--card); }}
  .step b {{ display: block; font-weight: 600; }}
  .step small {{ color: var(--muted); font-size: 13px; }}
  .arrow-step {{ display: flex; align-items: center; padding: 0 8px; color: var(--accent); font-size: 18px; }}
  .flow-note {{ color: var(--muted); font-size: 15px; }}
  .decisions {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }}
  .decision {{ padding: 18px; border: 1px solid var(--line); border-radius: 12px; background: var(--card); }}
  .decision h3 {{ margin: 0 0 6px; font-size: 16px; font-weight: 600; }}
  .decision p {{ color: var(--muted); font-size: 15px; }}
  .note {{ color: var(--muted); font-size: 15px; font-style: italic; }}
  @media (max-width: 640px) {{
    .decisions {{ grid-template-columns: 1fr; }}
    .flow {{ flex-direction: column; }}
    .step {{ flex: none; }}
    .arrow-step {{ justify-content: center; padding: 4px 0; transform: rotate(90deg); }}
  }}
"""


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}</title>
<meta name="description" content="{headline}. {location}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
{style}
</style>
</head>
<body>
<div class="wrap">
  <nav>
    <a class="brand" href="#">{short}</a>
    <div class="links"><a href="#work">Work</a><a href="#case-studies">Case studies</a><a href="#projects">Projects</a></div>
  </nav>

  <header>
    <div>
    <p class="eyebrow">{location}</p>
    <h1>{name}<span class="headline">{headline}</span></h1>
    <p class="intro">{intro}</p>
    <div class="contact">
        {contact}
    </div>
    </div>
    {photo}
  </header>

  <section>
    <h2>What I bring</h2>
    <div class="pillars">
{pillars}
    </div>
  </section>

  <section id="work">
    <h2>Experience</h2>
    <div class="role">
      <h3>{exp_title}</h3>
      <p class="meta">{exp_meta}</p>
      <ul class="highlights">
{highlights}
      </ul>
    </div>
  </section>

  <section id="case-studies">
    <h2>Case studies</h2>
    <div class="cards one">
{case_cards}
    </div>
  </section>

  <section id="projects">
    <h2>Projects</h2>
    <div class="cards">
{projects}
    </div>
  </section>


  <footer>
    <span>&copy; {name}</span>
  </footer>
</div>
</body>
</html>
"""


CASE_PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {name}</title>
<meta name="description" content="{subtitle}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
{style}
</style>
</head>
<body>
<div class="wrap cs">
  <nav>
    <a class="brand" href="../index.html">{short}</a>
    <div class="links"><a class="back" href="../index.html">&larr; Back to home</a></div>
  </nav>

  <div class="cs-head">
    <p class="eyebrow">Case study</p>
    <h1>{title}</h1>
    <p class="cs-sub">{subtitle}</p>
    <p class="cs-meta">{meta}</p>
  </div>
{sections}
  <section>
    <h2>{flow_title}</h2>
    <div class="flow">
{flow}
    </div>
    <p class="flow-note">{flow_note}</p>
  </section>

  <section>
    <h2>{decisions_title}</h2>
    <div class="decisions">
{decisions}
    </div>
  </section>

  <section>
    <h2>{scope_title}</h2>
    <p>{scope}</p>
  </section>

  <section>
    <h2>{outcome_title}</h2>
    <p>{outcome}</p>
  </section>

  <footer>
    <span>&copy; {name}</span>
    <div class="contact">
        {contact}
    </div>
  </footer>
</div>
</body>
</html>
"""


def build_case_studies(css: str) -> None:
    out_dir = HERE / "case-studies"
    out_dir.mkdir(exist_ok=True)
    for cs in getattr(c, "CASE_STUDIES", []):
        sections = []
        for title, items in cs.get("sections", []):
            lis = "".join(f"<li>{e(i)}</li>" for i in items)
            sections.append(f"  <section>\n    <h2>{e(title)}</h2>\n    <ul>{lis}</ul>\n  </section>")
        steps = []
        for i, (label, who) in enumerate(cs.get("flow", [])):
            if i:
                steps.append('      <div class="arrow-step">&rarr;</div>')
            steps.append(f'      <div class="step"><b>{e(label)}</b><small>{e(who)}</small></div>')
        decisions = "\n".join(
            f'      <div class="decision"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in cs.get("decisions", [])
        )
        page = CASE_PAGE.format(
            style=css, name=e(c.NAME), short=e(c.SHORT_NAME), title=e(cs["title"]),
            subtitle=e(cs["subtitle"]), meta=e(cs["meta"]), sections="\n".join(sections),
            flow_title=e(cs["flow_title"]), flow="\n".join(steps), flow_note=e(cs["flow_note"]),
            decisions_title=e(cs["decisions_title"]), decisions=decisions,
            scope_title=e(cs["scope_title"]), scope=e(cs["scope"]),
            outcome_title=e(cs["outcome_title"]), outcome=e(cs["outcome"]),
            contact=contact_links(),
        )
        path = out_dir / f"{cs['slug']}.html"
        path.write_text(page, encoding="utf-8")
        print(f"Built {path}")


def build() -> Path:
    css = STYLE.format(accent=e(c.ACCENT))
    out = PAGE.format(
        style=css, case_cards=case_cards(),
        name=e(c.NAME), short=e(c.SHORT_NAME), headline=e(c.HEADLINE), location=e(c.LOCATION),
        intro=e(c.INTRO), contact=contact_links(), pillars=pillars(), exp_title=e(c.EXPERIENCE_TITLE),
        exp_meta=e(c.EXPERIENCE_META), highlights=highlights(), projects=projects(), accent=e(c.ACCENT),
        photo=photo(),
    )
    path = HERE / "index.html"
    path.write_text(out, encoding="utf-8")
    print(f"Built {path}")
    build_case_studies(css)
    return path


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(HERE))
        print("Preview at http://localhost:8000  (Ctrl+C to stop)")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
