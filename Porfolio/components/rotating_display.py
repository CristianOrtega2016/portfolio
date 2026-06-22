# components/rotating_display.py
"""2D horizontal card slider — slides left to right with auto-advance."""

from __future__ import annotations

import asyncio
import reflex as rx
from typing import List


class RotatingDisplayState(rx.State):
    """State for the horizontal card slider."""
    current_index: int = 0
    total_cards: int = 6

    def next_card(self):
        """Slide to the next card."""
        self.current_index = (self.current_index + 1) % self.total_cards

    def prev_card(self):
        """Slide to the previous card."""
        self.current_index = (self.current_index - 1) % self.total_cards

    def go_to_card(self, index: int):
        """Jump to a specific card."""
        if 0 <= index < self.total_cards:
            self.current_index = index

    @rx.event(background=True)
    async def run_loop(self):
        """Background loop that auto-advances every 3 seconds."""
        while True:
            await asyncio.sleep(3.0)
            async with self:
                self.next_card()


def rotating_display(
    cards: List[rx.Component],
    labels: List[str],
    auto_rotate: bool = True,
    card_width: str = "500px",
    card_height: str = "400px",
) -> rx.Component:
    """2D horizontal card slider with auto-advance.

    Cards slide left-to-right with a smooth CSS translation.
    Navigation via arrows, dot indicators, and automatic every few seconds.

    Args:
        cards: List of card components.
        labels: Short labels for each card.
        auto_rotate: Enable auto-sliding.
        card_width: Width of the visible card area.
        card_height: Height of the visible card area.

    Returns:
        A horizontal sliding card component.
    """
    total = len(cards)
    if total == 0:
        return rx.box(rx.text("No content"), padding="20px")

    # Responsive sizes
    tablet_w = "min(420px, 90vw)"
    mobile_w = "min(320px, 95vw)"
    tablet_h = "min(360px, 70vh)"
    mobile_h = "min(300px, 60vh)"

    # Build the track with all cards laid out horizontally
    track_cards = []
    for card in cards:
        track_cards.append(
            rx.box(
                card,
                width="100%",
                height="100%",
                min_width="100%",
                padding="0 8px",
                flex_shrink="0",
            )
        )

    # Dots indicator
    dots = []
    for i in range(total):
        dots.append(
            rx.box(
                width="12px",
                height="12px",
                border_radius="50%",
                background_color=rx.cond(
                    RotatingDisplayState.current_index == i,
                    "var(--accent-9)",
                    "var(--gray-6)",
                ),
                cursor="pointer",
                on_click=RotatingDisplayState.go_to_card(i),
                _hover={"transform": "scale(1.2)", "transition": "all 0.2s"},
            )
        )

    # Build a reactive transform expression using rx.cond chain
    def _build_transform_cond(idx: int) -> str | rx.Var:
        """Recursively build rx.cond chain for translateX."""
        offset = -idx * 100
        if idx == total - 1:
            return f"translateX({offset}%)"
        return rx.cond(
            RotatingDisplayState.current_index == idx,
            f"translateX({offset}%)",
            _build_transform_cond(idx + 1),
        )

    # Build a reactive label expression using rx.cond chain
    def _label_at(idx: int):
        if idx == total - 1:
            return labels[idx]
        return rx.cond(
            RotatingDisplayState.current_index == idx,
            labels[idx],
            _label_at(idx + 1),
        )

    return rx.box(
        # Start auto-slide on mount
        rx.box(
            on_mount=RotatingDisplayState.run_loop if auto_rotate else None,
            display="none",
        ),

        # Viewport + track container
        rx.box(
            # Track (all cards in a row, translated)
            rx.hstack(
                *track_cards,
                spacing="0",
                flex_wrap="nowrap",
                # Smooth sliding transition
                transition="transform 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                transform=_build_transform_cond(0),
            ),
            width="100%",
            height="100%",
            overflow="hidden",
            border_radius="12px",
        ),

        # Navigation row
        rx.hstack(
            rx.icon_button(
                rx.icon("chevron_left", size=22),
                on_click=RotatingDisplayState.prev_card,
                variant="soft",
                size="3",
                aria_label="Previous",
            ),
            rx.hstack(*dots, spacing="2"),
            rx.icon_button(
                rx.icon("chevron_right", size=22),
                on_click=RotatingDisplayState.next_card,
                variant="soft",
                size="3",
                aria_label="Next",
            ),
            spacing="4",
            justify="center",
            align="center",
            width="100%",
            padding_top="1em",
        ),

        # Active label
        rx.text(
            _label_at(0),
            font_size="sm",
            color="gray",
            text_align="center",
            padding_top="0.3em",
        ),

        width="100%",
        max_width=[card_width, tablet_w, mobile_w],
        height=[card_height, tablet_h, mobile_h],
    )
