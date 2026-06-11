# Portfolio 3D

A 3D interactive portfolio built with [Reflex](https://reflex.dev/).

## Features

- Interactive 3D cube with draggable rotation
- Multi-face cube displaying CV, Skills, Experience, Contact, Projects, and Education
- Responsive design

## Setup

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (fast Python package manager)

### Install

```bash
# Clone the repository
git clone <repo-url>
cd portfolio

# Install dependencies
uv sync

# Run the app
reflex run
```

The app will be available at `http://localhost:3000`.

## Development

```bash
# Export static frontend (for deployment)
reflex export --frontend-only

# Run with debug mode
reflex run --loglevel debug
```

## Project Structure

```
portfolio/
├── assets/                  # Static assets (favicon, etc.)
├── Porfolio/
│   ├── components/          # Reusable UI components
│   │   ├── cube_3d_advanced.py    # 3D interactive cube
│   │   ├── dropdown_menu.py       # Navigation dropdown menu
│   │   └── __init__.py
│   ├── pages/               # App pages
│   │   ├── home.py          # Home page with the 3D cube
│   │   ├── cv.py            # CV / Resume page
│   │   └── __init__.py
│   ├── states/              # Reflex app states
│   │   ├── cube_3d_advanced_state.py
│   │   ├── dropdown_state.py
│   │   └── __init__.py
│   ├── Porfolio.py          # App configuration and routing
│   └── __init__.py
├── main.py                  # Entry point
├── pyproject.toml           # Python project config
├── rxconfig.py              # Reflex configuration
└── README.md
```
