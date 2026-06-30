import reflex as rx

class ContactCardState(rx.State):

    open: bool = False

    def toggle(self):
        self.open = not self.open