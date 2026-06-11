# Porfolio.py - Versión corregida
import reflex as rx
from Porfolio.pages import home

app = rx.App(
    style={
        "font_family": "Inter, sans-serif",
        "background_color": "var(--gray-1)",
    }
)

app.add_page(home.home, route="/", title="Portfolio 3D")