from pathlib import Path
import sys
import os


def load_context(project_path):
    project_path = Path(project_path).expanduser().resolve()
    src_path = str(project_path / "tougher_on_turf")

    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    if "PYTHONPATH" not in os.environ:
        os.environ["PYTHONPATH"] = src_path

    if os.getcwd() != str(project_path):
        print("Changing the current working directory to %s", str(project_path))
        os.chdir(str(project_path))  # Move to project root
