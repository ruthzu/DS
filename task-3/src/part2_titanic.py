from pathlib import Path

import pandas as pd


def explore(df: pd.DataFrame) -> None:
    print("\nStep 1: Exploration")
    print(df.head())
    print(df.info())
    print(df.describe(include="all"))


def clean(df: pd.DataFrame) -> pd.DataFrame:
    print("\nStep 2: Data Cleaning")
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())
    if "Embarked" in df.columns:
        df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    if "Cabin" in df.columns:
        df = df.drop(columns=["Cabin"])
    return df.drop_duplicates()


def analyze(df: pd.DataFrame) -> None:
    print("\nStep 3: Data Analysis")
    if "Survived" in df.columns and "Sex" in df.columns:
        survival_by_gender = df.groupby("Sex")["Survived"].mean()
        print("Survival rate by gender:")
        print(survival_by_gender)
    else:
        print("Columns 'Survived' and 'Sex' are required for groupby analysis.")


