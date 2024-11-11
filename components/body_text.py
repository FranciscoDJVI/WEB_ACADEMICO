import reflex as rx
from utils.constants import FontSize
from style.style import body_text_style

def body_text(text: str)->rx.Component:
    return rx.text(
        text,
        font_size=FontSize.SMALL,
        margin="10px", 
        style=body_text_style
    )