import subprocess
import sys
import shutil
import os
import gdown
import zipfile


# downloading soundfont assets
def download_soundfont(url):
    os.makedirs("assets/soundfonts", exist_ok=True)

    sf2_file = "assets/soundfonts/GeneralUser-GS/GeneralUser-GS.sf2" 
    zip_file = "assets/soundfonts/GeneralUserGS.zip"

    if os.path.exists(sf2_file):
        print("GeneralUser GS already exists.")
        return

    print("Downloading GeneralUser GS...")
    gdown.download(
        url=url,
        output=zip_file,
        quiet=False
    )

    print("Extracting SoundFont...")

    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall("assets/soundfonts")

    os.remove(zip_file)

    if os.path.exists(sf2_file):
        print("SoundFont installed successfully.")
    else:
        print("ERROR: Could not find 'GeneralUser GS.sf2' after extraction.")



# installing the fluidsynth
def is_installed(program):
    return shutil.which(program) is not None


def install_fluidsynth():
    if is_installed("fluidsynth"):
        print("\nFluidSynth is already installed.")
        return

    print("\nFluidSynth was not found.")

    if is_installed("choco"):
        choice = input("Install FluidSynth using Chocolatey? (Y/N): ").strip().lower()

        if choice == "y":
            try:
                subprocess.check_call([
                    "choco",
                    "install",
                    "fluidsynth",
                    "-y"
                ])
                print("FluidSynth installed successfully.")
                return
            except subprocess.CalledProcessError:
                print("Failed to install FluidSynth using Chocolatey.")
                print("Try running this script (install.py) as Administrator. Open powershell as administartor > navigate to this file > run 'python install.py' or 'py install.py'")

    print("Please install FluidSynth manually.")
    print("https://www.fluidsynth.org/")

# --------------------------------------------------------------------------------
# all the packages required for the project: Melody Engine
packages = [
    "noise",
    "pretty_midi",
    "pyfluidsynth",
    "gdown",
    "flet"
]

print("Upgrading pip...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# for package in packages:
#     print(f"Installing {package}...")
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package ])

for package in packages:
    print(f"Installing/Upgrading {package}...")
    subprocess.check_call([sys.executable,"-m","pip","install","--upgrade",package])

install_fluidsynth()
download_soundfont(url="https://drive.google.com/uc?export=download&id=12ZzM70Nxnr4vqyUF0bbRKE_HXQgLRNid")
#print("\nAll dependencies installed successfully!")