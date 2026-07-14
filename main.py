import perlin_noise_generator as png
import key_generation as kgen
import config
import octave_engine
import chord_engine
import rhythm_engine
import melody_engine


# The global seed value
seed = 1 

# Time Signature
time_sginature = [4,4] # time signature = 4/4

# Tempo = Beats per minute
tempo = 120

# Measure count
measure_count = 10

# each measure can contain time_signature[0] beats and each time_signature[0] in worst can be filled by 'time_signature[0]/0.5' eighth beat
base_perlin_length = measure_count * time_sginature[0] * 2 

# Generate the base perlin noise
Noise = png.Perlin_Noise_Generator()
pnoise = Noise.perlin_noise(length = base_perlin_length, seed = seed)

# Obtained the initial Key
key = kgen.key_gen(perlin_value=pnoise[0])

# Retrieve the note palette
note_palette = config.key_to_note_palette[key]

# Initialise chord octave engine
OCE = octave_engine.Octave_Engine(seed=seed, component="chord")


# Initialise melody octave engine
OME = octave_engine.Octave_Engine(seed=seed, component="melody")

# Obtain the initial chord
CE = chord_engine.Chord_Engine(seed=seed, note_palette=note_palette)


# Obtain the rhythm
RE = rhythm_engine.rhythm_Engine(seed=seed, time_signature=time_sginature, perlin_noise=pnoise)

# Initialise the melody engine
ME = melody_engine.Melody_Engine(seed=seed, note_palette=note_palette)

melody_track = [] # [[note, octave, duration in seconds]]
chord_track = [] # [[root note, third note, fifth note, octave, duration in seconds]]
for measure in range(measure_count):
    current_chord = CE.next_chord()
    chord_octave = OCE.next_octave()
    current_rhythm = RE.next_rhythm() # its an list of beats e.g [2, 1, 1] or [4] or [2, 1, 0.5, 0.5] ...
    total_duration = 0
    for i in range(len(current_rhythm)):
        if measure == 0 and i == 0:
            # the very first melody note
            note = ME.first_melody()
            melody_octave = OME.next_octave()
            duration = current_rhythm[i] * (60/tempo)
            total_duration += duration
            melody_track.append([note, melody_octave, duration])
        else:
            # subsequent notes
            pass
    chord_note_palette = config.key_to_note_palette[current_chord]
    root_note, third_note, fifth_note = chord_note_palette[0], chord_note_palette[2], chord_note_palette[4] 
    chord_track.append([root_note, third_note, fifth_note, chord_octave, total_duration])

print(melody_track)
print(chord_track)
    





