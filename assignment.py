import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
def load_data(file_path):
    """Loads the MMA dataset from a CSV file."""
    return pd.read_csv(file_path)

# Clean data
def clean_data(df):
    """Cleans the dataset by handling missing values and duplicates."""
    # Fill missing numerical values with 0 and categorical values with 'Unknown'
    df.fillna({
        "height_cm": 0,
        "weight_in_kg": 0,
        "reach_in_cm": 0,
        "stance": "Unknown"
    }, inplace=True)
    # Drop duplicate rows
    df.drop_duplicates(inplace=True)
    return df

# Add Win Rate (%)
def add_win_rate(df):
    """Adds a derived column for Win Rate (%)"""
    df["Win Rate (%)"] = (df["wins"] / (df["wins"] + df["losses"] + df["draws"])) * 100
    return df


def get_nickname(df):
    """Generates nicknames for all players and handles duplicates."""
    # Initialize a dictionary to track nickname counts
    nickname_count = {}

    # Iterate over rows to generate nicknames
    for index, row in df.iterrows():
        # Extract nickname or use the first name
        nickname = row['nickname'] if pd.notna(row['nickname']) else row['name'].split()[0]
        
        # Handle duplicates
        if nickname in nickname_count:
            nickname_count[nickname] += 1
            # Assign number based on win/loss ratio
            win_loss_ratio = row['wins'] / (row['losses'] if row['losses'] != 0 else 1)  # Avoid division by zero
            nickname = f"{nickname}_{nickname_count[nickname]}_{win_loss_ratio:.2f}"
        else:
            nickname_count[nickname] = 0  # Start counting for this nickname
        
        # Update the 'nickname' column in the dataframe
        df.at[index, 'nickname'] = nickname
    nickname_df = pd.DataFrame(df[['name', 'nickname']])
    print(nickname_df)
    nickname_df.to_csv('nicknames.csv', index=False)


    return df


# Generate Visualizations
def generate_visualizations(df):
    """Generates a bar chart and scatter plot."""
    # Bar Chart: Nickname vs Win Rate (%)
    plt.figure(figsize=(10, 6))
    plt.bar(df["nickname"].fillna("Unknown"), df["Win Rate (%)"], color='blue')
    plt.xlabel("Nickname")
    plt.ylabel("Win Rate (%)")
    plt.title("Win Rate by Fighter Nickname")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("win_rate_bar_chart.png")
    plt.close()

    # Scatter Plot: Height (cm) vs Reach (cm)
    plt.figure(figsize=(8, 6))
    plt.scatter(df["height_cm"], df["reach_in_cm"], color='green', alpha=0.7)
    plt.xlabel("Height (cm)")
    plt.ylabel("Reach (cm)")
    plt.title("Height vs Reach")
    plt.savefig("height_vs_reach_scatter.png")
    plt.close()

# Main execution
if __name__ == "__main__":
    file_path = "ufc-fighters-statistics.csv"

    # Load, clean, and process the data
    df = load_data(file_path)
    df = clean_data(df)
    df = add_win_rate(df)
    df = get_nickname(df)

    # Generate visualizations
    generate_visualizations(df)

    print("Data processing and visualization complete.")


