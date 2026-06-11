import reflex as rx

class Cube3DState(rx.State):
    """Estado para manejar la rotación del cubo mediante click y arrastre."""
    rotate_x: int = 0
    rotate_y: int = 0
    is_dragging: bool = False
    start_x: int = 0
    start_y: int = 0

    def start_drag(self, e):
        """Inicia el arrastre. Recibe un PointerEvent con client_x, client_y."""
        self.is_dragging = True
        self.start_x = int(e.client_x)
        self.start_y = int(e.client_y)

    def on_drag(self, e):
        """Maneja el arrastre para rotar el cubo. Recibe un PointerEvent."""
        if self.is_dragging:
            client_x = int(e.client_x)
            client_y = int(e.client_y)
            delta_x = client_x - self.start_x
            delta_y = client_y - self.start_y
            self.rotate_y += delta_x
            self.rotate_x -= delta_y
            self.start_x = client_x
            self.start_y = client_y

    def end_drag(self):
        """Termina el arrastre."""
        self.is_dragging = False
