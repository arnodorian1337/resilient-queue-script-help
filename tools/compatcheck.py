"""Run the repository's installed GitHub CLI compatibility extension."""

from pathlib import Path
import os
import subprocess
import sys


environment = os.environ.copy()
environment["XDG_DATA_HOME"] = str(Path(__file__).with_name(".compat-data"))
environment["GH_NO_UPDATE_NOTIFIER"] = "1"
environment["GH_PROMPT_DISABLED"] = "1"

result = subprocess.run(
    ["gh.exe", "extension", "exec", "--help"],
    env=environment,
    text=True,
    capture_output=True,
    check=False,
)
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
raise SystemExit(result.returncode)
