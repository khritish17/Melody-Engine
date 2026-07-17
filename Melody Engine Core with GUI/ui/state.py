class AppState:
    def __init__(self):
        self.seed = 0
        self.tempo = 120
        self.measure_count = 8

        self.melody_instruments = []
        self.chord_instruments = []
        self.bass_instruments = []
state = AppState()