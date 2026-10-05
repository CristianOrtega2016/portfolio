import reflex as rx

def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")),
        color="white",
        href=url,
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")
        ),
        # Dark text: these items render both inside the (white) dropdown panel
        # and on the light iris navbar. White was invisible on the panel.
        color=rx.color("gray", 12),
        href=url,
    )