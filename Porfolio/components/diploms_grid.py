import reflex as rx

def diploms_card(name_png: str, pdf_url: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.box(
                rx.flex(
                    rx.image(
                        src=f"/diploms_pictures/{name_png}",
                        width="20rem",
                        height="10rem",
                        border_radius="1rem",
                    ),
                    rx.box(
                        rx.heading(name_png.removesuffix(".png")),
                        rx.text("Click the image to zoom"),
                    ),
                    spacing="2",
                    direction="column",
                    align="center",
                ),
            ),
            as_child=True,
            width="30vw",
            height="40vh",
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
        columns="3",
        flow="row-dense",
        justify="between",
        spacing_x="9",
        spacing_y="9",
        width="100%",
        border="solid",
        border_color="white",
        border_radius="0.5rem", bg=rx.color("iris", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        
    )


    