import flet as ft
from ui import theme
from ui.state import state


def general_settings_ui():
    return ft.Container(
        #expand=True,
        bgcolor = theme.background_color,
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#AFC1F8"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#AFC1F8",
        offset=ft.Offset(0, 0),
        ),
        content=ft.Column(
            controls=[
                heading(),
                row1(),
                row2()

            ]
        )
    )

def heading():
    return ft.Row(
        controls=[
            badge(1, "#4E62F8"),
            ft.Text(f"Generation Settings", color="#4E62F8", weight=ft.FontWeight.BOLD)
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
def row2():
    return ft.Row(
        controls=[
            ft.Container(expand = True, content=key_panel()),
            ft.Container(width=8),
            ft.Container(expand = True, content=time_signature_panel()),
            
        ]
    )

def time_signature_panel():
    return ft.Column(
        controls=[
            ft.Text("Time Signature", weight=ft.FontWeight.BOLD, color=theme.value_text_color),
            time_signature_tag()
        ]
    )

def time_signature_tag():
    return ft.Container(
        alignment=ft.Alignment.CENTER_LEFT,
        #expand=True,
        bgcolor = theme.background_color,
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#AFC1F8"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#AFC1F8",
        offset=ft.Offset(0, 0),
        ),
        content=ft.Text(f"4/4", color="#0D1529", weight=ft.FontWeight.BOLD)
    )

def key_panel():
    return ft.Column(
        controls=[
            ft.Text("Key", weight=ft.FontWeight.BOLD, color=theme.regular_text_color),
            key_auto_tag(),
        ]
    )
def key_auto_tag():
    return ft.Container(
        alignment=ft.Alignment.CENTER_RIGHT,
        #expand=True,
        #bgcolor = theme.background_color,
        bgcolor="#EDF7F4",
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#AFC1F8"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#EDF7F4",
        offset=ft.Offset(0, 0),
        ),
        content=ft.Text(f"Auto", color="#6DB992", weight=ft.FontWeight.BOLD)
        
    )



def row1():
    return ft.Row(
        controls=[
            ft.Container(expand = True, content=seed_panel()),
            ft.Container(width=8),
            ft.Container(expand = True, content=tempo_panel()),
            ft.Container(width=8),
            ft.Container(expand = True, content=measure_panel()),
        ]
    )

def measure_panel():
    return ft.Column(
        controls=[
            ft.Text("Measure Count", weight=ft.FontWeight.BOLD, color=theme.regular_text_color),
            measure_input()
        ]
        
    )
def measure_input():
    def onpressed(f):
        if f.control.value.isnumeric():
            state.measure_count = int(f.control.value)
    return ft.TextField(
        border_radius=10,
        color="#0D1529",
        value = str(state.measure_count),
        border_color="#CFCFCF",          # Normal border
        focused_border_color="#AFC1F8",  # Purple when focused
        cursor_color="#AFC1F8",
        on_change=onpressed,
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)
    )




def tempo_panel():
    return ft.Column(
        controls=[
            ft.Text("Tempo (BPM)", weight=ft.FontWeight.BOLD, color=theme.regular_text_color),
            tempo_input()
        ]
        
    )
def tempo_input():
    def onpressed(e):
        if e.control.value.isnumeric():
            state.tempo = int(e.control.value)
    return ft.TextField(
        border_radius=10,
        color="#0D1529",
        value = str(state.tempo),
        border_color="#CFCFCF",          # Normal border
        focused_border_color="#AFC1F8",  # Purple when focused
        cursor_color="#AFC1F8",
        on_change=onpressed,
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD)
    )


def seed_panel():
    return ft.Column(
        controls=[
            ft.Text("Seed", weight=ft.FontWeight.BOLD, color=theme.regular_text_color),
            seed_input()
        ]
        
    )
def seed_input():
    def onpressed(e):
        if e.control.value.isnumeric():
            state.seed = int(e.control.value)
    return ft.TextField(
        color="#0D1529",
        border_radius=10,
        value = str(state.seed),
        border_color="#CFCFCF",          # Normal border
        focused_border_color="#AFC1F8",  # Purple when focused
        cursor_color="#AFC1F8",
        on_change=onpressed,
        text_style=ft.TextStyle( weight=ft.FontWeight.BOLD)
    )