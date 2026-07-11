import subprocess
import sys


# all the packages required for the project: Melody Engine
packages = [
    "noise"
]

print("Upgrading pip...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

for package in packages:
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package ])

print("\nAll dependencies installed successfully!")