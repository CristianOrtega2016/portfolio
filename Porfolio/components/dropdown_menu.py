import reflex as rx

from Porfolio.states.dropdown_state import DropdownMenuState


def dropdown_menu():
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
            rx.menu.item("About me"),
            rx.menu.separator(),
            rx.menu.item("Diploms"),
            rx.menu.separator(),
            rx.menu.item("Projects"),
            variant="solid",
            size="2",
            justify="center",
        ),
        on_open_change=DropdownMenuState.count_opens,
    )