import config, pretty_midi

midi = pretty_midi.PrettyMIDI()

def note_to_midi_pitch(note, octave):
    semitone = config.note_to_semitone[note]
    midi_pitch = 12 * (octave + 1) + semitone
    return midi_pitch

def convert_melody_to_MIDI_data(melody_track, melody_instrument_program):
    melody = pretty_midi.Instrument(program=melody_instrument_program)
    start_time = 0
    velocity = 90
    for note, octave, duration in melody_track:
        end_time = start_time + duration
        pitch = note_to_midi_pitch(note=note, octave=octave)
        midi_note = pretty_midi.Note(velocity=velocity,
                                     pitch=pitch,
                                     start=start_time,
                                     end=end_time)
        start_time = end_time
        melody.notes.append(midi_note)
    return melody

def convert_chord_to_MIDI_data(chord_track, chord_instrument_program):
    chord = pretty_midi.Instrument(program=chord_instrument_program)
    start_time = 0
    velocity = 90
    for root, third, fifth, octave, duration in chord_track:
        end_time = start_time + duration
        root_pitch = note_to_midi_pitch(note=root, octave=octave)
        third_pitch = note_to_midi_pitch(note=third, octave=octave)
        fifth_pitch = note_to_midi_pitch(note=fifth, octave=octave)
        root_midi = pretty_midi.Note(velocity=velocity,
                                     pitch=root_pitch,
                                     start=start_time,
                                     end=end_time)
        third_midi = pretty_midi.Note(velocity=velocity,
                                     pitch=third_pitch,
                                     start=start_time,
                                     end=end_time)
        fifth_midi = pretty_midi.Note(velocity=velocity,
                                     pitch=fifth_pitch,
                                     start=start_time,
                                     end=end_time)
        start_time = end_time
        chord.notes.append(root_midi)
        chord.notes.append(third_midi)
        chord.notes.append(fifth_midi)
    return chord 

def convert_bass_to_MIDI_data(bass_track, bass_instrument_program):
    bass = pretty_midi.Instrument(program=bass_instrument_program)
    start_time = 0
    velocity = 90
    for root, octave, duration in bass_track:
        end_time = start_time + duration
        root_pitch = note_to_midi_pitch(note=root, octave=octave)
        root_midi = pretty_midi.Note(velocity=velocity,
                                     pitch=root_pitch,
                                     start=start_time,
                                     end=end_time)
        start_time = end_time
        bass.notes.append(root_midi)
    return bass 



# melody_track = [['D', 4, 1.0], ['E', 4, 0.5], ['F#', 4, 0.5], ['E', 4, 0.5], ['D', 4, 0.5], ['C#', 5, 0.5], ['C#', 5, 0.5], ['D', 4, 0.5], ['B', 5, 0.5], ['G', 5, 0.5], ['A', 5, 0.5]]
# convert_melody_to_MIDI_data(melody_track=melody_track, melody_instrument_program=0)

