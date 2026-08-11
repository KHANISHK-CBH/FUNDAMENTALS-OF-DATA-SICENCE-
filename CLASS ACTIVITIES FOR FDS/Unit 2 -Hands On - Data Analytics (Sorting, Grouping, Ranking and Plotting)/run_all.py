import glob
import subprocess
import sys

# Finds all python files in current directory except this runner
files = [
    f for f in glob.glob("*.py") if f != "run_all.py" and not f.startswith(".")
]

for file in sorted(files):
    print(f"\n================ Running {file} ================")
    # sys.executable ensures it uses the same Python interpreter as this script
    subprocess.run([sys.executable, file])