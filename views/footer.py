import reflex as rx
from reflex.components.core.colors import color
from utils.constants import Display, FontSize
from style.style import icons_hover

def footer() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text(
                "Academico.net/servicios tecnologicos© 2024.",
                font_size=FontSize.VERY_SMALL,
                color="#b3b6b7",
            ),
            rx.text(
                "Todos los derechos reservados.",
                font_size=FontSize.VERY_SMALL,
                color="#b3b6b7",
            ),
            direction="row",
            justify="center",
            align="center",
            margin_top=Display.SMALL,
        ),
    )
