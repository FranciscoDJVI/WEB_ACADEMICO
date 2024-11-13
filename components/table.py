import reflex as rx

class State(rx.State):
    data: list = [
        ["Trabajos escritos", "$10.000"],
        ["Ensayos", "$8.000"],
        ["Consultas", "$5.000"],
        ["Impresiones B/N", "$300"],
        ["Impresiones a color", "$500"],
        ["Fotocopias", "$100"],
        ["Scanners", "$500"],
    ]
    columns: list[str] = ["Servicios", "Precios"]


def table()->rx.Component:
    return rx.data_table(
        data=State.data,
        columns=State.columns,
        search=True,
        sort=True,
        resizable=True,
    )
