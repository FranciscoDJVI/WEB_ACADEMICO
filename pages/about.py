import reflex as rx
from components.tittle import tittle
from components.navb import navbar
from components.table import table
from views.footer import footer
from utils.constants import Display

@rx.page("/about", title="about", description="Información acerca de la empresa.")
def about() -> rx.Component:
    return rx.container(
        rx.flex(
            navbar(),
            rx.box(
                table(),
                margin_left = Display.MEDIUN,
                margin_right = Display.MEDIUN),
            
            footer(),

            spacing="3",
            justify="center",
            align="center",
            direction="column",
        ),
        
    )
