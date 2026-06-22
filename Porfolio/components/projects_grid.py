import reflex as rx

def projects_card(name_png: str, source_url: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.box(
                rx.flex(
                    rx.image(
                        src=f"/pictures/{name_png}",
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
        href=source_url,
        is_external=True,
        text_decoration="none",
        
    )

def projects_grid() -> rx.Component:

    diploms = [
        projects_card("fundme_code.png", "https://github.com/CristianOrtega2016/foundry-fund-me.git"),
        projects_card("github_profile.png", "https://github.com/CristianOrtega2016"),
        projects_card("cyfrin_courses_2.png", "https://updraft.cyfrin.io/courses"),
        projects_card("cyfrin_courses.png", "https://updraft.cyfrin.io/courses"),
        projects_card("linkedin_profile.png", "linkedin.com/in/cristian-ortega-aab1523b5"),
        projects_card("lottery_code.png", "https://github.com/CristianOrtega2016/Raffle.git"),
        projects_card("reflex_code.png", "https://github.com/CristianOrtega2016/portfolio.git"),
        projects_card("token_app_frontend.png", "https://github.com/CristianOrtega2016/erc20-platform-token-dapp.git"),
        projects_card("token_app_solidity.png", "https://sepolia.etherscan.io/address/0x4bfB347B2D1bbef14cE2f1fbde8B8D707727500D"),
        projects_card("token_app.png", "https://project-inres.vercel.app/"),
        projects_card("video_transcriber_code.png", "https://github.com/CristianOrtega2016/AI.git"),
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


    