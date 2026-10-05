# Portfolio — Cristian Ortega

Personal portfolio and CV web app built with [Reflex](https://reflex.dev/)
(Python on the backend, React on the frontend — no JavaScript written by hand).

**Live:** https://deploy-reflex-portfolio-blue-star.reflex.run

## What it is

A single Reflex app with several routes, all sharing one navbar (desktop links /
mobile hamburger menu) and footer:

| Route | Page | Content |
|---|---|---|
| `/` | Home | Intro text + auto-rotating card carousel |
| `/cv` | Curriculum | Full-screen embedded PDF viewer (`assets/pdfs/cv_7.pdf`) |
| `/about` | About me | Profile, presentation, skills, contact access |
| `/diploms` | Diplomas | Responsive grid of diploma cards (image → PDF) |
| `/pdfview/[file_name]` | Diploma viewer | Full-screen PDF viewer for a given diploma |
| `/projects` | Projects | Responsive grid of project cards linking to repos / live apps |

Key UI pieces:

- **Rotating display** — a CSS `translateX` carousel over 6 cards
  (Resume, Skills, Experience, Contact, Projects, Education). Autoplay is driven
  by a Reflex background task (`RotatingDisplayState.run_loop`, `asyncio.sleep(3s)`),
  with prev/next/dot navigation.
- **Contact dialog** — modal built from `rx.dialog` + `rx.data_list`, toggled
  globally via `ContactCardState`.
- **Projects / diplomas grids** — reusable card components rendered in a
  breakpoint-aware `rx.grid` (1 / 2 / 3 columns).
- **Mobile dropdown menu** — the desktop nav collapses into a hamburger
  `rx.menu` under the mobile/tablet breakpoints.

## Architecture

- **Framework:** [Reflex](https://reflex.dev/) `>= 0.9.4` (`reflex_components_radix`
  for the Radix Themes UI kit).
- **Theme:** dark, forced on every device via
  `RadixThemesPlugin(theme=rx.theme(color_mode="dark"))` in `rxconfig.py`.
- **State:** Reflex state classes — `RotatingDisplayState` (carousel index +
  autoplay loop), `ContactCardState` (dialog open/close), `DropdownMenuState`
  (menu open tracking). No database; all data is static/declarative.
- **Assets:** served from `assets/` (profile photo, project screenshots,
  diploma preview PNGs, diploma + CV PDFs).
- **Deployment:** [Reflex Cloud](https://cloud.reflex.dev/) (`reflex deploy`),
  region `arn` (Stockholm).

## Project structure

```
portfolio/
├── main.py                       # Entry point (runs the app)
├── rxconfig.py                   # Reflex config + Radix theme plugin
├── pyproject.toml                # Dependencies (uv)
├── assets/
│   ├── profile/                  # Profile picture
│   ├── pictures/                 # Project screenshots used by the projects grid
│   ├── diploms_pictures/         # Diploma preview images
│   ├── diploms/                  # Diploma PDFs
│   └── pdfs/                     # CV PDF
└── Porfolio/                     # App package (folder name is legacy, kept as-is)
    ├── Porfolio.py               # rx.App setup, routes, theme
    ├── components/
    │   ├── navbar.py             # Desktop links + mobile menu item helpers
    │   ├── footer.py             # Footer with social links
    │   ├── rotating_display.py   # Carousel component + RotatingDisplayState
    │   ├── projects_grid.py      # Projects grid/cards
    │   ├── diploms_grid.py       # Diplomas grid/cards
    │   ├── contact_dialog.py     # Contact modal + navbar button
    │   └── dropdown_menu.py      # Legacy dropdown helper (currently unused)
    ├── pages/
    │   ├── home.py               # "/"     — intro + rotating carousel
    │   ├── cv.py                 # "/cv"   — embedded CV PDF
    │   ├── about.py              # "/about"
    │   ├── diploms.py            # "/diploms"
    │   ├── diplom_view.py        # "/pdfview/[file_name]"
    │   └── projects.py           # "/projects"
    └── states/
        ├── contact_card_state.py # ContactCardState
        └── dropdown_state.py     # DropdownMenuState
```

## Run locally

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
reflex run          # http://localhost:3000
```

## Deploy

```bash
reflex deploy --app-id cef9b688-42b1-428f-a1a8-29dfe2d2a4dc --region arn --no-interactive
```

## Notes

- The app is intentionally pinned to the dark theme so phones (usually in light
  mode) match the desktop look.
- Interactive elements use `rx.color(...)` tokens rather than hardcoded colors,
  so they stay readable in either theme.
