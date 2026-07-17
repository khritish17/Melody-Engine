import flet as ft
from ui import theme


def footer_ui():
    return ft.Row(
        controls=[
            ft.Container(
                expand = True,
                content = ft.Row(
                    controls = [
                            ft.Icon(
                                ft.Icons.FAVORITE,
                                size=18,
                                color="#FF0076",),
                            ft.Text("Made with passion for Music", 
                                size=13, 
                                weight=ft.FontWeight.W_600, 
                                color=theme.regular_text_color,),
                    ]
                )
            ),
            ft.Container(
                expand = True,
                content = ft.Row(
                    controls = [
                            ft.Icon(
                                ft.Icons.HEADPHONES,
                                size=18,
                                color="#8A6CFF",),
                            ft.Text("Use headphones for the best experience", 
                                size=13, 
                                weight=ft.FontWeight.W_600, 
                                color=theme.regular_text_color,),
                    ]
                )
            ),
            ft.Container(
                content = ft.Text("v1.0.0", 
                                size=13, 
                                weight=ft.FontWeight.W_600, 
                                color="#42BC8A",)
            ),
        ]
    )