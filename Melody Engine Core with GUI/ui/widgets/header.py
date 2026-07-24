import flet as ft
from ui import theme


def header_ui():
    return ft.Row(
        controls=[
            ft.Container(expand=True, content=title_design(),),
            ft.Container(expand=True,
                         content=ft.Row(
                            controls=[
                                information_design()
                                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                ),
            ),
            ft.Container( expand=True,
                        content=ft.Row(
                            controls=[
                                about_section()
                                ],
                        alignment=ft.MainAxisAlignment.END,
                ),
            ),
        ]
    )


def title_design():
    return ft.Row(
        spacing=12,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(
                ft.Icons.MUSIC_NOTE_ROUNDED,
                size=55,
                color="#AC38EB",
            ),
            ft.Column(
                spacing=2,
                controls=[
                    ft.Text(
                        "Melody Engine",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=theme.title_text_color,
                    ),
                    ft.Text(
                        "Procedural Music Generator | © Diagonals.lab 2026",
                        size=13,
                        weight=ft.FontWeight.W_600,
                        color=theme.regular_text_color,
                    ),
                ],
            ),
        ],
    )

status_text = ft.Text(
                "Waiting",
                size=15,
                weight=ft.FontWeight.BOLD,
                color=theme.regular_text_color,
            )
status_icon = ft.Icon(
                ft.Icons.CIRCLE,
                size=10,
                color="#FF0579",
            )
def information_design():
    return ft.Row(
        spacing=8,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(
                ft.Icons.AUTO_AWESOME,
                size=18,
                color="#AC38EB",
            ),
            ft.Text(
                "Perlin Noise",
                size=15,
                weight=ft.FontWeight.BOLD,
                color=theme.regular_text_color,
            ),
            ft.Container(width=7),
            ft.Icon(
                ft.Icons.RADIO_BUTTON_CHECKED_OUTLINED,
                size=18,
                color="#8A6CFF",
            ),
            ft.Text(
                "Procedural",
                size=15,
                weight=ft.FontWeight.BOLD,
                color=theme.regular_text_color,
            ),
            ft.Container(width=7),

            status_icon,
            status_text,
        ],
    )


def about_section():
    img_width = 180
    img_height = int((507/1636)*img_width) 
    return ft.Row(
        spacing=6,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Image(src="assets/img/diagonals.png",height=img_height, width=img_width), # h/v = 1636/507
        ],
    )