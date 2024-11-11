import reflex as rx
from reflex.components.el import s
from pages.home import home
from pages.about import about
from rxconfig import config
from style.style import background


class State(rx.State):
    """The app state."""

    ...


app = rx.App(style=background)
app.add_page(home)
app.add_page(about)