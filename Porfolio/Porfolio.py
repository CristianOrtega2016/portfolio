# Porfolio.py - App configuration and routing
import reflex as rx
from Porfolio.pages import home, cv

app = rx.App(
    style={
        "font_family": "Inter, sans-serif",
        "background_color": "var(--gray-1)",
    }
)

app.add_page(home.home, route="/", title="Portfolio 3D")
app.add_page(cv.cv, route="/cv", title="CV - Portfolio 3D")