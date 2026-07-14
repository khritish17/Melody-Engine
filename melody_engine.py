import config
import random

class Melody_Engine:
    def __init__(self, seed, note_palette):
        self.seed = seed
        self.note_palette = note_palette
        self.chord_weights = config.chord_influence_meldoy_weights
        self.rng = random.Random(self.seed)
    
    def first_melody(self):
        normalized_chord_weights = {}
        for chord_tone, weight in self.chord_weights.items():
            normalized_chord_weights[self.note_palette[chord_tone]] = weight/100
        
        chord_influence_range = {}
        initial_value = 0
        for chord_tone, weight in normalized_chord_weights.items():
            chord_influence_range[chord_tone] = [initial_value, initial_value + weight]
            initial_value += weight
        
        r = self.rng.uniform(0, 1)
        for chord_tone, val_range in chord_influence_range.items():
            lf, rt = val_range
            if lf <= r <= rt:
                return chord_tone
    def map_movement(self, movement, current_melody_note, note_palette, current_octave):
        index = note_palette.index(current_melody_note)
        new_index = index + movement
        next_octave = current_octave
        l = len(note_palette)
        next_melody_note = note_palette[new_index % l ]
        if  new_index >= len(note_palette):
            next_octave = current_octave + 1
        elif new_index < 0:
            next_octave = current_octave - 1
        
        if next_octave > 5:
            next_octave = 4
        elif next_octave < 4:
            next_octave = 5 
        return [next_melody_note, next_octave]

        
    
    def next_melody(self, delta, current_melody_note, current_octave, current_chord, note_palette):
        # convert the general melody movement weigths to melody-note-movements-weights
        melody_movements_weights = config.melody_movements_weights
        melody_note_movements_weight = {}
        next_octave = current_octave
        exact_prefered_movement = 0 
        for movement, influence in melody_movements_weights.items():
            lf, rt, weight = influence
            next_melody_note, next_octave = self.map_movement(movement=movement, current_melody_note=current_melody_note, 
                                                              note_palette=note_palette, current_octave=current_octave)
            melody_note_movements_weight[(next_melody_note, next_octave, movement)] = [lf, rt, weight]

            if lf <= delta <= rt:
                exact_prefered_movement = movement
        #------------------------------------------------------------------------------------
        # perlin dirction influence
        melody_perlin_multiplier = config.melody_perlin_multiplier
        for k, v in melody_note_movements_weight.items():
            next_melody_, next_octave, movement = k
            lf, rt, weight = v
            if exact_prefered_movement != 0:
                if exact_prefered_movement * movement >= 0:
                    # both movement and exact_prefered_movement are of same sign
                    if exact_prefered_movement == movement:
                        weight *= melody_perlin_multiplier["preferred"]
                    else:
                        weight *= melody_perlin_multiplier["related"]
                else:
                    # both movement and exact_prefered_movement are of opposite sign
                    weight *= melody_perlin_multiplier["opposite"]
            else:
                # exact_prefered_movement = 0
                if movement == exact_prefered_movement:
                    weight *= melody_perlin_multiplier["preferred"]
                elif movement < exact_prefered_movement:
                    weight *= melody_perlin_multiplier["opposite"]
                elif movement > exact_prefered_movement:
                    weight *= melody_perlin_multiplier["related"]
            melody_note_movements_weight[next_melody_, next_octave, movement] = [lf, rt, weight]
        # --------------------------------------------------------------------------------
        # chord influence
        chord_note_palette = config.key_to_note_palette[current_chord]
        root, third, fifth = chord_note_palette[0], chord_note_palette[2], chord_note_palette[4]
        melody_chord_multiplier = config.melody_chord_multiplier
        for k, v in melody_note_movements_weight.items():
            next_melody_, next_octave, movement = k
            lf, rt, weight = v
            if next_melody_ == root:
                weight *= melody_chord_multiplier["root"]
            elif next_melody_ == third:
                weight *= melody_chord_multiplier["third"]
            elif next_melody_ == fifth:
                weight *= melody_chord_multiplier["fifth"]
            melody_note_movements_weight[(next_melody_, next_octave, movement)] = [lf, rt, weight]
        # -------------------------------------------------------------------------------------------------
        # Normalize the melody_note_movements_weight
        normalized_note_movements = {}
        total_weight = 0
        for k, v in melody_note_movements_weight.items():
            next_melody_, next_octave, movement = k
            lf, rt, weight = v
            normalized_note_movements[(next_melody_, next_octave)] = weight
            total_weight += weight
        
        for next_note_octave, wt in normalized_note_movements.items():
            normalized_note_movements[next_note_octave] = wt/total_weight
        
        # normalized_range_assignment
        normalized_range = {}
        initial_value = 0
        for next_note_octave, weight in normalized_note_movements.items():
            normalized_range[next_note_octave] = [initial_value, initial_value + weight]
            initial_value += weight

        # random selection based on probabilities
        r = self.rng.uniform(0,1)
        for next_note_octave, val_range in normalized_range.items():
            lf, rt = val_range
            if lf <= r <= rt:
                return next_note_octave








# ME = Melody_Engine(seed=1000, note_palette=['C','D','E','F','G', 'A', 'B'])
# # print(ME.first_melody())
# print(ME.next_melody(0.1, current_melody_note="E", current_octave=4, current_chord="C", note_palette=['C','D','E','F','G', 'A', 'B']))