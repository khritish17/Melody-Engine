import flet as ft
from ui import theme

from ui.widgets import generate_music_panel, visualizer
def right_portion_ui():
    return ft.Container(
        #expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                visualizer.visualizer_panel(),
                generate_music_panel.generate_music_panel()
                ]
        )
    ) 
