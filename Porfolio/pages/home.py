"""Home page — auto-rotating portfolio cards."""

from __future__ import annotations

import reflex as rx
from Porfolio.components.dropdown_menu import dropdown_menu
from Porfolio.components.rotating_display import rotating_display
from Porfolio.components.navbar import navbar_icons_item, navbar_icons_menu_item
from Porfolio.components.contact_dialog import contact_nav_button, contact_dialog
from Porfolio.states.contact_card_state import ContactCardState
from Porfolio.components.footer import footer


def _cv_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Curriculum", size="5"),
            rx.image(src="/pictures/linkedin_profile.png", width="150px", border_radius= "20%",),         
            rx.link("Look my LinkedIn", href="https://www.linkedin.com/in/cristian-ortega-aab1523b5/", is_external=True, font_size="sm"),
            rx.button(
                "CV",
                on_click=lambda: rx.redirect("/cv"),
                color_scheme="blue",
            ),
            spacing="2",
            align="center",
        ),
        padding="10px",
        height="100%",
        width="100%",
    )


def _skills_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Skills", size="5"),
            rx.badge("Python", color_scheme="green"),
            rx.badge("Reflex", color_scheme="blue"),
            rx.badge("React", color_scheme="cyan"),
            rx.badge("JavaScript", color_scheme="yellow"),
            rx.badge("Docker", color_scheme="orange"),
            rx.badge("PostgreSQL", color_scheme="violet"),
            spacing="2",
            align="center",
        ),
        padding="20px",
        height="100%",
        width="100%",
    )


def _experience_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Experience", size="5"),
            rx.text("🧑‍💻 5 years in web development"),
            rx.text("🐍 3 years with Python"),
            rx.text("⚛️ 2 years with  Reflex"),
            rx.text("🏗️ 2 years with  React"),
            spacing="3",
            align="center",
        ),
        padding="20px",
        height="100%",
        width="100%",
    )


def _contact_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Contact", size="5"),
            rx.link("🐙 GitHub", href="https://github.com/CristianOrtega2016", is_external=True),
            rx.link("💼 LinkedIn", href="https://linkedin.com", is_external=True),
            rx.link("🐦 Twitter", href="https://twitter.com", is_external=True),
            spacing="3",
            align="start",
        ),
        padding="20px",
        height="100%",
        width="100%",
    )


def _projects_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Projects", size="5"),
            rx.text("🎯 Portfolio 3D"),
            rx.text("📋 DApp Token"),
            rx.text("📊 Video transcriber"),
            rx.text("🛒 E-commerce"),
            spacing="3",
            align="center",
        ),
        padding="20px",
        height="100%",
        width="100%",
    )


def _education_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Education", size="5"),
            rx.text("🎓 Course of Blockchain development"),
            rx.text("📚 Courses of advanced Python"),
            rx.text("🎯 Knowledge in Reflex"),
            rx.text("🏅 Full Stack Development"),
            spacing="3",
            align="center",
        ),
        padding="20px",
        height="100%",
        width="100%",
    )

CARDS = {
    "cv": {
        "label": "📄 Resume",
        "component": _cv_card,
    },
    "skills": {
        "label": "🛠️ Skills",
        "component": _skills_card,
    },
    "experience": {
        "label": "💼 Experience",
        "component": _experience_card,
    },
    "contact": {
        "label": "📬 Contact",
        "component": _contact_card,
    },
    "projects": {
        "label": "🚀 Project",
        "component": _projects_card,
    },
    "education": {
        "label": "📖 Education",
        "component": _education_card,
    },
}

_cards  = [item["component"]() for item in CARDS.values()]
_labels = [item["label"] for item in CARDS.values()]

def navbar_home() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        tag="briefcase-business", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="white"          # Color adaptable con CSS
                    ),
                    rx.heading("My Portfolio", size="7", weight="bold", color="white",),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Diploms", "file-stack", "/diploms"),
                    navbar_icons_item("Projects", "folders", "/projects"),
                    navbar_icons_item("About me", "user-round", "/about"),                    
                    navbar_icons_item("Curriculum", "book-text", "/cv"),
                    contact_nav_button(),
                    spacing="6",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        tag="briefcase-business", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="white"          # Color adaptable con CSS
                    ),
                    rx.heading("My Portfolio", size="7", weight="bold", color="white",),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        navbar_icons_menu_item("Diploms", "file-stack", "/diploms"),
                        navbar_icons_menu_item("Projects", "folder", "/projects"),  
                        navbar_icons_menu_item("About me", "user-round", "/about"),                      
                        navbar_icons_menu_item("Curriculum", "book-text", "/CV"),
                        contact_nav_button(size="3"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("iris", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )


def home() -> rx.Component:
    """Render the home page with header, auto-rotating cards, and footer."""
    return rx.vstack(
        # ── Header ──
        navbar_home(),
        rx.divider(width="100%"),
        # ── Body: rotating display centered ──
        rx.box(
            rx.desktop_only(
                rx.flex(
                    rx.box(
                        rx.scroll_area(
                            rx.heading("Presentation", size="5"),
                            rx.image(src="/profile/profilbild.JPG", width="80px", border_radius= "20%"),
                            rx.text(
                                "Hello, my name is Cristian Ortega! I am a Certified Public Accountant and Auditor from Chile, and some time ago I had the opportunity to work as a Credit Card Analyst at Citibank. In this role, I was responsible for monitoring eight bridge accounts where credits issued to customers due to transaction disputes were recorded. These included duplicate payments, services not received, fraud cases, stolen cards, among others. My responsibility was to ensure that each customer case was resolved within a maximum period of three months, including the corresponding accounting process.",
                                margin_top="0.5em",
                                font_size="sm",
                            ),
                        ),
                        background="linear-gradient(45deg, var(--green-9), var(--plum-9))",
                        width="25%",
                        max_width="350px",
                        min_width="200px",
                        max_height="450px",
                        height="100%",
                        padding="1em",
                        justify="center",
                        align="center",
                        direction="column",
                        border="solid",
                        border_color="white",
                        flex_grow="1",
                    ),
                    rotating_display(
                        cards=_cards,
                        labels=_labels,
                        auto_rotate=True,
                        card_width="600px",
                        card_height="500px",
                    ),
                    rx.box(
                        rx.scroll_area(
                            rx.text(
                                "In addition, I have studied accounting and programming in Sweden, which allows me to have a modern and comprehensive perspective on business and financial processes. My areas of expertise include accounting and auditing, proficiency in Office tools, and specialized software such as AS400 and WinRunner. I also have programming skills in Java, Spring Data, JavaScript, React, TypeScript, and Python. Currently, I am learning Smart Contracts using Solidity and Artificial Intelligence (AI Agents). My main goal is to continue learning everything related to AI and apply it to accounting, data analys, and software development.",
                                margin_top="0.5em",
                                font_size="sm",
                            ),
                        ),
                        background="linear-gradient(45deg, var(--blue-9), var(--plum-9))",
                        width="25%",
                        max_width="350px",
                        min_width="200px",
                        max_height="450px",
                        height="100%",
                        padding="1em",
                        justify="start",
                        align="start",
                        direction="column",
                        border="solid",
                        border_color="white",
                        flex_grow="1",
                    ),
                    justify="center",
                    align="center",
                    width="100%",
                    height="100%",
                    gap="1em",
                ),
                contact_dialog(),
            ),
            flex_grow="1",
            width="100%",
            padding="0.5em",
        ),
        rx.mobile_and_tablet(
            rx.box(
                rx.vstack(                    
                    rx.box(
                        rx.heading("Presentation", size="5"),
                        rx.image(src="/profile/profilbild.JPG", width="80px", border_radius= "20%"),
                        rx.text(
                            "Hello, my name is Cristian Ortega! I am a Certified Public Accountant and Auditor from Chile, and some time ago I had the opportunity to work as a Credit Card Analyst at Citibank. In this role, I was responsible for monitoring eight bridge accounts where credits issued to customers due to transaction disputes were recorded. These included duplicate payments, services not received, fraud cases, stolen cards, among others. My responsibility was to ensure that each customer case was resolved within a maximum period of three months, including the corresponding accounting process. In addition, I have studied accounting and programming in Sweden, which allows me to have a modern and comprehensive perspective on business and financial processes. My areas of expertise include accounting and auditing, proficiency in Office tools, and specialized software such as AS400 and WinRunner. I also have programming skills in Java, Spring Data, JavaScript, React, TypeScript, and Python. Currently, I am learning Smart Contracts using Solidity and Artificial Intelligence (AI Agents). My main goal is to continue learning everything related to AI and apply it to accounting, data analys, and software development.",
                            margin_top="0.5em",
                            font_size="sm",
                        ),
                        background="linear-gradient(45deg, var(--green-9), var(--plum-9))",
                        width="100%",
                        padding="0.8em",
                        border_radius="8px",
                    ),
                    rotating_display(
                        cards=_cards,
                        labels=_labels,
                        auto_rotate=True,
                        card_width="500px",
                        card_height="400px",
                    ),
                    align_items="center",
                    justify="center",
                    width="100%",
                    height="100%",
                ),
                height="100%",
                width="100%",
                overflow_y="auto",
                padding="0.5em",
            ),
        ),
        
        rx.divider(width="100%"),
        # ── Footer ──
        footer(),
        min_height="100vh",
        width="100%",
        spacing="3",
        bg=rx.color("iris", 3),
        
    )
