import flet as ft
from ui import theme
from ui.state import state
from ui import instruments_config

class InstrumentConfig:
    def __init__(self):
        self.instrument_program_name = "Acoustic Grand Piano"
        self.velocity = 90
        self.delay = 0

chord_list = ft.ListView(spacing=10, auto_scroll=True, expand=True)

def refresh_chord_list():
    chord_list.controls.clear()

    for instrument in state.chord_instruments:
        chord_list.controls.append(
            instrument_card_ui(instrument)
        )

    chord_list.update()

def chord_instruments_ui():
    return ft.Container(
        #expand=True,
        bgcolor = theme.background_color,
        padding=10,
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#FCCF9F"
        ),

        shadow=ft.BoxShadow(
        blur_radius=3,
        color="#FCCF9F",
        offset=ft.Offset(0, 0),
        ),
        
        content= ft.Column(
            controls=[
                heading(),
                ft.Container(height=125, content=chord_list,),
                
            ]
        ),
    )

def instrument_card_ui(instrument_config):
    return ft.Row(
        controls=[
            ft.Container(content=music_icon()),
            ft.Container(width=2),
            ft.Container(expand=True, content=instrument_panel(instrument_config)),
            ft.Container(expand=True, content=velocity_panel(instrument_config)),
            ft.Container(expand = True, content=delay_panel(instrument_config)),
            ft.Container(alignment=ft.Alignment.CENTER, content=delete_button(instrument_config)),
            
        ]
    )

def delete_clicked(e, config):
    state.chord_instruments.remove(config)
    refresh_chord_list()
    pass

def delete_button(config):
    return ft.OutlinedButton(
        content=ft.Row(
        #spacing=8,
        height=40,
        # width=40,
        alignment=ft.Alignment.CENTER,
        controls=[
            ft.Icon(ft.Icons.DELETE_OUTLINE_OUTLINED, color="#F22B25", size=30),
            ],
        ),
        style=ft.ButtonStyle(
            bgcolor=theme.background_color,
            side=ft.BorderSide(width=0.5,color="#FCCF9F"),
            shape=ft.RoundedRectangleBorder(radius= 10),
        ),
        on_click=lambda e: delete_clicked(e, config)
    )


def delay_panel(instrument_config):
    return ft.Column(
        controls=[
            ft.Text("Delay (sec)", weight=ft.FontWeight.BOLD, color=theme.regular_text_color),
            delay_input(instrument_config)
        ]
        
    )
def delay_input(instrument_config):
    def onpressed(e):
        if e.control.value.isnumeric():
            print("delay chnaged")
            instrument_config.delay = e.control.value
    return ft.TextField(
        color="#0D1529",
        border_radius=10,
        value = str(instrument_config.delay),
        border_color="#CFCFCF",          # Normal border
        focused_border_color="#AFC1F8",  # Purple when focused
        cursor_color="#AFC1F8",
        on_change=onpressed,
        text_style=ft.TextStyle( weight=ft.FontWeight.BOLD)
    )



#velocity_value = ft.Text("90",weight=ft.FontWeight.BOLD, color="#0D1529")
def velocity_panel(instrument_config):
    velocity_value = ft.Text(
        value = str(instrument_config.velocity),
        weight=ft.FontWeight.BOLD,
        color="#0D1529",
    )

    def velocity_changed(e):
        velocity_value.value = str(int(e.control.value))
        instrument_config.velocity = int(e.control.value)
        e.page.update()

    slider = ft.Slider(
        value=instrument_config.velocity,
        min=0,
        max=127,
        divisions=127,
        expand=True,
        active_color="#FC8C18",
        on_change=velocity_changed,
    )
    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text(f"Velocity", weight=ft.FontWeight.BOLD, color=theme.regular_text_color),
                    velocity_value,
                ]
            ),
            slider,
        ]
    )
# def velocity_slider():
#     def velocity_changed(e):
#         velocity_value.value = str(int(e.control.value))
#         # velocity_value.update()

#     return ft.Slider(
#         value=90,
#         min=0,
#         max=127,
#         divisions=127,
#         expand = True,
#         on_change=velocity_changed
#     )

def instrument_panel(instrument_config):
    return ft.Column(
        controls=[
            ft.Text("Instrument", weight=ft.FontWeight.BOLD, color=theme.regular_text_color),
            instrument_dropdown(instrument_config)
        ]
    )
def instrument_dropdown(instrument_config):
    def instrument_changed(e):
        print("chord Instrument Changed")
        print(e.control.value)
        instrument_config.instrument_program_name = e.control.value

    dropdown = ft.Dropdown(
        value=instrument_config.instrument_program_name,
        #width=220,
        border_color="#CFCFCF",
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color="#0D1529"),
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#AFC1F8"
        ),
        options=[
            ft.dropdown.Option(name) for name in instruments_config.instrument_programs.keys()
        ],
        on_select=instrument_changed
    )
    # dropdown.on_change=instrument_changed
    return dropdown

def music_icon():
    return ft.Container(
        height=40,
        width=40,
        bgcolor="#FDF0E3",
        content=ft.Icon(icon=ft.Icons.PIANO, size=30, color="#FC8C18"),
        border_radius=10,
        border=ft.Border.all(
            width=0.5,
            color="#FCCF9F"
        ),
    )

def heading():
    return ft.Row(
        controls=[
            badge(2, "#FC8C18"),
            ft.Text(f"Chord Instruments", color="#FC8C18", weight=ft.FontWeight.BOLD),
            ft.Container(expand=True),
            add_instrumen_button(),
            confirm_button()
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

def add_instument_clicked():
    state.chord_instruments.append(InstrumentConfig())
    refresh_chord_list()

def add_instrumen_button():
    return ft.OutlinedButton(
        content=ft.Row(
        #spacing=8,
        #width=100,
        controls=[
            ft.Icon(ft.Icons.ADD, color="#FC8C18"),
            ft.Text("Add Instrument", color="#FC8C18"),
            ],
        ),
        style=ft.ButtonStyle(
            bgcolor="#FDF0E3",
            side=ft.BorderSide(width=0.5,color="#FCCF9F"),
            shape=ft.RoundedRectangleBorder(radius= 10),
        ),
        on_click=add_instument_clicked
    )

def confirm_clicked():
    state.confirmed_chord_instruments = []
    for config in state.chord_instruments:
        instrument_program_name = config.instrument_program_name
        velocity = config.velocity
        delay = config.delay
        instrument_program_no = instruments_config.instrument_programs[instrument_program_name]
        state.confirmed_chord_instruments.append([instrument_program_no, velocity, delay])
    print(state.confirmed_chord_instruments)

def confirm_button():
    return ft.OutlinedButton(
        content=ft.Row(
        #spacing=8,
        #width=100,
        controls=[
            ft.Icon(ft.Icons.CHECK, color="#6DB992"),
            ft.Text("Confirm", color="#6DB992"),
            ],
        ),
        style=ft.ButtonStyle(
            bgcolor="#EDF7F4",
            side=ft.BorderSide(width=0.5,color="#C4FFE0"),
            shape=ft.RoundedRectangleBorder(radius= 10),
        ),
        on_click=confirm_clicked
    )