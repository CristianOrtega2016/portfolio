import reflex as rx
from Porfolio.components.projects_grid import projects_grid

def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")),
        color="yellow",
        href=url,
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")
        ),
        href=url,
    )


def navbar_projects() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        tag="graduation-cap", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="yellow"          # Color adaptable con CSS
                    ),
                    rx.icon(
                        tag="award", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="yellow"          # Color adaptable con CSS
                    ),
                    rx.heading("Projects", size="7", weight="bold", color="yellow",),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Home", "home", "/#"),
                    navbar_icons_item("Projects", "coins", "/#"),
                    navbar_icons_item("Contact", "mail", "/#"),
                    navbar_icons_item("Curriculum", "layers", "/cv"),
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
                        tag="graduation-cap", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="yellow"          # Color adaptable con CSS
                    ),
                    rx.icon(
                        tag="award", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="yellow"          # Color adaptable con CSS
                    ),
                    rx.heading("Diploms", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        navbar_icons_menu_item("Home", "home", "/#"),
                        navbar_icons_menu_item("Projects", "folder", "/#"),
                        navbar_icons_menu_item("Contact", "mail", "/#"),
                        navbar_icons_menu_item("Curriculum", "layers", "/#"),
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
def projects() -> rx.Component:
    return rx.box(
        navbar_projects(),
        projects_grid(),
    )