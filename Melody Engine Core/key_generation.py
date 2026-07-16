import config

def key_gen(perlin_value):
    key_to_noise_range = config.key_to_noise_range
    for key, noise_range in key_to_noise_range.items():
        l, r = noise_range
        # print(f"{key}, [{l},{r}]")
        if l <= perlin_value <= r:
            return key

# print(key_gen(perlin_value=0.418))