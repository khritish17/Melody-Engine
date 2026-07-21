import flet as ft
from ui import theme
from ui.state import state
import music_generator

def generate_music_panel():
    return ft.Container(
        #expand = True,
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
            expand= True,
            controls=[
                ft.Row(expand=True, controls=[generate_music_button()]),
                ft.Row(expand = True, controls=[download_wav_button(), download_midi_button()])
            ]
        )
    )

def generate_music_clicked():
    print("Generating music")
    seed = state.seed
    tempo = state.tempo
    measure_count = state.measure_count
    melody_instruments = state.confirmed_melody_instruments
    chord_instruments= state.confirmed_chord_instruments
    bass_instruments= state.confirmed_bass_instruments
    
    MG = music_generator.Music_Generator(seed=seed, tempo=tempo, measure_count=measure_count)
    MG.configure_instruments(melody_instruments=melody_instruments,
                             chord_instruments=chord_instruments,
                             bass_instruments=bass_instruments)
    MG.generate_music()
    print(f"Seed: {seed}, Tempo: {tempo}, measure: {measure_count}")
    print(f"Melody:{melody_instruments}\nChord: {chord_instruments}\nbass:{bass_instruments}")
    print("Music Generated")

def generate_music_button():
    return ft.FilledButton(
        #width=1000,
        height=50,
        expand=True,
        bgcolor= "#863BF2",
        icon=ft.Icon(icon=ft.Icons.AUTO_AWESOME, color="#F2F2F2"),
        content= ft.Text("Generate Music",  color= "#F2F2F2",weight=ft.FontWeight.BOLD),
        style=ft.ButtonStyle( shape=ft.RoundedRectangleBorder(radius=10),),
        on_click=generate_music_clicked
    )

def download_wav_button():
    return ft.OutlinedButton(
        height=50,
        expand=True,
        #align=ft.Alignment.CENTER,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(ft.Icons.GRAPHIC_EQ, color="#32B97F"),
            ft.Text("Download WAV", color="#32B97F", weight=ft.FontWeight.BOLD),
            ],
        ),
        style=ft.ButtonStyle(
            bgcolor="#E1FCEE",
            side=ft.BorderSide(width=0.5,color="#6DB992"),
            shape=ft.RoundedRectangleBorder(radius= 10),
        ),
        #on_click=add_instument_clicked
    )

def download_midi_button():
    return ft.OutlinedButton(
        height=50,
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(ft.Icons.MUSIC_NOTE_ROUNDED, color="#2F98FC"),
            ft.Text("Download MIDI", color="#2F98FC", weight=ft.FontWeight.BOLD),
            ],
        ),
        style=ft.ButtonStyle(
            bgcolor="#F1F8FE",
            side=ft.BorderSide(width=0.5,color="#2F98FC"),
            shape=ft.RoundedRectangleBorder(radius= 10),
        ),
        #on_click=add_instument_clicked
    )