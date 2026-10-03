from __future__ import annotations

import asyncio
import reflex as rx


class RotatingDisplayState(rx.State):
    current_index: int = 0
    total_cards: int = 6
    loop_running: bool = False

    def next_card(self):
        self.current_index = (self.current_index + 1) % self.total_cards

    def prev_card(self):
        self.current_index = (self.current_index - 1) % self.total_cards

    def go_to_card(self, index: int):
        if 0 <= index < self.total_cards:
            self.current_index = index

    @rx.event(background=True)
    async def run_loop(self):
        # Evita que se creen varios loops simultáneos
        async with self:
            if self.loop_running:
                return

            self.loop_running = True

        try:
            while True:
                await asyncio.sleep(3.0)

                async with self:
                    self.next_card()

        finally:
            async with self:
                self.loop_running = False


def rotating_display(
    cards,
    labels,
    auto_rotate=True,
    card_width="500px",
    card_height="400px",
):
    total = len(cards)

    # Mantener el estado sincronizado con la cantidad real de tarjetas
    RotatingDisplayState.total_cards = total

    # Cada tarjeta ocupa exactamente 1/N del track.
    slide_width = f"{100 / total}%"

    track_cards = []

    for card in cards:
        track_cards.append(
            rx.box(
                card,
                width=slide_width,
                min_width=slide_width,
                height="100%",
                flex=f"0 0 {slide_width}",
                box_sizing="border-box",
                padding="0 8px",
            )
        )

    # El track completo mide N veces el viewport.
    track_width = f"{total * 100}%"

    # Cada posición desplaza exactamente 1 tarjeta.
    transform = rx.cond(
        RotatingDisplayState.current_index == 0,
        "translateX(0%)",
        rx.cond(
            RotatingDisplayState.current_index == 1,
            f"translateX(-{100 / total}%)",
            rx.cond(
                RotatingDisplayState.current_index == 2,
                f"translateX(-{2 * 100 / total}%)",
                rx.cond(
                    RotatingDisplayState.current_index == 3,
                    f"translateX(-{3 * 100 / total}%)",
                    rx.cond(
                        RotatingDisplayState.current_index == 4,
                        f"translateX(-{4 * 100 / total}%)",
                        f"translateX(-{5 * 100 / total}%)",
                    ),
                ),
            ),
        ),
    )

    return rx.box(
        # Inicia el autoplay solamente si esta instancia lo necesita.
        rx.box(
            on_mount=(
                RotatingDisplayState.run_loop
                if auto_rotate
                else None
            ),
            display="none",
        ),

        # VIEWPORT
        rx.box(
            # TRACK
            rx.box(
                *track_cards,
                display="flex",
                flex_direction="row",
                flex_wrap="nowrap",
                width=track_width,
                height="100%",
                transform=transform,
                transition=(
                    "transform 0.4s "
                    "cubic-bezier(0.4, 0, 0.2, 1)"
                ),
            ),

            width="100%",
            height="100%",
            overflow="hidden",
            border_radius="12px",
        ),

        width="100%",
        max_width=card_width,
        height=card_height,
    )

