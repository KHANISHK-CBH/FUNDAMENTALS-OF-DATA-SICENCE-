import subprocess
import sys

# List of all python files to run in order
files_to_run = [
    "program1_data_analysis.py",
    "program2_pandas_basics.py",
    "program3_scipy_basics.py",
    "program4_scikit_supervised.py",
    "program5_scikit_unsupervised.py",
]

for file in files_to_run:
    print("=" * 60)
    print(f"RUNNING FILE: {file}")
    print("=" * 60)
    
    # Executes the file in a separate subprocess using the active Python interpreter
    result = subprocess.run([sys.executable, file])
    
    if result.returncode != 0:
        print(f"Error occurred while executing {file}")
    print("\n")