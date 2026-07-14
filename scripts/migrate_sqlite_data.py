"""
SQLite se PostgreSQL me purana data shift karo.

Step 1 — SQLite se export:
    set USE_SQLITE=True
    python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 -o sqlite_backup.json

Step 2 — PostgreSQL pe import:
    set USE_SQLITE=False
    python manage.py migrate
    python manage.py loaddata sqlite_backup.json
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DUMP_PATH = BASE_DIR / "sqlite_backup.json"


def run(cmd: list[str], env: dict | None = None) -> None:
    print(">", " ".join(cmd))
    subprocess.run(cmd, cwd=BASE_DIR, env=env, check=True)


def main() -> None:
    if not (BASE_DIR / "db.sqlite3").exists():
        print("db.sqlite3 nahi mili — shayad data pehle se PostgreSQL me hai.")
        sys.exit(1)

    env_export = os.environ.copy()
    env_export["USE_SQLITE"] = "True"

    run(
        [
            sys.executable,
            "manage.py",
            "dumpdata",
            "--natural-foreign",
            "--natural-primary",
            "-e",
            "contenttypes",
            "-e",
            "auth.Permission",
            "--indent",
            "2",
            "-o",
            str(DUMP_PATH),
        ],
        env=env_export,
    )

    env_import = os.environ.copy()
    env_import.pop("USE_SQLITE", None)

    run([sys.executable, "manage.py", "migrate"], env=env_import)
    run([sys.executable, "manage.py", "loaddata", str(DUMP_PATH)], env=env_import)
    print("Done! SQLite data PostgreSQL me shift ho gaya.")


if __name__ == "__main__":
    main()
