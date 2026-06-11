# components/cube_3d_advanced.py
from __future__ import annotations

import reflex as rx
from typing import Dict
from Porfolio.states.cube_3d_advanced_state import Cube3DState


def _translate_z(width: int, height: int) -> str:
    """Calculate the translateZ value dynamically based on cube dimensions.

    The translateZ should be half the smallest dimension (width or height)
    so all 6 faces form a perfect cube.
    """
    z = min(width, height) // 2
    return f"{z}px"


def _perspective(width: int, height: int) -> str:
    """Calculate a reasonable perspective value based on cube size."""
    p = max(width, height) * 1.5
    return f"{p:.0f}px"


def _face_style(color: str, transform: str, tz: str) -> dict:
    """Generate style dict for a cube face."""
    return {
        "position": "absolute",
        "width": "100%",
        "height": "100%",
        "border": "2px solid white",
        "border_radius": "8px",
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "overflow": "auto",
        "padding": "20px",
        "box_sizing": "border-box",
        "backface_visibility": "visible",
        "background_color": color,
        "transform": transform,
    }


def cube_3d_advanced(
    faces: Dict[str, rx.Component],
    width: int = 400,
    height: int = 400,
    auto_rotate: bool = False,
) -> rx.Component:
    """3D interactive cube built with native Reflex components.

    Uses on_click (pointer_event_spec), on_double_click, and on_mouse_leave
    for click-based interaction. Click and drag the cube to rotate it.

    Args:
        faces: Dictionary mapping face names ('front', 'back', 'left', 'right', 'top', 'bottom')
               to their corresponding Reflex components.
        width: Cube width in pixels.
        height: Cube height in pixels.
        auto_rotate: Whether the cube should auto-rotate on load.

    Returns:
        A Reflex component displaying the 3D cube.
    """
    tz = _translate_z(width, height)

    # Responsive sizing
    tablet_w = min(width, 300)
    tablet_h = min(height, 300)
    mobile_w = min(width, 260)
    mobile_h = min(height, 260)

    transform_value = f"rotateX({Cube3DState.rotate_x}deg) rotateY({Cube3DState.rotate_y}deg)"

    face_configs = [
        ("front", f"translateZ({tz})", "rgba(59, 130, 246, 0.9)"),
        ("back", f"rotateY(180deg) translateZ({tz})", "rgba(236, 72, 153, 0.9)"),
        ("right", f"rotateY(90deg) translateZ({tz})", "rgba(16, 185, 129, 0.9)"),
        ("left", f"rotateY(-90deg) translateZ({tz})", "rgba(245, 158, 11, 0.9)"),
        ("top", f"rotateX(90deg) translateZ({tz})", "rgba(139, 92, 246, 0.9)"),
        ("bottom", f"rotateX(-90deg) translateZ({tz})", "rgba(239, 68, 68, 0.9)"),
    ]

    faces_rx = []
    for name, face_transform, bg_color in face_configs:
        content = faces.get(
            name,
            rx.card(
                rx.vstack(
                    rx.heading(f"{name.capitalize()} Face", size="4"),
                ),
                width="100%",
                height="100%",
            ),
        )
        faces_rx.append(
            rx.box(
                content,
                style=_face_style(bg_color, face_transform, tz),
            )
        )

    perspective = _perspective(width, height)

    # Use on_click (which passes pointer_event_spec with client_x/client_y)
    # for both starting and continuing the drag.
    return rx.box(
        rx.box(
            *faces_rx,
            style={
                "position": "relative",
                "width": "100%",
                "height": "100%",
                "transform_style": "preserve-3d",
                "transition": "transform 0.1s ease",
                "cursor": "grab",
                "transform": transform_value,
            },
            on_click=[
                Cube3DState.start_drag,
                Cube3DState.on_drag,
            ],
            on_double_click=Cube3DState.end_drag,
            on_context_menu=Cube3DState.end_drag,
            on_mouse_leave=Cube3DState.end_drag,
            width="100%",
            height="100%",
        ),
        style={
            "width": f"{width}px",
            "height": f"{height}px",
            "perspective": perspective,
            "margin": "auto",
            "max_width": "min(100vw, 100%)",
        },
        # Responsive via Reflex breakpoints
        width=[f"{width}px", f"{tablet_w}px", f"{mobile_w}px"],
        height=[f"{height}px", f"{tablet_h}px", f"{mobile_h}px"],
    )
