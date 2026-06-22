# Porfolio.py - App configuration and routing
import reflex as rx
from Porfolio.pages.home import home
from Porfolio.pages.cv import cv_page
from Porfolio.pages.about import about
from Porfolio.pages.diploms import diploms
from Porfolio.pages.diplom_view import diplom_page
from Porfolio.pages.projects import projects

app = rx.App(
    style={
        "font_family": "Inter, sans-serif",
        "background_color": "var(--gray-1)",
    }
)

app.add_page(home, route="/", title="portfolio")
app.add_page(cv_page, route="/cv", title="curriculum")
app.add_page(about, route="/about", title="about me")
app.add_page(diploms, route="/diploms", title="diploms")
app.add_page(diplom_page, route="/pdfview/[file_name]", title="diplom detail")
app.add_page(projects, route="/projects", title="projects")