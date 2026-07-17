import flet as ft
from ui import theme


def melody_instruments_ui():
    return ft.Container(
        #expand=True,
        bgcolor = theme.background_color,
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#FEB2D5"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#FEB2D5",
        offset=ft.Offset(0, 0),
        ),
        content=heading()
    )

def heading():
    return ft.Row(
        controls=[
            badge(2, "#ED41A1"),
            ft.Text(f"Melody Instruments", color="#ED41A1", weight=ft.FontWeight.BOLD)
        ]
    )

def badge(number, color):
    return ft.Container(
        alignment=ft.Alignment.CENTER,
        bgcolor=color,
        height=30,
        width=30,
        border_radius=5,
        content=ft.Text(f"{number}", color=theme.background_color, weight=ft.FontWeight.BOLD), 
    )