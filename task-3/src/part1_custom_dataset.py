from pathlib import Path

import pandas as pd


def build_dataset() -> pd.DataFrame:
    data = {
        "student_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
        "name": [
            "Alex",
            "Bela",
            "Chen",
            "Dara",
            "Eli",
            "Faye",
            "Gus",
            "Hana",
            "Ivan",
            "Jade",
            "Kofi",
            "Lina",
            "Mona",
            "Niko",
            "Omar",
        ],
        "age": [19, 20, 18, 21, 19, 22, 20, 18, 21, 19, 23, 20, 18, 22, 21],
        "major": [
            "CS",
            "Math",
            "Physics",
            "CS",
            "Biology",
            "Math",
            "CS",
            "Physics",
            "Biology",
            "Math",
            "CS",
            "Physics",
            "Biology",
            "CS",
            "Math",
        ],
        "gpa": [3.6, 3.2, 3.8, 3.1, 3.4, 3.7, 3.0, 3.5, 3.3, 3.9, 2.9, 3.6, 3.2, 3.8, 3.1],
    }
    custom_index = [f"S-{idx}" for idx in range(1, 16)]
    return pd.DataFrame(data, index=custom_index)


def save_dataset(output_path: Path) -> pd.DataFrame:
    df = build_dataset()
    df.to_csv(output_path, index_label="index")
    return df


