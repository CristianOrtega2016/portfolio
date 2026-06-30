import reflex as rx

def social_link(label: str, href: str) -> rx.Component:
    return rx.link(rx.text(label, weight="bold"), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("GitHub", "https://github.com/CristianOrtega2016"),
        social_link("LinkedIn", "https://www.linkedin.com/in/cristian-ortega-aab1523b5/"),
        spacing="3",
        justify="end",
        width="100%",
        is_external= True,
    )


def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.icon(tag="copyright", width="1.5em", color="white"),
                rx.text(
                    "2026 Cristian Ortega, MIT",
                    size="3",
                    white_space="nowrap",
                    weight="medium",
                    color="white",
                ),
                align="center",
            ),
            socials(),
            justify="between",
            align="center",
            width="100%",
            height="100%",
        ),
        bg=rx.color("iris", 3),
        padding="1em",
        width="100%",
    )

