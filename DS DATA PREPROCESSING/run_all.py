import glob
import subprocess

# Finds all python files in the current directory except this runner script
files = [f for f in glob.glob("*.py") if f != "run_all.py"]

for file in sorted(files):
    print(f"\n================ Running {file} ================")
    subprocess.run(["python", file])