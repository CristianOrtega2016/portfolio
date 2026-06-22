import reflex as rx

def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(rx.icon(icon), rx.text(text, size="4", weight="medium")),
        href=url,
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16), rx.text(text, size="3", weight="medium")
        ),
        href=url,
    )


def navbar_icons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/profile/profilbild.JPG",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("About me", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Home", "home", "/#"),
                    navbar_icons_item("Pricing", "coins", "/#"),
                    navbar_icons_item("Contact", "mail", "/#"),
                    navbar_icons_item("Services", "layers", "/#"),
                    spacing="6",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/profile/profilbild.JPG",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("About me", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        navbar_icons_menu_item("Home", "home", "/#"),
                        navbar_icons_menu_item("Pricing", "coins", "/#"),
                        navbar_icons_menu_item("Contact", "mail", "/#"),
                        navbar_icons_menu_item("Services", "layers", "/#"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("blue", 5),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        
    )
def body_item() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
               rx.box(
                rx.text(
                    """
                    I am a highly motivated individual with a strong passion for programming and web development.
                    Over the past years, I have intentionally focused my learning path toward Web3 technologies,
                    driven by my interest in decentralized systems and their real-world impact.
                    """
                ),

                rx.text(
                    """
                    To build a solid foundation, I enrolled in a MOOC program at the University of Nicosia,
                    where I am currently completing my certification in blockchain-related studies.
                    In parallel, I have been self-studying Solidity and Artificial Intelligence.
                    """
                ),

                rx.text(
                    """
                    My main focus in Web3 is Solidity development, with the goal of becoming a professional
                    Web3 developer specialized in smart contracts and decentralized applications (DApps).
                    """
                ),

                rx.text(
                    """
                    In addition to blockchain, I am actively exploring Artificial Intelligence,
                    particularly its integration into applications and workflows.
                    """
                ),

                rx.text(
                    """
                    Beyond technology, I bring a strong professional background in finance,
                    administration, accounting, and financial analysis.
                    """
                ),

                
                padding="2em",
                spacing="5",
                align_items="start",
                width="33%",
                border_radius="3px", 
                border="solid",
                border_color="indigo",
            ),
                rx.box(
                    rx.text(
                        """
                        Today, I am actively seeking opportunities in the Web3 space, where I can combine
                        my technical skills, financial knowledge, and passion for decentralized technologies.
                        """
                    ),

                    rx.text(
                        """
                        Thank you for your time and consideration.
                        I would welcome the opportunity to further discuss how my background and motivation
                        can add value to your organization.
                        """
                    ),

                    rx.text(
                        "Kind regards,",
                        font_weight="bold",
                    ),

                    rx.text(
                        "Cristian Ortega",
                        font_weight="bold",
                    ),
                    padding="2em",
                    spacing="5",
                    align_items="stretch",
                    width="33%",
                    border="solid",
                    border_radius="3px",
                    height="auto",
                    border_color="indigo",
                ),
      
            ),
               
        ),

        rx.mobile_and_tablet(
            rx.box(
                rx.text(
                    """
                    I am a highly motivated individual with a strong passion for programming and web development.
                    Over the past years, I have intentionally focused my learning path toward Web3 technologies,
                    driven by my interest in decentralized systems and their real-world impact.
                    """
                    
                ),

                rx.text(
                    """
                    To build a solid foundation, I enrolled in a MOOC program at the University of Nicosia,
                    where I am currently completing my certification in blockchain-related studies.
                    In parallel, I have been self-studying Solidity and Artificial Intelligence.
                    """
                ),

                rx.text(
                    """
                    My main focus in Web3 is Solidity development, with the goal of becoming a professional
                    Web3 developer specialized in smart contracts and decentralized applications (DApps).
                    """
                ),

                rx.text(
                    """
                    In addition to blockchain, I am actively exploring Artificial Intelligence,
                    particularly its integration into applications and workflows.
                    """
                ),

                rx.text(
                    """
                    Beyond technology, I bring a strong professional background in finance,
                    administration, accounting, and financial analysis.
                    """
                ),

                rx.text(
                    """
                    Today, I am actively seeking opportunities in the Web3 space, where I can combine
                    my technical skills, financial knowledge, and passion for decentralized technologies.
                    """
                ),

                rx.text(
                    """
                    Thank you for your time and consideration.
                    I would welcome the opportunity to further discuss how my background and motivation
                    can add value to your organization.
                    """
                ),

                rx.text(
                    "Kind regards,",
                    font_weight="bold",
                ),

                rx.text(
                    "Cristian Ortega",
                    font_weight="bold",
                ),

            spacing="5",
            align_items="start",
            width="100%",
            )
        ),
)

def about() -> rx.Component:
    return rx.vstack(
                navbar_icons(),
                body_item(),
                bg=rx.color("cyan", 7), 
    )

