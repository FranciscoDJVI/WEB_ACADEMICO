import reflex as rx
from reflex.components.el import i
from style.style import title_style
from utils.constants import Display


def tittle(title: str) -> rx.Component:
    return rx.center(
        rx.box(
            rx.text(title, style=title_style, padding=Display.SMALL),
            margin_top=Display.SMALL,
            margin_bottom=Display.SMALL,
        )
    )
