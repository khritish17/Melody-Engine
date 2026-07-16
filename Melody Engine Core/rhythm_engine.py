import config
import random

class rhythm_Engine:
    def __init__(self, seed, time_signature, perlin_noise):
        self.seed = seed
        self.rng = random.Random(self.seed)
        self.perlin_noise = perlin_noise
        self.i = 0
        self.beats_per_measure, _  = time_signature
    
    def next_rhythm(self):
        next_rhythm_slot = []
        beats_per_measure = self.beats_per_measure + 0
        while beats_per_measure > 0:
            initial_weight = config.rhythm_weights
            perlin_value = self.perlin_noise[self.i]
            self.i += 1
            total_weight_post_perlin_influence = 0

            # consider the perlin influence
            rhythm_perlin_influencer = config.rhythm_perlin_influencer
            for cls, influencer in rhythm_perlin_influencer.items():
                lf, rt, whole, half, quarter, eighth = influencer
                if lf <= perlin_value <= rt:
                    initial_weight[4] = initial_weight[4] * whole
                    initial_weight[2] = initial_weight[2] * half
                    initial_weight[1] = initial_weight[1] * quarter
                    initial_weight[0.5] = initial_weight[0.5] * eighth
                    
                    # eliminate non-eligible beats
                    if beats_per_measure - 4 < 0:
                        initial_weight[4] = 0
                    if beats_per_measure - 2 < 0:
                        initial_weight[2] = 0
                    if beats_per_measure - 1 < 0:
                        initial_weight[1] = 0
                    if beats_per_measure - 0.5 < 0:
                        initial_weight[0.5] = 0

                    total_weight_post_perlin_influence += initial_weight[4] + initial_weight[2] + initial_weight[1] + initial_weight[0.5]
                    break
                        

            # normalize the weight
            initial_weight[4] = initial_weight[4]/total_weight_post_perlin_influence
            initial_weight[2] = initial_weight[2]/total_weight_post_perlin_influence
            initial_weight[1] = initial_weight[1]/total_weight_post_perlin_influence
            initial_weight[0.5] = initial_weight[0.5]/total_weight_post_perlin_influence

            # create rhythm ranges : key = beat, value = range
            rytem_ranges = {}
            initial_value = 0
            for beat, wt in initial_weight.items():
                if wt > 0:
                    rytem_ranges[beat] = [initial_value, initial_value + wt]
                    initial_value += wt
            
            # random weights rhythm generation
            r = self.rng.uniform(0, 1)
            for beat, val_range in rytem_ranges.items():
                lf, rt = val_range
                if lf <= r < rt:
                    next_rhythm_slot.append(beat)
                    beats_per_measure -= beat
                    break
        return next_rhythm_slot


# RE = rhythm_Engine(seed=100000, time_signature=[4,4], perlin_noise=[0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542,0.124,0.157,0.489,0.542, 0.124,0.157,0.489,0.542])
# print(RE.next_rhythm())
# print(RE.next_rhythm())
# print(RE.next_rhythm())
# print(RE.next_rhythm())
# print(RE.next_rhythm())
# print(RE.next_rhythm())
# print(RE.next_rhythm())
# print(RE.next_rhythm())
                