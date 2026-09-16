# Project Title

<!-- TODO: what this demo / project page shows and which paper it accompanies. -->

Static demo / project page. Source lives in `pages/`, and the build output goes to `_site/` (git-ignored).

## Local preview

```sh
python3 scripts/build_site.py
python3 -m http.server --directory _site 8000
# open http://localhost:8000
```

## Build and deploy

- **CI (`.github/workflows/site.yml`)** builds the site on every push and pull request, and uploads `_site/` as a workflow artifact.
- **Deploy is off by default.** The lab website lives at [jasprlab.com](https://jasprlab.com), outside GitHub. Choose one:
  - **Hand off to jasprlab.com:** download the `site` artifact from the CI run and publish it through the lab website's process. TODO: document that process here.
  - **GitHub Pages for this repo:** only works for **public** repos on GitHub Free. Enable Pages (Settings → Pages → Source: GitHub Actions), then set the repository variable `DEPLOY_PAGES=true` (Settings → Secrets and variables → Actions → Variables).

If you use a site generator (Jekyll, Hugo, Astro, etc.), replace `scripts/build_site.py` and the build step in `site.yml`. Keep the output in `_site/`.

## Layout

| Path | Contents |
|---|---|
| `pages/` | Site source (HTML/CSS/JS/assets) |
| `scripts/build_site.py` | Build: copies `pages/` → `_site/` |
| `configs/` | Optional site config |
| `docs/` | Notes |

## License

MIT (see [LICENSE](LICENSE)). Check that images, videos, and datasets shown on the page may be redistributed.
