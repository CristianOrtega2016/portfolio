import reflex as rx

from Porfolio.states.dropdown_state import DropdownMenuState


def dropdown_menu() -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon("menu"),  # Icono de hamburguesa
                "Menu",
                variant="ghost",
                size="4",
                bg="center/cover url('/reflex_icon.png')",
                position="relative",
                align="right",
                justify="right",
            )
        ),
        rx.menu.content(
            rx.menu.item("About me", on_click=lambda: rx.redirect("/about")),
            rx.menu.separator(),
            rx.menu.item("Diploms", on_click=lambda: rx.redirect("/diploms")),
            rx.menu.separator(),
            rx.menu.item("Projects", on_click=lambda: rx.redirect("/projects")),
            variant="solid",
            size="2",
            justify="center",
        ),
        on_open_change=DropdownMenuState.count_opens,
    )