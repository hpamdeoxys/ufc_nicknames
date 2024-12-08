import pandas as pd
import pytest
from assignment import (clean_data, add_win_rate, get_nickname)

@pytest.fixture
def sample_data():
    return pd.read_csv("ufc-fighters-statistics.csv")

def test_clean_data(sample_data):
    cleaned_df = clean_data(sample_data)
    assert cleaned_df["height_cm"].isnull().sum() == 0, "Missing values not filled for height."
    assert cleaned_df["stance"].isnull().sum() == 0, "Missing values not filled for stance."
    assert len(cleaned_df) == len(sample_data.drop_duplicates()), "Duplicates not removed."

def test_add_win_rate(sample_data):
    cleaned_df = clean_data(sample_data)
    df_with_win_rate = add_win_rate(cleaned_df)
    assert "Win Rate (%)" in df_with_win_rate.columns, "Win Rate (%) column missing."
    first_row = df_with_win_rate.iloc[0]
    expected_win_rate = (first_row["wins"] / (first_row["wins"] + first_row["losses"] + first_row["draws"])) * 100
    assert abs(first_row["Win Rate (%)"] - expected_win_rate) < 0.1, "Win Rate (%) calculation incorrect."

def test_get_nickname(sample_data):
    df = clean_data(sample_data)
    df = add_win_rate(df)
    df = get_nickname(df)

    for index, row in df.iterrows():
        if pd.isna(row["nickname"]):
            first_name = row["name"].split()[0]
            assert row["nickname"] == first_name, f"Nickname for {row['name']} should be {first_name}."

    nickname_counts = df['nickname'].value_counts()
    for nickname, count in nickname_counts.items():
        if count > 1:
            nickname_rows = df[df['nickname'] == nickname]
            for i, row in enumerate(nickname_rows.itertuples(), 1):
                expected_nickname = f"{nickname}_{i}_{row._asdict()['Win Rate (%)']:.2f}"
                assert row.nickname == expected_nickname, f"Duplicate nickname {nickname} for {row.name} is incorrect."

    for index, row in df.iterrows():
        wins = row['wins']
        losses = row['losses']
        if losses == 0:
            assert row["nickname"] is not None, f"Division by zero error for {row['name']}."
