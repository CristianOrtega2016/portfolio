import reflex as rx
from Porfolio.states.contact_card_state import ContactCardState


def contact_dialog() -> rx.Component:
    """Contact info dialog — controlled by ContactCardState.

    Place this once at the page level (e.g. inside the page layout).
    The trigger buttons in the navbar toggle ContactCardState.open.
    """
    return rx.cond(
        ContactCardState.open,
        rx.dialog.root(
            rx.dialog.content(
                rx.dialog.title("Contact Information"),
                rx.card(
                    rx.data_list.root(
                        rx.data_list.item(
                            rx.data_list.label("Name"),
                            rx.data_list.value(
                                rx.badge("Cristian Ortega", variant="soft", radius="full"),
                            ),
                            align="center",
                        ),
                        rx.data_list.item(
                            rx.data_list.label("Phonenumber"),
                            rx.data_list.value(rx.code("+46769466215")),
                        ),
                        rx.data_list.item(
                            rx.data_list.label("LinkedIn"),
                            rx.data_list.value(
                                rx.link(
                                    "Cristian Ortega",
                                    href="https://www.linkedin.com/in/cristian-ortega-aab1523b5/",
                                    is_external=True,
                                ),
                            ),
                        ),
                        rx.data_list.item(
                            rx.data_list.label("Email"),
                            rx.data_list.value(
                                rx.link(
                                    "cristian.ortega.01@gmail.com",
                                    href="mailto:cristian.ortega.01@gmail.com",
                                ),
                            ),
                        ),
                        rx.data_list.item(
                            rx.data_list.label("Discord"),
                            rx.data_list.value(
                                rx.link(
                                    "cristian_ortega_2026",
                                    href="https://discord.com/",
                                    is_external=True,
                                ),
                            ),
                        ),
                        rx.data_list.item(
                            rx.data_list.label("GitHub"),
                            rx.data_list.value(
                                rx.link(
                                    "CristianOrtega2016",
                                    href="https://github.com/CristianOrtega2016",
                                    is_external=True,
                                ),
                            ),
                        ),
                    ),
                    
                    width="40vw",
                    height="50vh",
                    bg=rx.color("blue", 3),
                ),
                #rx.dialog.close(
                #    rx.button("Close", on_click=ContactCardState.toggle),
                #    padding="15px",
                #),
                height="65vh",
                
            ),
            open=True,
            on_open_change=ContactCardState.toggle,            
        ),
    )


def contact_nav_button(text: str = "Contact", icon: str = "file-user", size: str = "4") -> rx.Component:
    """Navbar button that toggles the contact dialog."""
    return rx.button(
        rx.hstack(rx.icon(icon), rx.text(text, size=size, weight="medium")),
        color="white",
        cursor="pointer",
        variant="ghost",
        on_click=ContactCardState.toggle,
    )
