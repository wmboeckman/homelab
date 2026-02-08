import os
import subprocess
import sys

VENV_DIR = ".venv/"

def main():
    # Determine the correct pip path based on OS
    pip_exe = os.path.join(VENV_DIR, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_dir, "bin", "pip")
    python_exe = os.path.join(VENV_DIR, "Scripts", "python") if os.name == "nt" else os.path.join(venv_dir, "bin", "python")

    create_venv()

    print("Installing requirements...")
    subprocess.check_call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([pip_exe, "install", "-r", "requirements.txt"])
    print("Setup finished successfully.")

def create_venv():
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in {VENV_DIR}...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
    else:
        print("Virtual environment already exists.")

if __name__ == "__main__":
    main()