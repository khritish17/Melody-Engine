import config
import random

class Chord_Engine:
    def __init__(self, seed, note_palette):
        self.seed = seed
        self.rng = random.Random(seed)
        self.note_palette = note_palette
    
    def next_chord(self):
        chord_weights = config.chord_weights
        normalized_chord_weight = {}
        i = 0
        for deg, chord_wt in chord_weights.items():
            chord, wt = chord_wt
            normalized_chord_weight[f"{self.note_palette[i]}{chord}"] = wt/100
            i += 1
        
        chord_ranges = {}
        initial_value = 0
        for chord, norm_wt in normalized_chord_weight.items():
            chord_ranges[chord] = [initial_value, initial_value + norm_wt]
            initial_value += norm_wt
        
        r = self.rng.uniform(0,1)

        for chord, val_range in chord_ranges.items():
            lf, rt = val_range
            if lf <= r <= rt:
                return chord

# CE = Chord_Engine(seed=100, note_palette=['C','D','E','F','G', 'A', 'B'])
# print(CE.next_chord())
# print(CE.next_chord())
# print(CE.next_chord())
# print(CE.next_chord())
# print(CE.next_chord())
# print(CE.next_chord())
# print(CE.next_chord())
# print(CE.next_chord())
# print(CE.next_chord())