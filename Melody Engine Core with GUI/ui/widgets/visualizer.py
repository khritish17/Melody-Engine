import flet as ft
from ui import theme
import random

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
        padding=15,
        content=audio_panel(),
    )

def audio_panel():
    return ft.Column(
        controls=[
            visualizer(),
            ft.Container(height=30),
            audio_time_line_tray(),
            audio_buttons_tray(),
        ]
    )



play_button = ft.IconButton(icon=ft.Icons.PLAY_ARROW, icon_color="white", bgcolor="#5D64F8", icon_size=20,)

def audio_buttons_tray():
    return ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(width=10),
                play_button,
                ft.Container(width=20),
                ft.Icon(icon=ft.Icons.VOLUME_UP),
                ft.Container(padding=0, content=ft.Slider(value = 60, min=0, max = 100, divisions=100, active_color="#5D64F8",width=150),),
            ]
        )
    )

total_time = "01:36"
ellapsed_time = "00:55"
def audio_time_line_tray():
    t_time = total_time.split(":")
    e_time = ellapsed_time.split(":")
    total_time_sec = (int(t_time[0]) * 60) + int(t_time[1])
    ellapsed_time_sec = (int(e_time[0]) * 60) + int(e_time[1])
    return ft.Container(
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(padding=0, height=20, 
                             content=ft.Slider(expand=True, value = ellapsed_time_sec, min=0, max = total_time_sec, divisions=1000, active_color="#5D64F8"),
                             ),
                ft.Container(padding=ft.Padding.symmetric(horizontal=15),content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(ellapsed_time),
                        ft.Text(total_time)]
                )),
                
            ],
        )
    )

bars = []
colors = [
    "#EC2F7F", "#F13388", "#F53896", "#F73FA5",
    "#F245B5", "#F15DF1", "#E96AF8", "#D96BFC",
    "#C96EFF", "#BD6CFF", "#A876FF", "#9370F8",
    "#7E73F3", "#677CF5", "#5887FA", "#4993FD",
    "#339EFE", "#1EA8F5", "#0BAAEB", "#08BCEB",
    "#07D5F3", "#07FAF8", "#19E8DD", "#34D8CE",
    "#53D5A7", "#69EF5D", "#8AF158", "#A8F354",
    "#C5F354", "#DFED47", "#F4E73C", "#F6C934",
    "#F5A22C", "#FF8531", "#FF673D", "#F23E5D"
]
def change_animation():
    for i in range(len(colors)):
        bars.append(ft.Container(expand=True, height=random.randint(60, 150), border_radius=5, bgcolor=colors[i], 
                                shadow=ft.BoxShadow(
                                    blur_radius=8,
                                    color=colors[i],)
                                )
                    )

def visualizer():
    change_animation()
    return ft.Container(expand = True,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.END,
                            spacing=3,
                            controls=bars,)
                            )