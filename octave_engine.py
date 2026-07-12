import config
import random
import sys

class Octave_Engine:
    def __init__(self, seed, component):
        self.seed = seed
        self.component = component
        self.rng = random.Random(self.seed)
        
        if self.component not in ["melody", "chord", "bass"]:
            sys.stdout.errors("Error: invalid component provided...component should be either melody/chord/bass")
        
        self.octave_weights = {}
        if component == "melody":
            self.octave_weights = config.melody_octave_weights
        elif component == "chord":
            self.octave_weights = config.chord_octave_weights
        else:
            self.octave_weights = config.bass_octave_weights
    
    def next_octave(self):
        normalized_octave_weights = {}
        total_weight = 0
        for weights in self.octave_weights.values():
            total_weight += weights
        for octave, weight in self.octave_weights.items():
            normalized_octave_weights[octave] = weight/total_weight
        
        octave_ranges = {}
        initial_val = 0
        for oct, norm_weight in normalized_octave_weights.items():
            octave_ranges[oct] = [initial_val, initial_val + norm_weight]
            initial_val += norm_weight
        
        r = self.rng.uniform(0, 1)
        for oct, val_range in octave_ranges.items():
            lf, rt = val_range
            if lf <= r <= rt:
                return oct

# OE = Octave_Engine(seed=100, component="chord")
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())
# print(OE.next_octave())