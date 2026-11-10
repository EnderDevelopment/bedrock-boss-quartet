from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "FourRealmsBosses.mcpack"
FILES = [
    Path("manifest.json"),
    Path("README.md"),
    Path("entities/ember_tyrant.json"),
    Path("entities/storm_colossus.json"),
    Path("entities/tide_hydra.json"),
    Path("entities/void_reaver.json"),
]

with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED) as archive:
    for relative_path in FILES:
        source = ROOT / relative_path
        if not source.is_file():
            raise FileNotFoundError(f"Missing required pack file: {relative_path}")
        archive.write(source, relative_path.as_posix())

print(f"Created {OUTPUT}")
