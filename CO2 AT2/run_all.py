import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RESULT_FILE = BASE_DIR / "run_results.txt"
SCRIPTS = [
    "1_data_preprocessing_visualization.py",
    "2_dataframe_demo.py",
    "3_scipy_examples.py",
    "4_sklearn_examples.py",
]

with RESULT_FILE.open("w", encoding="utf-8") as output_file:
    output_file.write("Run Results for data_analysis_scripts\n")
    output_file.write("=" * 50 + "\n\n")

    for script in SCRIPTS:
        output_file.write(f"Running {script}\n")
        output_file.write("-" * 50 + "\n")

        process = subprocess.run(
            ["python", str(BASE_DIR / script)],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
        )

        output_file.write("STDOUT:\n")
        output_file.write(process.stdout or "(no stdout)\n")
        output_file.write("\nSTDERR:\n")
        output_file.write(process.stderr or "(no stderr)\n")
        output_file.write(f"Exit code: {process.returncode}\n")
        output_file.write("=" * 50 + "\n\n")

        if process.returncode != 0:
            output_file.write("Execution stopped due to failure.\n")
            break

    output_file.write("Run complete.\n")

print(f"Results written to {RESULT_FILE}")
