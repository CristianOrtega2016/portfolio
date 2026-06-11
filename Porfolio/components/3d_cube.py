# components/3d_cube.py
import reflex as rx

def cube_3d(
    content: rx.Component,
    width: int = 300,
    height: int = 300,
    rotation_speed: float = 0.01,
    **props
) -> rx.Component:
    """Wrapper para el componente Cube3D de React"""
    
    return rx.react(
        # Nombre del componente React
        "Cube3D",
        # Props que se pasan al componente
        width=width,
        height=height,
        rotation_speed=rotation_speed,
        # El contenido de Reflex se pasa como children
        children=[content],
        **props
    )# components/3d_cube.py
import reflex as rx

def cube_3d(
    content: rx.Component,
    width: int = 300,
    height: int = 300,
    rotation_speed: float = 0.01,
    **props
) -> rx.Component:
    """Wrapper para el componente Cube3D de React"""
    
    return rx.react(
        # Nombre del componente React
        "Cube3D",
        # Props que se pasan al componente
        width=width,
        height=height,
        rotation_speed=rotation_speed,
        # El contenido de Reflex se pasa como children
        children=[content],
        **props
    )