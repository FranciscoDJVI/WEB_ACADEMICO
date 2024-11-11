import reflex as rx
from components.tittle import tittle
from components.body_text import body_text
from utils.constants import FontSize
from utils.constants import Display
from components.navb import navbar
from components.button_whatsapp import button_whatsapp
from views.footer import footer
from style.style import background


@rx.page("/", title="Home", description="Home page")
def home() -> rx.Component:
    return rx.container(
        rx.flex(
            navbar(),
            tittle("Academico.NET"),
            body_text(
                "Servivos de realización de tesis,trabajos escritos y consultoria."
            ),
            button_whatsapp(),
            rx.separator(),
            rx.spacer(),
            footer(),
            rx.spacer(),
            font_size=FontSize.MEDIUN,
            direction="column",
            spacing="4",
            justify="start",
        ),
        margin_left=Display.LARGE,
        margin_right=Display.LARGE,
    )
