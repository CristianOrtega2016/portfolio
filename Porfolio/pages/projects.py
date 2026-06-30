import reflex as rx
from Porfolio.components.projects_grid import projects_grid
from Porfolio.components.contact_dialog import contact_dialog, contact_nav_button
from Porfolio.components.navbar import navbar_icons_item, navbar_icons_menu_item


def navbar_projects() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.icon(tag="binoculars", width="3em", color="white"),
                    rx.icon(tag="square-user-round", width="3em", color="white"),
                    rx.heading("Projects", size="7", weight="bold", color="white"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Home", "home", "/#"),
                    navbar_icons_item("Diploms", "file-stack", "/diploms"), 
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
                    rx.icon(tag="binoculars", width="3em", color="white"),
                    rx.icon(tag="square-user-round", width="3em", color="white"),
                    rx.heading("Projects", size="7", weight="bold", color="white"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        navbar_icons_menu_item("Home", "home", "/#"),
                        navbar_icons_menu_item("Diploms", "file-stack", "/diploms"),
                        navbar_icons_menu_item("About me", "user-round", "/about"),                         
                        navbar_icons_menu_item("Curriculum", "book-text", "/cv"),
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
        width="100%",
    )


def projects() -> rx.Component:
    return rx.box(
        navbar_projects(),
        projects_grid(),
        contact_dialog(),
    )
