import perlin_noise_generator as png
import key_generation as kgen
import config

# Generate the base perlin noise
Noise = png.Perlin_Noise_Generator()
pnoise = Noise.perlin_noise(length = 100, seed = 220)

# Obtained the initial Key
key = kgen.key_gen(perlin_value=pnoise[0])

# Retrieve the note palette
note_palette = config.key_to_note_palette[key]

print(key)
print(note_palette)
