import config
import random
import sys

def octave_engine(seed, component):
    component = component.lower()
    if component not in ["melody", "chord", "bass"]:
        sys.stdout.errors("Error: invalid component provided...component should be either melody/chord/bass")
    
    octave_weights = {}
    if component == "melody":
        octave_weights = config.melody_octave_weights
    elif component == "chord":
        octave_weights = config.chord_octave_weights
    else:
        octave_weights = config.bass_octave_weights

    normalized_octave_weights = {}
    total_weight = 0
    for weights in octave_weights.values():
        total_weight += weights
    for octave, weight in octave_weights.items():
        normalized_octave_weights[octave] = weight/total_weight
    
    octave_ranges = {}
    initial_val = 0
    for oct, norm_weight in normalized_octave_weights.items():
        octave_ranges[oct] = [initial_val, initial_val + norm_weight]
        initial_val += norm_weight
    
    rng = random.Random(seed)
    r = rng.uniform(0, 1)
    for oct, val_range in octave_ranges.items():
        lf, rt = val_range
        if lf <= r <= rt:
            return oct

# print(octave_engine(seed=2, component="bass"))