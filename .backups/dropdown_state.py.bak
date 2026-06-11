import reflex as rx


class DropdownMenuState(rx.State):
    num_opens: int = 0
    opened: bool = False

    def count_opens(self, opened: bool):
        self.opened = opened

        if opened:
            self.num_opens += 1