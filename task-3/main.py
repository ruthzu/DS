from pathlib import Path


def main() -> None:
    from src.part1_custom_dataset import save_dataset
    from src.part2_titanic import analyze, clean, explore

    data_dir = Path(__file__).resolve().parent / "data"

    print("Part 1: Create Your Own Dataset (Foundation)")
    custom_df = save_dataset(data_dir / "custom_dataset.csv")
    print(custom_df)

    print("\nPart 2: Real Dataset - Titanic")
    titanic_path = data_dir / "dataset-2.csv"
    import pandas as pd

    df = pd.read_csv(titanic_path)
    explore(df)
    df = clean(df)
    analyze(df)


if __name__ == "__main__":
    main()
