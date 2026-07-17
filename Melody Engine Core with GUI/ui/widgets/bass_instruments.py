import flet as ft
from ui import theme


def bass_instruments_ui():
    return ft.Container(
        #expand=True,
        bgcolor = theme.background_color,
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#6DB992"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#6DB992",
        offset=ft.Offset(0, 0),
        ),
        content=heading()
    )

def heading():
    return ft.Row(
        controls=[
            badge(4, "#32B97F"),
            ft.Text(f"Bass Instruments", color="#32B97F", weight=ft.FontWeight.BOLD)
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