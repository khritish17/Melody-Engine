import perlin_noise_generator as png
import key_generation as kgen
import config
import octave_engine


# The global seed value
seed = 220 


# Generate the base perlin noise
Noise = png.Perlin_Noise_Generator()
pnoise = Noise.perlin_noise(length = 100, seed = seed)

# Obtained the initial Key
key = kgen.key_gen(perlin_value=pnoise[0])

# Retrieve the note palette
note_palette = config.key_to_note_palette[key]

# Obtain the initial chord octave
initial_chord_octave = octave_engine.octave_engine(seed=seed, component="chord")
print(initial_chord_octave)
