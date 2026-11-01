# Personal website

A one-page site introducing Syed Uzair Shah Bukhari and linking to his projects.
Built with plain Python (no packages to install) and hosted on GitHub Pages.

## Change the text

1. Open `content.py` and edit anything: intro, highlights, projects, links, colour.
2. Rebuild the page:

   ```bash
   python3 build.py
   ```

3. Preview it in your browser at http://localhost:8000:

   ```bash
   python3 build.py --serve
   ```

## Publish changes

```bash
git add -A && git commit -m "Update site" && git push
```

GitHub Pages updates the live site about a minute after each push.

## Add a project

Copy one of the blocks in `PROJECTS` inside `content.py`, change the title, text, tags and link, then rebuild.
