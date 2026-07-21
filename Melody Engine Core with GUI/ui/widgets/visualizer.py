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
        content=ft.Column(
                controls=[heading(), audio_player(), card_tray()]
            )
    )

def heading():
    return ft.Row(
        controls=[
            badge(5, "#8885F6"),
            ft.Text(f"Live Visualizer & Playback", color="#8885F6", weight=ft.FontWeight.BOLD)
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

def card_tray():
    tempo = "--:--"
    current_measure = "--:--"
    total_measure = "--:--"
    beat = "--:--"
    return ft.Row(
        controls=[card(icon=ft.Icons.SPEED, icon_color="#27B27A", tag="BPM", value=tempo),
                  card(icon=ft.Icons.TIMER_OUTLINED, icon_color="#8232E9", tag="Time Signature", value="4/4"),
                  card(icon=ft.Icons.GRAPHIC_EQ, icon_color="#4699FC", tag="Measure", value=f"{current_measure}/{total_measure}"),
                  card(icon=ft.Icons.SEGMENT, icon_color="#F96902", tag="Beat", value=beat),
                  ]
    )

def card(icon, icon_color, tag, value):
    return ft.Container(
        alignment=ft.Alignment.CENTER,
        expand=True,
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
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                    ft.Icon(icon, color=icon_color), ft.Text(tag, color=theme.value_text_color)
                    ]),
                ft.Text(value, weight=ft.FontWeight.BOLD, color="#000000")
                ]
        )
    )

def audio_player():
    return ft.Container(
        expand=True,
        bgcolor="#0E162A",
        border_radius=10,
    )