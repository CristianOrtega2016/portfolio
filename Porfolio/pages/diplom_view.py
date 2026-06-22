import reflex as rx


class DiplomViewState(rx.State):
    """State for the diploma PDF viewer page."""

    @rx.var
    def pdf_src(self) -> str:
        return f"/diploms/{self.router._page.params.get('file_name', '')}"


def diplom_page() -> rx.Component:
    return rx.box(
        rx.el.iframe(
            src=DiplomViewState.pdf_src,
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            border="none",
            background="#f5f5f5",
        ),
        rx.link(
            "← Back to diploms",
            href="/diploms",
            position="fixed",
            top="1rem",
            left="1rem",
            z_index="10",
            padding="0.5rem 1rem",
            background="white",
            border_radius="0.5rem",
            box_shadow="0 2px 8px rgba(0,0,0,0.15)",
            text_decoration="none",
            font_weight="bold",
        ),
    )
