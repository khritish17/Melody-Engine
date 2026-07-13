import perlin_noise_generator as png
import key_generation as kgen
import config
import octave_engine
import chord_engine
import rhythm_engine


# The global seed value
seed = 1205 

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

# Obtain the initial chord octave
OE = octave_engine.Octave_Engine(seed=seed, component="chord")
initial_chord_octave = OE.next_octave()



# Obtain the initial chord
CE = chord_engine.Chord_Engine(seed=seed, note_palette=note_palette)


# Obtain the rhythm
RE = rhythm_engine.rhythm_Engine(seed=seed, time_signature=time_sginature, perlin_noise=pnoise)

for measure in range(measure_count):
    current_chord = CE.next_chord()
    current_rhythm = RE.next_rhythm() # its an list of beats e.g [2, 1, 1] or [4] or [2, 1, 0.5, 0.5] ...

