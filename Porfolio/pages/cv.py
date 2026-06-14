"""CV / Resume page."""

from __future__ import annotations

import reflex as rx


def _section_header(text: str) -> rx.Component:
    return rx.heading(text, size="5", margin_top="1.5em", margin_bottom="0.5em")


def cv() -> rx.Component:
    """Render the CV / resume page."""
    return rx.container(
        rx.vstack(
            rx.link("← back to home", href="/"),
            rx.heading("Resume", size="8"),
            rx.divider(),
            # Personal info
            _section_header("Datos Personales"),
            rx.text("Nombre: Cristian González"),
            rx.text("Email: cristian@example.com"),
            rx.text("Ubicación: Stockholm, Sweden"),
            rx.divider(),
            # Experience
            _section_header("Experiencia Profesional"),
            rx.text("• Desarrollador Full-Stack (2020 - presente)"),
            rx.text("• Ingeniero de Software (2018 - 2020)"),
            rx.text("• Desarrollador Junior (2016 - 2018)"),
            rx.divider(),
            # Education
            _section_header("Educación"),
            rx.text("🎓 Ingeniería en Sistemas - Universidad Nacional"),
            rx.text("📚 Máster en Desarrollo Web"),
            rx.divider(),
            # Skills
            _section_header("Habilidades Técnicas"),
            rx.badge("Python", color_scheme="green"),
            rx.badge("Reflex", color_scheme="blue"),
            rx.badge("React", color_scheme="cyan"),
            rx.badge("JavaScript", color_scheme="yellow"),
            rx.badge("TypeScript", color_scheme="orange"),
            rx.badge("SQL", color_scheme="purple"),
            width="100%",
            spacing="2",
            align="start",
        ),
        padding_y="2em",
    )
