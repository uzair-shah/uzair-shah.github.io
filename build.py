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


def contact_links() -> str:
    links = []
    if c.LINKEDIN:
        links.append(f'<a href="{e(c.LINKEDIN)}" target="_blank" rel="noopener">LinkedIn</a>')
    if c.GITHUB:
        links.append(f'<a href="{e(c.GITHUB)}" target="_blank" rel="noopener">GitHub</a>')
    if c.EMAIL:
        links.append(f'<a href="mailto:{e(c.EMAIL)}">Email</a>')
    return "\n        ".join(links)


def contact_details() -> str:
    rows = []
    if c.EMAIL:
        rows.append(f'<a class="detail" href="mailto:{e(c.EMAIL)}"><span>Email</span>{e(c.EMAIL)}</a>')
    if c.LINKEDIN:
        shown = c.LINKEDIN.replace("https://", "").replace("www.", "").rstrip("/")
        rows.append(f'<a class="detail" href="{e(c.LINKEDIN)}" target="_blank" rel="noopener"><span>LinkedIn</span>{e(shown)}</a>')
    if c.GITHUB:
        shown = c.GITHUB.replace("https://", "").rstrip("/")
        rows.append(f'<a class="detail" href="{e(c.GITHUB)}" target="_blank" rel="noopener"><span>GitHub</span>{e(shown)}</a>')
    return "\n      ".join(rows)


def photo() -> str:
    if not getattr(c, "PHOTO", ""):
        return ""
    return f'<img class="photo" src="{e(c.PHOTO)}" alt="Photo of {e(c.NAME)}" width="320" height="320">'


def pillars() -> str:
    return "\n".join(
        f'      <div class="pillar"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in c.PILLARS
    )


def highlights() -> str:
    return "\n".join(
        f'        <li><strong>{e(t)}</strong><span>{e(d)}</span></li>' for t, d in c.HIGHLIGHTS
    )


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
  :root {{
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
  #contact {{ scroll-margin-top: 24px; }}
  .contact-lead {{ color: var(--muted); max-width: 560px; margin: 0 0 22px; }}
  .details {{ display: grid; gap: 10px; max-width: 520px; }}
  .detail {{ display: flex; justify-content: space-between; gap: 16px; padding: 14px 18px; border: 1px solid var(--line);
            border-radius: 12px; background: var(--card); font-weight: 500; transition: border-color .15s; word-break: break-all; }}
  .detail span {{ color: var(--muted); font-weight: 400; word-break: normal; }}
  .detail:hover {{ border-color: var(--accent); color: var(--accent); }}
  .eyebrow {{ color: var(--accent); font-weight: 500; font-size: 14px; margin: 0 0 12px; }}
  h1 {{ font-size: clamp(32px, 6vw, 46px); line-height: 1.12; letter-spacing: -0.025em; margin: 0 0 20px; font-weight: 600; }}
  .intro {{ color: var(--muted); font-size: 18px; max-width: 620px; margin: 0 0 28px; }}
  .contact {{ display: flex; gap: 22px; flex-wrap: wrap; font-weight: 500; }}
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
    .detail {{ flex-direction: column; gap: 2px; }}
  }}
</style>
</head>
<body>
<div class="wrap">
  <nav>
    <a class="brand" href="#">{short}</a>
    <div class="links"><a href="#work">Work</a><a href="#projects">Projects</a><a href="#contact">Contact</a></div>
  </nav>

  <header>
    <div>
    <p class="eyebrow">{location}</p>
    <h1>{name}<br>{headline}.</h1>
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

  <section id="projects">
    <h2>Projects</h2>
    <div class="cards">
{projects}
    </div>
  </section>

  <section id="contact">
    <h2>Contact</h2>
    <p class="contact-lead">{contact_text}</p>
    <div class="details">
      {details}
    </div>
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


def build() -> Path:
    out = PAGE.format(
        name=e(c.NAME), short=e(c.SHORT_NAME), headline=e(c.HEADLINE), location=e(c.LOCATION),
        intro=e(c.INTRO), contact=contact_links(), pillars=pillars(), exp_title=e(c.EXPERIENCE_TITLE),
        exp_meta=e(c.EXPERIENCE_META), highlights=highlights(), projects=projects(), accent=e(c.ACCENT),
        photo=photo(), details=contact_details(), contact_text=e(getattr(c, "CONTACT_TEXT", "")),
    )
    path = HERE / "index.html"
    path.write_text(out, encoding="utf-8")
    print(f"Built {path}")
    return path


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server

        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(HERE))
        print("Preview at http://localhost:8000  (Ctrl+C to stop)")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
