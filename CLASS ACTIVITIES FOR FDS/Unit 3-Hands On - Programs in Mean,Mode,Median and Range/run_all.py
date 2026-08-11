import subprocess
import sys

scripts = [
    "01_mean.py",
    "02_median.py",
    "03_mode.py",
    "04_range.py",
    "05_variance.py",
    "06_std_dev.py",
    "07_statistics_module.py",
    "08_numpy_stats.py",
    "09_scipy_mode.py",
    "10_pandas_summary.py"
]

for script in scripts:
    print(f"\n==================== RUNNING {script} ====================")
    subprocess.run([sys.executable, script])