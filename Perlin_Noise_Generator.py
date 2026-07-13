import noise
import random
#from matplotlib import pyplot as plt

class Perlin_Noise_Generator:
    def __int__(self):
        pass
    
    def perlin_noise(self, length, seed):
        output = []
        rng = random.Random(seed)
        start = rng.uniform(0.01, 1000)
        step = 0.05
        
        for _ in range(length):
            perlin_value = noise.pnoise1(start, base = seed) 
            normalized_value = round((perlin_value + 1)/2, 4)
            output.append(normalized_value)
            start += step
        return output

# P = Perlin_Noise_Generator()
# l = 200
# output = P.perlin_noise(l, seed=100)
# x = [i for i in range(1, l + 1)]
# ran = [random.uniform(0,1) for _ in range(l)]
# plt.plot(x, output, x, ran)
# plt.plot(x, output, "*", x, ran,"^")
# plt.show()