key_to_noise_range = {"C": [0, 0.083], "G":[0.083, 0.167], "D":[0.167, 0.250],
                      "A":[0.250, 0.333],"E":[0.333, 0.417],"B":[0.417, 0.500],
                      "Am":[0.500, 0.583], "Em":[0.583, 0.667], "Bm":[0.667, 0.750],
                      "F#m":[0.750, 0.833], "C#m":[0.833, 0.917], "G#m":[0.917, 1.00] }

key_to_note_palette = {
    # Major
    "C":  ["C", "D", "E", "F", "G", "A", "B"],
    "G":  ["G", "A", "B", "C", "D", "E", "F#"],
    "D":  ["D", "E", "F#", "G", "A", "B", "C#"],
    "A":  ["A", "B", "C#", "D", "E", "F#", "G#"],
    "E":  ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "B":  ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "F"],
    "C#": ["C#", "D#", "F", "F#", "G#", "A#", "C"],

    "F":  ["F", "G", "A", "A#", "C", "D", "E"],
    "A#": ["A#", "C", "D", "D#", "F", "G", "A"],
    "D#": ["D#", "F", "G", "G#", "A#", "C", "D"],
    "G#": ["G#", "A#", "C", "C#", "D#", "F", "G"],
    
    # Natural Minor
    "Am":  ["A", "B", "C", "D", "E", "F", "G"],
    "Em":  ["E", "F#", "G", "A", "B", "C", "D"],
    "Bm":  ["B", "C#", "D", "E", "F#", "G", "A"],
    "F#m": ["F#", "G#", "A", "B", "C#", "D", "E"],
    "C#m": ["C#", "D#", "E", "F#", "G#", "A", "B"],
    "G#m": ["G#", "A#", "B", "C#", "D#", "E", "F#"],
    "D#m": ["D#", "F", "F#", "G#", "A#", "B", "C#"],
    "A#m": ["A#", "C", "C#", "D#", "F", "F#", "G#"],
    "Dm":  ["D", "E", "F", "G", "A", "A#", "C"],
    "Gm":  ["G", "A", "A#", "C", "D", "D#", "F"],
    "Cm":  ["C", "D", "D#", "F", "G", "G#", "A#"],
    "Fm":  ["F", "G", "G#", "A#", "C", "C#", "D#"],

    # diminished chords (only for chords)
    "Adim": ["A", "-", "C", "-", "D#", "-", "-"],
    "A#dim": ["A#", "-", "C#", "-", "E", "-", "-"],

    "Bdim": ["B", "-", "D", "-", "F", "-", "-"],
    "B#dim": ["B#", "-", "D#", "-", "F#", "-", "-"],

    "Cdim": ["C", "-", "D#", "-", "F#", "-", "-"],
    "C#dim": ["C#", "-", "E", "-", "G", "-", "-"],

    "Ddim": ["D", "-", "F", "-", "G#", "-", "-"],
    "D#dim": ["D#", "-", "F#", "-", "A", "-", "-"],

    "Edim": ["E", "-", "G", "-", "A#", "-", "-"],
    "E#dim": ["E#", "-", "G#", "-", "B", "-", "-"],

    "Fdim": ["F", "-", "G#", "-", "B", "-", "-"],
    "F#dim": ["F#", "-", "A", "-", "C", "-", "-"],

    "Gdim": ["G", "-", "A#", "-", "C#", "-", "-"],
    "G#dim": ["G#", "-", "B", "-", "D", "-", "-"],
}
melody_octave_weights = {4: 60, 5: 40}
chord_octave_weights = {3:70, 4: 30}
bass_octave_weights = {2: 80, 3: 20}

chord_weights = {1: ["", 30], 2: ["m", 7], 3:["m", 2], 4:["", 20],
                 5: ["", 25], 6: ["m", 15], 7: ["dim", 1]}
# chord_weights = {1: ["", 30], 2: ["m", 7], 3:["m", 2], 4:["", 20],
#                  5: ["", 25], 6: ["m", 16]}

rhythm_weights = {4: 5, 2:20, 1: 50, 0.5:25} # [key = beats, value = weight]  initial weights of the rhythm

# rhythm_perlin_influencer:  key = class, value = [perlin lf range, perlin rt range, whole X (4), half X (2), quarter X (1), eighth X (0.5)]
rhythm_perlin_influencer = {1: [0.00, 0.20, 2.0, 1.8, 0.9, 0.5],
                            2: [0.20, 0.40, 1.6, 1.4, 1.0, 0.8],
                            3: [0.40, 0.60, 1.0, 1.0, 1.0, 1.0],
                            4: [0.60, 0.80, 0.7, 0.9, 1.2, 1.4],
                            5: [0.80, 1.00, 0.4, 0.7, 0.3, 1.8]} 

# chord_influence_weights
chord_influence_meldoy_weights = {0: 50, 2:30, 4:20} # root (0 index) = 50, third(2 index) = 30, fifth (4 index) = 20

# melody_movement_weights
melody_movements_weights = {-3: [-1, -0.18, 2], -2:[-0.18, -0.10, 10], -1:[-0.10, -0.03, 25],
                            0:[-0.03, 0.03, 10],
                            1:[0.03, 0.10, 35], 2:[0.10, 0.18, 15], 3:[0.18, 1, 3]}

# melody_perlin_multiplier
melody_perlin_multiplier = {
    "preferred" : 1.5,
    "related": 1.2,
    "opposite":0.6}

# melody chord multiplier
melody_chord_multiplier = {
    "root": 1.3,
    "third": 1.2,
    "fifth": 1.1 }

note_to_semitone = {
    "C":0,
    "C#":1,
    "D":2,
    "D#":3,
    "E":4,
    "F":5,
    "F#":6,
    "G":7,
    "G#":8,
    "A":9,
    "A#":10,
    "B":11
}