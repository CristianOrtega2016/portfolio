# components/cube_3d_advanced.py
import reflex as rx
from typing import Dict
from Porfolio.states.cube_3d_advanced_state import Cube3DState
# components/cube_3d_advanced.py - Versión simplificada que sí funciona

def cube_3d_advanced(
    faces: Dict[str, rx.Component],
    width: int = 400,
    height: int = 400,
    auto_rotate: bool = False,
) -> rx.Component:
    """Cubo 3D usando solo componentes nativos de Reflex con CSS inline"""
    
    # Estilos CSS inline usando rx.style
    cube_styles = {
        ".cube-container": {
            "width": f"{width}px",
            "height": f"{height}px",
            "perspective": f"{width * 1.5}px",
            "margin": "auto",
        },
        ".cube": {
            "position": "relative",
            "width": "100%",
            "height": "100%",
            "transform_style": "preserve-3d",
            "transition": "transform 0.1s ease",
            "cursor": "grab",
        },
        ".cube:active": {
            "cursor": "grabbing",
        },
        ".cube-face": {
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
        },
        "@keyframes spin": {
            "from": {"transform": "rotateX(0deg) rotateY(0deg)"},
            "to": {"transform": "rotateX(360deg) rotateY(360deg)"},
        },
        ".spin-animation": {
            "animation": "spin 20s linear infinite",
        },
    }
    
    transform_value = f"rotateX({Cube3DState.rotate_x}deg) rotateY({Cube3DState.rotate_y}deg)"
    
    cube_class = "cube"
    if auto_rotate:
        cube_class += " spin-animation"
    
    return rx.box(
        # Inyectar estilos CSS
        rx.style(cube_styles),
        
        # Contenedor del cubo
        rx.box(
            # Cara frontal
            rx.box(
                faces.get('front', rx.card(
                    rx.vstack(
                        rx.heading("Front Face", size="4"),
                        rx.text("Contenido frontal"),
                    ),
                    width="100%",
                    height="100%",
                )),
                class_name="cube-face",
                style={"transform": "translateZ(200px)", "bg": "rgba(59, 130, 246, 0.9)"},
            ),
            
            # Cara trasera
            rx.box(
                faces.get('back', rx.card(
                    rx.vstack(
                        rx.heading("Back Face", size="4"),
                        rx.text("Contenido trasero"),
                    ),
                    width="100%",
                    height="100%",
                )),
                class_name="cube-face",
                style={"transform": "rotateY(180deg) translateZ(200px)", "bg": "rgba(236, 72, 153, 0.9)"},
            ),
            
            # Cara derecha
            rx.box(
                faces.get('right', rx.card(
                    rx.vstack(
                        rx.heading("Right Face", size="4"),
                        rx.text("Contenido derecho"),
                    ),
                    width="100%",
                    height="100%",
                )),
                class_name="cube-face",
                style={"transform": "rotateY(90deg) translateZ(200px)", "bg": "rgba(16, 185, 129, 0.9)"},
            ),
            
            # Cara izquierda
            rx.box(
                faces.get('left', rx.card(
                    rx.vstack(
                        rx.heading("Left Face", size="4"),
                        rx.text("Contenido izquierdo"),
                    ),
                    width="100%",
                    height="100%",
                )),
                class_name="cube-face",
                style={"transform": "rotateY(-90deg) translateZ(200px)", "bg": "rgba(245, 158, 11, 0.9)"},
            ),
            
            # Cara superior
            rx.box(
                faces.get('top', rx.card(
                    rx.vstack(
                        rx.heading("Top Face", size="4"),
                        rx.text("Contenido superior"),
                    ),
                    width="100%",
                    height="100%",
                )),
                class_name="cube-face",
                style={"transform": "rotateX(90deg) translateZ(200px)", "bg": "rgba(139, 92, 246, 0.9)"},
            ),
            
            # Cara inferior
            rx.box(
                faces.get('bottom', rx.card(
                    rx.vstack(
                        rx.heading("Bottom Face", size="4"),
                        rx.text("Contenido inferior"),
                    ),
                    width="100%",
                    height="100%",
                )),
                class_name="cube-face",
                style={"transform": "rotateX(-90deg) translateZ(200px)", "bg": "rgba(239, 68, 68, 0.9)"},
            ),
            
            class_name=cube_class,
            style={"transform": transform_value},
            on_mouse_down=lambda e: Cube3DState.start_drag(e.client_x, e.client_y),
            on_mouse_move=lambda e: Cube3DState.on_drag(e.client_x, e.client_y),
            on_mouse_up=Cube3DState.end_drag,
            on_mouse_leave=Cube3DState.end_drag,
        ),
        class_name="cube-container",
    )