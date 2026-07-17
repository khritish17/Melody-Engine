import flet as ft
from ui import theme
from ui.widgets import general_settings, melody_instruments, chord_instruments, bass_instruments

def left_portion_ui():
    return ft.Container(
        #expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                general_settings.general_settings_ui(),
                melody_instruments.melody_instruments_ui(),
                chord_instruments.chord_instruments_ui(),
                bass_instruments.bass_instruments_ui(),
                ]
        )
    ) 
