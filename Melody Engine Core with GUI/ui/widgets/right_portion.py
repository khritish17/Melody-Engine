import flet as ft
from ui import theme
def right_portion_ui():
    return ft.Container(
        #expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Live Visualizer pannel"),
                ft.Text("Generate Button pannel")
                ]
        )
    ) 
