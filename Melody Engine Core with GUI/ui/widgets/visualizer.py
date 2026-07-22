import flet as ft
from ui import theme
import random
import vlc
import time
import os
import asyncio
from ui.state import state

page_ref = None

path = os.path.abspath("output/song.wav")

player = vlc.MediaPlayer(path)
playback_running = False

async def playback_loop():
    global playback_running

    playback_running = True

    while playback_running:

        state = player.get_state()

        if state == vlc.State.Playing:
            update_playback()
            animate_visualizer()

        elif state == vlc.State.Ended:
            play_button.icon = ft.Icons.REPLAY_ROUNDED
            page_ref.update()
            break

        page_ref.update()
        await asyncio.sleep(0.1)

    playback_running = False



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
    tempo = str(state.tempo)
    return ft.Row(
        controls=[card(icon=ft.Icons.SPEED, icon_color="#27B27A", tag="BPM", value_control=ft.Text(tempo, weight=ft.FontWeight.BOLD, color="#000000")),
                  card(icon=ft.Icons.TIMER_OUTLINED, icon_color="#8232E9", tag="Time Signature", value_control=ft.Text("4/4", weight=ft.FontWeight.BOLD, color="#000000")),
                  measure_card,
                  beat_card,
                  ]
    )


def card(icon, icon_color, tag, value_control):
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
                value_control,
                # ft.Text(value, weight=ft.FontWeight.BOLD, color="#000000")
                ]
        )
    )
current_measure = "--:--"
total_measure = "--:--"
beat = "--:--"
measure_text = ft.Text("--/--", weight=ft.FontWeight.BOLD, color="#000000")
beat_text = ft.Text("--", weight=ft.FontWeight.BOLD, color="#000000")
measure_card = card(icon=ft.Icons.GRAPHIC_EQ, icon_color="#4699FC", tag="Measure", value_control=measure_text)
beat_card = card(icon=ft.Icons.SEGMENT, icon_color="#F96902", tag="Beat", value_control=beat_text)


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
            visualizer_row,
            ft.Container(height=30),
            audio_time_line_tray(),
            audio_buttons_tray(),
        ]
    )

def play_button_clicked(e):
    state = player.get_state()

    if state == vlc.State.Ended:
        player.stop()          
        player.play()  
        play_button.icon = ft.Icons.REPLAY_ROUNDED       
        
    elif player.is_playing():
        player.pause()
        play_button.icon = ft.Icons.PLAY_ARROW
    else:
        player.play()
        play_button.icon = ft.Icons.PAUSE
        if not playback_running:
            if not playback_running:
                page_ref.run_task(playback_loop)

    e.page.update()

play_button = ft.IconButton(icon=ft.Icons.PLAY_ARROW, icon_color="white", bgcolor="#5D64F8", icon_size=20,on_click=play_button_clicked)

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


ellapsed_time = "--:--"
total_time = "--:--"

progress_slider = ft.Slider(expand=True, value = 0, min=0, max = 0, divisions=1000, active_color="#5D64F8")
def ms_sec_str(ms):
    total_sec = ms//1000
    min = total_sec//60
    sec = total_sec % 60
    return f"{min}:{sec}"

def update_playback():
    global ellapsed_time
    global total_time

    current_ms = player.get_time()
    total_ms = player.get_length()

    if total_ms <= 0:
        return

    progress_slider.max = total_ms
    progress_slider.value = current_ms

    ellapsed_text.value = ms_sec_str(current_ms)
    total_text.value = ms_sec_str(total_ms)

    sec_per_beat = 60 / state.tempo
    sec_per_measure = 4 * sec_per_beat
    current_sec = current_ms / 1000
    measure = int(current_sec / sec_per_measure) + 1
    beat = int((current_sec % sec_per_measure) / sec_per_beat) + 1

    measure_text.value = f"{measure}/{state.measure_count}"
    beat_text.value = str(beat)
    

ellapsed_text = ft.Text(ellapsed_time)
total_text = ft.Text(total_time)
def audio_time_line_tray():
    return ft.Container(
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(padding=0, height=20, 
                             content=progress_slider,
                             ),
                ft.Container(padding=ft.Padding.symmetric(horizontal=15),content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ellapsed_text,
                        total_text]
                )),
                
            ],
        )
    )

bars = []
colors = [
    "#EC2F7F", "#EF327F", "#F13388", "#F33690", "#F53896",
    "#F63B9D", "#F73FA5", "#F543AD", "#F245B5", "#F34CC5",
    "#F15DF1", "#EC64F5", "#E56AF8", "#DC6BFB", "#D26CFE",
    "#C96EFF", "#C171FF", "#B874FF", "#AE75FE", "#A276FC",
    "#9370F8", "#866FF5", "#7971F3", "#6C76F4", "#677CF5",
    "#5F83F8", "#568AFA", "#4C92FC", "#4299FD", "#339EFE",
    "#26A5F8", "#18ACEF", "#0BAAEB", "#08B9EC", "#07C8F0",
    "#07D5F3", "#08E5F7", "#0EF8F8", "#1CDDD8", "#34D8CE",
    "#4BD6BA", "#62E98A", "#78F05B", "#9AF255", "#B8F353",
    "#D2F04C", "#E8EA43", "#F4D93A", "#F6B92F", "#FF8A31"
]

def animate_visualizer():
    for bar in bars:
        bar.height = random.randint(40, 150)




def create_visualizer():
    bars.clear()

    for color in colors:
        bars.append(
            ft.Container(
                expand=True,
                height=random.randint(60, 150),
                border_radius=5,
                bgcolor=color,
                animate=ft.Animation(100, ft.AnimationCurve.EASE_OUT),
                shadow=ft.BoxShadow(
                    blur_radius=8,
                    color=color,
                ),
            )
        )
create_visualizer()
visualizer_row = ft.Container(expand = True,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.END,
                        spacing=3,
                        controls=bars,)
                        )