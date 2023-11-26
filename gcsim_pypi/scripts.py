import json
from pathlib import Path

with open(
    Path(__file__).parent.joinpath("availability").joinpath("characters.json"), "w"
) as f:
    json.dump(
        list(
            set(
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
                        .parent.parent.joinpath("gcsim")
                        .joinpath("internal")
                        .joinpath("characters")
                    ).rglob("config.yml")
                ]
            )
        ),
        f,
    )

with open(
    Path(__file__).parent.joinpath("availability").joinpath("artifacts.json"), "w"
) as f:
    json.dump(
        list(
            set(
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
                        .parent.parent.joinpath("gcsim")
                        .joinpath("internal")
                        .joinpath("artifacts")
                    ).rglob("config.yml")
                ]
            )
        ),
        f,
    )

with open(
    Path(__file__).parent.joinpath("availability").joinpath("weapons.json"), "w"
) as f:
    json.dump(
        list(
            set(
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
                        .parent.parent.joinpath("gcsim")
                        .joinpath("internal")
                        .joinpath("weapons")
                    ).rglob("config.yml")
                ]
            )
        ),
        f,
    )
