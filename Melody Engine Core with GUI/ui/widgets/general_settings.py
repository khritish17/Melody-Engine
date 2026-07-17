import flet as ft
from ui import theme


def general_settings_ui():
    return ft.Container(
        #expand=True,
        bgcolor = theme.background_color,
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#AFC1F8"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#AFC1F8",
        offset=ft.Offset(0, 0),
        ),
        content=heading()
    )

def heading():
    return ft.Row(
        controls=[
            badge(1, "#4E62F8"),
            ft.Text(f"Generation Settings", color="#4E62F8", weight=ft.FontWeight.BOLD)
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