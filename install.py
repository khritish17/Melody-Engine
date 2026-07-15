import subprocess
import sys
import shutil
import os
import gdown


# downloading soundfont assets
def download_soundfont(url):
    os.makedirs("assets/soundfonts", exist_ok=True)

    output = "assets/soundfonts/GeneralUser GS.sf2"

    if os.path.exists(output):
        print("GeneralUser GS already exists.")
        return

    print("Downloading GeneralUser GS...")
    gdown.download(
        url=url,
        output=output,
        quiet=False,
    )

    print("Download complete.")



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
    "gdown"
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