import reflex as rx

def diploms_card(name_png: str, pdf_url: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.box(
                rx.flex(
                    rx.image(
                        src=f"/diploms_pictures/{name_png}",
                        width="100%",
                        height="auto",
                        max_height="8rem",
                        object_fit="contain",
                        border_radius="1rem",
                    ),
                    rx.box(
                        rx.heading(name_png.removesuffix(".png"), size="4"),
                        rx.text("Click the image to zoom"),
                    ),
                    spacing="2",
                    direction="column",
                    align="center",
                    width="100%",
                ),
            ),
            as_child=True,
            width="100%",
            height=["40vh", "35vh", "30vh"],
            border="solid",
            border_color="cyan",
            border_radius="1rem",
            _hover={
                "background": "linear-gradient(45deg, var(--yellow-3), var(--plum-6))",
                },
        ),
        href=pdf_url,
        text_decoration="none",
        
    )

def diploms_grid() -> rx.Component:

    diploms = [
        diploms_card("Betyg_Javautvecklare.png", "/pdfview/Betyg_Javautvecklare.pdf"),
        diploms_card("Examen_Bevis_Javautvecklare.png", "/pdfview/Examen_Bevis_Javautvecklare.pdf"),
        diploms_card("Högskoleverkets bedömning.png", "/pdfview/Högskoleverkets bedömning.pdf"),
        diploms_card("Magisterexamen_Chile.png", "/pdfview/Magisterexamen_Chile.pdf"),
        diploms_card("Utbildningsbevis ekonomi.png", "/pdfview/Utbildningsbevis ekonomi.pdf"),
    ]

    return rx.grid(
        *diploms,
        columns=["3", "2", "1"],
        flow="row-dense",
        justify="between",
        spacing_x="9",
        spacing_y="9",
        width="100%",
        max_width="100%",
        border="solid",
        border_color="white",
        border_radius="0.5rem", bg=rx.color("iris", 3),
        padding="1em",
        overflow="hidden",
    )


    