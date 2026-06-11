# components/cube_3d_with_styles.py
import reflex as rx

def add_cube_styles() -> rx.Component:
    """Componente para agregar estilos CSS dinámicamente"""
    return rx.script(
        """
        const style = document.createElement('style');
        style.textContent = `
            @keyframes spin {
                from { transform: rotateX(0deg) rotateY(0deg); }
                to { transform: rotateX(360deg) rotateY(360deg); }
            }
            .cube-container {
                width: 500px;
                height: 500px;
                perspective: 750px;
                margin: auto;
            }
            .cube {
                position: relative;
                width: 100%;
                height: 100%;
                transform-style: preserve-3d;
                transition: transform 0.1s ease;
                cursor: grab;
            }
            .cube:active {
                cursor: grabbing;
            }
            .cube-face {
                position: absolute;
                width: 100%;
                height: 100%;
                border: 2px solid white;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: auto;
                padding: 20px;
                box-sizing: border-box;
            }
            .spin-animation {
                animation: spin 20s linear infinite;
            }
        `;
        document.head.appendChild(style);
        """
    )