import subprocess

def generate_wav(midi_file, soundfont, wav_file):
    subprocess.check_call([
    "fluidsynth",
    "-ni",
    "-F",
    wav_file,
    "-r",
    "44100",
    soundfont,
    midi_file])
    print("WAV generated successfully.")