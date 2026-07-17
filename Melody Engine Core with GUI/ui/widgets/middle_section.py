import flet as ft
from ui import theme
from ui.widgets import left_portion

def middle_section_ui():
    return ft.Container(
        expand=True,
        content=ft.Row(
            #alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                # left portion of the middle section
                ft.Container(
                    expand = True,
                    content = left_portion.left_portion_ui()
                ),
                ft.Container(width = 10),
                # right portion of the middle section
                ft.Container(
                    expand = True,
                    content = left_portion.left_portion_ui()
                ),
                #ft.Text("Right portion", color=theme.regular_text_color),
            ]
        )
    )