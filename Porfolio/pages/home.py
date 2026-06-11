"""Home page — interactive 3D portfolio cube."""

from __future__ import annotations

import reflex as rx
from Porfolio.components.dropdown_menu import dropdown_menu
from Porfolio.components.cube_3d_advanced import cube_3d_advanced


def _cv_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.avatar(fallback="CV", size="9"),
            rx.heading("Curriculum", size="5"),
            rx.text("Ver mi experiencia profesional"),
            rx.button(
                "Ver CV",
                on_click=lambda: rx.redirect("/cv"),
                color_scheme="blue",
            ),
        ),
        padding="20px",
        height="100%",
        width="100%",
    )


def _skills_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Habilidades", size="4"),
            rx.badge("Python", color_scheme="green"),
            rx.badge("Reflex", color_scheme="blue"),
            rx.badge("React", color_scheme="cyan"),
            rx.badge("JavaScript", color_scheme="yellow"),
            spacing="2",
        ),
        padding="20px",
    )


def _experience_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Experiencia", size="4"),
            rx.text("• 5 años en desarrollo web"),
            rx.text("• 3 años con Python"),
            rx.text("• 2 años con Reflex"),
            spacing="2",
        ),
        padding="20px",
    )


def _contact_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Contacto", size="4"),
            rx.link("GitHub", href="https://github.com"),
            rx.link("LinkedIn", href="https://linkedin.com"),
            rx.link("Twitter", href="https://twitter.com"),
            spacing="2",
        ),
        padding="20px",
    )


def _projects_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Proyectos", size="4"),
            rx.text("• Portfolio 3D"),
            rx.text("• App de tareas"),
            rx.text("• Dashboard analytics"),
            spacing="2",
        ),
        padding="20px",
    )


def _education_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Educación", size="4"),
            rx.text("🎓 Ingeniería en Sistemas"),
            rx.text("📚 Cursos de Python avanzado"),
            rx.text("🎯 Certificación en Reflex"),
            spacing="2",
        ),
        padding="20px",
    )


def home() -> rx.Component:
    """Render the home page with the 3D portfolio cube."""
    return rx.container(
        rx.flex(
            # Header row: colour-mode toggle, title, dropdown menu
            rx.flex(
                rx.color_mode.button(
                    position="left",
                    size="4",
                    top="10",
                    left="0",
                    margin="auto",
                    padding="10px",
                    justify="start",
                    align="center",
                ),
                rx.heading(
                    "Welcome to my portfolio!",
                    size="7",
                    text_align="center",
                    min_width="0%",
                    margin="auto",
                ),
                rx.box(
                    dropdown_menu(),
                    position="right",
                    top="10",
                    right="0",
                    margin="auto",
                    padding="10px",
                ),
                direction="row",
                align="center",
                justify="center",
                width="100%",
                height="20%",
                flex_wrap="wrap",
                flex_shrink="1",
            ),
            rx.divider(),
            # 3D portfolio cube
            cube_3d_advanced(
                faces={
                    'front': _cv_card(),
                    'back': _skills_card(),
                    'left': _experience_card(),
                    'right': _contact_card(),
                    'top': _projects_card(),
                    'bottom': _education_card(),
                },
                width=500,
                height=500,
                auto_rotate=False,
            ),
        ),
    )
