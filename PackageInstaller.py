import subprocess
import sys

class InstallPackages:
    def __init__(self):
        self.InstallPackage()
    def InstallPackage(self):
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "opencv-python", "opencv-contrib-python", "numpy", "flask"])
            print("Packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing packages: {e}")