import reflex as rx
from utils.constants import FontSize
from utils.constants import Display
from utils.constants import Border
from utils.constants import FontFamily


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"),
        href=url,
        color="#b3b6b7",
        font_family=FontFamily.CURSIVE,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.webp",
                        width=Display.VERY_SMALL,
                        height=Display.VERY_SMALL,
                        margin="10px",
                        border_radius=Border.MAXIMUN,
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("Acerca de y precios ", "/about"),
                    justify="end",
                    spacing="3",
                    margin_right=Display.SMALL,
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.webp",
                        width=Display.SMALL,
                        height=Display.SMALL,
                        margin="10px",
                        border_radius=Border.MAXIMUN,
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Inicio"),
                        rx.menu.item("Acerca de y precios"),
                    ),
                    justify="end",
                    margin_right=Display.SMALL,
                ),
                justify="between",
                align_items="center",
            ),
        ),
        padding="auto",
        width="100%",
    )
