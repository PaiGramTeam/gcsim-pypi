import re
import json
from pathlib import Path

GCSIM_PATH = Path(__file__).parent.joinpath("gcsim")
GCSIM_PYPI_PATH = Path(__file__).parent.joinpath("gcsim_pypi")


def generate():
    print("Generating character...")
    character_keys = set(
        next(
            filter(
                lambda line: line.startswith("key:"),
                f.read_text().split("\n"),
            ),
            f.parent.stem,
        )
        .split(" ")[-1]
        .strip('"')
        for f in (GCSIM_PATH.joinpath("internal").joinpath("characters")).rglob(
            "config.yml"
        )
    )
    character_aliases = {}
    for alias, key in re.findall(
        r"\"(\w+)\":[ ]*keys\.(\w+),",
        GCSIM_PATH.joinpath("pkg")
        .joinpath("shortcut")
        .joinpath("characters.go")
        .read_text(),
    ):
        if alias in character_aliases:
            print(f"WARNING: Duplicate alias {alias} for {key}")
        character_aliases[alias] = key.lower()
    character_aliases.update({key: key for key in character_keys})

    with open(
        GCSIM_PYPI_PATH.joinpath("availability").joinpath("characters.py"),
        "w",
    ) as f:
        f.write("AVAILABLE_CHARACTERS = {\n")
        for character in sorted(character_keys.union(character_aliases.keys())):
            f.write(f'  "{character}",\n')
        f.write("}")
    with open(
        GCSIM_PYPI_PATH.joinpath("aliases").joinpath("characters.py"),
        "w",
    ) as f:
        f.write("CHARACTER_ALIASES = {\n")
        for alias, key in character_aliases.items():
            f.write(f'  "{alias}": "{key}",\n')
        f.write("}")

    print("Generating artifact...")
    artifact_keys = set(
        [
            next(
                filter(
                    lambda line: line.startswith("key:"),
                    f.read_text().split("\n"),
                ),
                f.parent.stem,
            )
            .split(" ")[-1]
            .strip('"')
            for f in (
                Path(__file__)
                .parent.joinpath("gcsim")
                .joinpath("internal")
                .joinpath("artifacts")
            ).rglob("config.yml")
        ]
    )
    artifact_aliases = {}
    for alias, key in re.findall(
        r"\"(\w+)\":[ ]*keys\.(\w+),",
        GCSIM_PATH.joinpath("pkg")
        .joinpath("shortcut")
        .joinpath("artifacts.go")
        .read_text(),
    ):
        if alias in artifact_aliases:
            print(f"WARNING: Duplicate alias {alias} for {key}")
        artifact_aliases[alias] = key.lower()
    artifact_aliases.update({key: key for key in artifact_keys})

    with open(
        GCSIM_PYPI_PATH.joinpath("availability").joinpath("artifacts.py"),
        "w",
    ) as f:
        f.write("AVAILABLE_ARTIFACTS = {\n")
        for art in sorted(artifact_keys.union(artifact_aliases.keys())):
            f.write(f'  "{art}",\n')
        f.write("}")
    with open(GCSIM_PYPI_PATH.joinpath("aliases").joinpath("artifacts.py"), "w") as f:
        f.write("ARTIFACT_ALIASES = {\n")
        for alias, key in artifact_aliases.items():
            f.write(f'  "{alias}": "{key}",\n')
        f.write("}")

    print("Generating weapon...")
    weapon_keys = set(
        next(
            filter(
                lambda line: line.startswith("key:"),
                f.read_text().split("\n"),
            ),
            f.parent.stem,
        )
        .split(" ")[-1]
        .strip('"')
        for f in (GCSIM_PATH.joinpath("internal").joinpath("weapons")).rglob(
            "config.yml"
        )
    )
    weapon_aliases = {}
    for alias, key in re.findall(
        r"\"(\w+)\":[ ]*keys\.(\w+),",
        GCSIM_PATH.joinpath("pkg")
        .joinpath("shortcut")
        .joinpath("weapons.go")
        .read_text(),
    ):
        if alias in weapon_aliases:
            print(f"WARNING: Duplicate alias {alias} for {key}")
        weapon_aliases[alias] = key.lower()
    weapon_aliases.update({key: key for key in weapon_keys})

    with open(
        GCSIM_PYPI_PATH.joinpath("availability").joinpath("weapons.py"),
        "w",
    ) as f:
        f.write("AVAILABLE_WEAPONS = {\n")
        for weapon in sorted(weapon_keys.union(weapon_aliases.keys())):
            f.write(f'  "{weapon}",\n')
        f.write("}")
    with open(
        GCSIM_PYPI_PATH.joinpath("aliases").joinpath("weapons.py"),
        "w",
    ) as f:
        f.write("WEAPON_ALIASES = {\n")
        for alias, key in weapon_aliases.items():
            f.write(f'  "{alias}": "{key}",\n')
        f.write("}")


if __name__ == "__main__":
    generate()
