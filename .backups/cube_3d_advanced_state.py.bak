import reflex as rx

class Cube3DState(rx.State):
    """Estado para manejar la rotación del cubo"""
    rotate_x: int = 0
    rotate_y: int = 0
    is_dragging: bool = False
    start_x: int = 0
    start_y: int = 0
    
    def start_drag(self, client_x: int, client_y: int):
        """Inicia el arrastre"""
        self.is_dragging = True
        self.start_x = client_x
        self.start_y = client_y
    
    def on_drag(self, client_x: int, client_y: int):
        """Maneja el arrastre para rotar el cubo"""
        if self.is_dragging:
            delta_x = client_x - self.start_x
            delta_y = client_y - self.start_y
            self.rotate_y += delta_x
            self.rotate_x -= delta_y
            self.start_x = client_x
            self.start_y = client_y
    
    def end_drag(self):
        """Termina el arrastre"""
        self.is_dragging = False