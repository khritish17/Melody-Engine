import perlin_noise_generator
import key_generation as kgen
import config
import octave_engine
import chord_engine
import rhythm_engine
import melody_engine
import midi_generation
import synthesizer

class Music_Generator:
    def __init__(self, seed, tempo, measure_count):
        self.seed = seed
        self.midi_file = "output/song.mid"
        self.soundfont = "assets/soundfonts/GeneralUser-GS/GeneralUser-GS.sf2"
        self.wav_file = "output/song.wav"
        self.tempo = tempo
        self.measure_count = measure_count
        self.time_sginature = [4,4]
    
    def configure_instruments(self, melody_instruments, chord_instruments, bass_instruments):
        self.melody_instruments = melody_instruments # melody instruments [[instrument_program, velocity, start_time]]
        self.chord_instruments = chord_instruments # chord instruments [[instrument_program, velocity, start_time]]
        self.bass_instruments = bass_instruments # bass instruments [[instrument_program, velocity, start_time]]
    
    def generate_music(self):
        # each measure can contain time_signature[0] beats and each time_signature[0] in worst can be filled by 'time_signature[0]/0.5' eighth beat
        base_perlin_length = self.measure_count * self.time_sginature[0] * 2 
        
        # Generate the base perlin noise
        Noise = perlin_noise_generator.Perlin_Noise_Generator()
        pnoise = Noise.perlin_noise(length = base_perlin_length, seed = self.seed)

        # Obtained the initial Key
        key = kgen.key_gen(perlin_value=pnoise[0])

        # Retrieve the note palette
        note_palette = config.key_to_note_palette[key]

        # Initialise the Octave engine for melody, chord, bass
        OCE = octave_engine.Octave_Engine(seed=self.seed, component="chord")
        OME = octave_engine.Octave_Engine(seed=self.seed, component="melody")
        OBE = octave_engine.Octave_Engine(seed=self.seed, component="bass")

        # Initialise the Core Engines (Chord, Rythem, Melody)
        CE = chord_engine.Chord_Engine(seed=self.seed, note_palette=note_palette)
        RE = rhythm_engine.rhythm_Engine(seed=self.seed, time_signature=self.time_sginature, perlin_noise=pnoise)
        ME = melody_engine.Melody_Engine(seed=self.seed, note_palette=note_palette)

        # Track generation
        melody_track = [] # [[note, octave, duration in seconds]]
        chord_track = [] # [[root note, third note, fifth note, octave, duration in seconds]]
        bass_track = [] # [[root note, octave, duration in seconds]]
        pn_index = 1
        melody_note = ""
        melody_octave = 4
        for measure in range(self.measure_count):
            current_chord = CE.next_chord()
            chord_octave = OCE.next_octave()
            current_rhythm = RE.next_rhythm() # its an list of beats e.g [2, 1, 1] or [4] or [2, 1, 0.5, 0.5] ...
            total_duration = 0
            for i in range(len(current_rhythm)):
                if measure == 0 and i == 0:
                    # the very first melody note
                    melody_note = ME.first_melody()
                    melody_octave = OME.next_octave()
                    duration = current_rhythm[i] * (60/self.tempo)
                    total_duration += duration
                    melody_track.append([melody_note, melody_octave, duration])
                else:
                    # subsequent notes
                    if pn_index == len(pnoise):
                        break
                    delta = pnoise[pn_index] - pnoise[pn_index - 1]
                    melody_note, melody_octave = ME.next_melody(delta=delta, current_melody_note=melody_note, 
                                                                current_octave=melody_octave, current_chord=current_chord, note_palette=note_palette)
                    duration = current_rhythm[i] * (60/self.tempo)
                    total_duration += duration
                    melody_track.append([melody_note, melody_octave, duration])
            chord_note_palette = config.key_to_note_palette[current_chord]
            root_note, third_note, fifth_note = chord_note_palette[0], chord_note_palette[2], chord_note_palette[4] 
            chord_track.append([root_note, third_note, fifth_note, chord_octave, total_duration])
            bass_octave = OBE.next_octave()
            bass_track.append([root_note, bass_octave, total_duration])
        
        # melody instruments 
        for melody_instrument_program, melody_instrument_velocity, start_time in self.melody_instruments:
            midi_generation.convert_melody_to_MIDI_data(melody_track=melody_track, melody_instrument_program=melody_instrument_program, velocity = melody_instrument_velocity, start_time=start_time)
        
        # chord instruments 
        for chord_instrument_program, chord_instrument_velocity, start_time in self.chord_instruments:
            midi_generation.convert_chord_to_MIDI_data(chord_track=chord_track, chord_instrument_program=chord_instrument_program, velocity = chord_instrument_velocity, start_time=start_time)
        
        # bass instruments 
        for bass_instrument_program, bass_instrument_velocity, start_time in self.bass_instruments:
            midi_generation.convert_bass_to_MIDI_data(bass_track=bass_track, bass_instrument_program=bass_instrument_program, velocity = bass_instrument_velocity, start_time=start_time)
        
        midi_generation.save_midi(filename=self.midi_file)

        # Generate the wav files
        synthesizer.generate_wav(midi_file=self.midi_file, soundfont=self.soundfont, wav_file=self.wav_file)

MG = Music_Generator(seed=1, tempo=110, measure_count=25)
MG.configure_instruments(melody_instruments=[[0, 110, 0]],
                         chord_instruments=[[48, 45, 0]],
                         bass_instruments=[[32, 50, 0]])
MG.generate_music()