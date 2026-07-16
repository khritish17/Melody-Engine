import pretty_midi

m = pretty_midi.PrettyMIDI("output/song.mid")

print("Number of instruments:", len(m.instruments))

total_notes = 0

for i, inst in enumerate(m.instruments):
    print(f"Instrument {i}")
    print("  Program:", inst.program)
    print("  Notes:", len(inst.notes))

    total_notes += len(inst.notes)

    if inst.notes:
        n = inst.notes[0]
        print("  First note:")
        print("    Pitch:", n.pitch)
        print("    Start:", n.start)
        print("    End:", n.end)
        print("    Velocity:", n.velocity)

print("Total notes:", total_notes)