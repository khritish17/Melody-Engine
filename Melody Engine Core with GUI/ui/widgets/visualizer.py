import flet as ft
from ui import theme

def visualizer_panel():
    return ft.Container(
        expand = True,
         bgcolor = theme.background_color,
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#E9E9EA"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#E9E9EA",
        offset=ft.Offset(0, 0),
        ),
    )