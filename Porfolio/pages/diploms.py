import reflex as rx
from Porfolio.components.diploms_grid import diploms_grid
from Porfolio.components.contact_dialog import contact_dialog, contact_nav_button
from Porfolio.components.navbar import navbar_icons_item, navbar_icons_menu_item
from Porfolio.components.footer import footer


def navbar_diploms() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.icon(
                        tag="binoculars", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="white"          # Color adaptable con CSS
                    ),
                    rx.icon(
                        tag="square-user-round", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="white"          # Color adaptable con CSS
                    ),
                    rx.heading("Diploms", size="7", weight="bold", color="white",),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Home", "home", "/#"),
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
                        tag="binoculars", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="white"          # Color adaptable con CSS
                    ),
                    rx.icon(
                        tag="square-user-round", # Muestra un birrete/diploma estilizado
                        width="3em",               # Tamaño en píxeles
                        color="white"          # Color adaptable con CSS
                    ),
                    rx.heading("Diploms", size="7", weight="bold", color="white",),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        navbar_icons_menu_item("Home", "home", "/#"),
                        navbar_icons_menu_item("Projects", "coins", "/#"),  
                        navbar_icons_menu_item("About me", "user-round", "/about"),                      
                        navbar_icons_menu_item("Curriculum", "layers", "/#"),
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
def diploms() -> rx.Component:
    return rx.vstack(
        navbar_diploms(),
        rx.box(
            diploms_grid(),
            flex_grow="1",
            width="100%",
        ),
        rx.divider(width="100%"),
        footer(),
        contact_dialog(),
        min_height="100vh",
        width="100%",
        spacing="3",
        bg=rx.color("iris", 3),
    )