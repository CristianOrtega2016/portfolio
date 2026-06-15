# Porfolio.py - App configuration and routing
import reflex as rx
from Porfolio.pages.home import home
from Porfolio.pages.cv import cv_page

app = rx.App(
    style={
        "font_family": "Inter, sans-serif",
        "background_color": "var(--gray-1)",
    }
)

app.add_page(home, route="/", title="Portfolio")
app.add_page(cv_page, route="/cv", title="CV- Portfolio")