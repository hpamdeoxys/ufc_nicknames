# MMA Fighter Statistics Assignment

![Placeholder for Assignment Logo or Image]

Welcome to the MMA Fighter Statistics Assignment! This document provides a detailed overview of what you are expected to do, how to structure your files, and how to run and submit your work. Follow the instructions carefully to ensure your assignment meets all requirements.

---

## Objective

You will analyze an MMA dataset, process the data, and perform tests to validate the correctness of your implementation. Your final output will be compared with an expected dataset to verify your results.

You are required to create **two files**:

1. `tests/test_fight.py` (under the `tests` folder): A test file to validate the correctness of your implementation.
2. `score_assignment.py` (in the root directory): A Python script to process the MMA dataset and generate the required output.

---

## Files Provided

1. **Dataset**: `ufc-fighters-statistics.csv` - The input dataset.
2. **Expected Output**: `nicknames.csv` - The expected output dataset.
3. **Autograder Script**: `run_autograder.py` - A script to validate your implementation.

---

## File Requirements

### `tests/test_fight.py`

This is your test file, which will run using `pytest`. Below is a summary of the tests you are required to include:

- **Test 1: `test_clean_data`**

  - Verify that missing values in `height_cm` and `stance` are handled correctly.
  - Ensure duplicates are removed.

- **Test 2: `test_add_win_rate`**

  - Verify the "Win Rate (%)" column is added correctly.
  - Ensure the win rate is calculated accurately.
  
  Formula for Win Rate:
  ```
  Win Rate (%) = (wins / (wins + losses + draws)) * 100
  ```

- **Test 3: `test_get_nickname`**

  - Ensure nicknames are generated correctly when missing.
  - Validate that duplicate nicknames are handled properly using a unique suffix.
  - Check for potential division by zero errors.

### `score_assignment.py`

This script processes the MMA dataset and generates `student_output.csv`. It includes the following functions:

- **`load_data(file_path)`**

  - **Purpose**: Loads the MMA dataset from a CSV file.
  - **Input**: File path to the dataset.
  - **Output**: A pandas DataFrame containing the dataset.

- **`clean_data(df)`**

  - **Purpose**: Handles missing values and removes duplicates.
  - **Details**:
    - Missing values in `height_cm`, `weight_in_kg`, `reach_in_cm` are filled with `0`.
    - Missing `stance` values are replaced with "Unknown".
    - Duplicates are dropped.
  - **Output**: A cleaned DataFrame.

- **`add_win_rate(df)`**

  - **Purpose**: Adds a derived column for "Win Rate (%)".
  - **Details**: Win rate is calculated using the formula:
    ```
    Win Rate (%) = (wins / (wins + losses + draws)) * 100
    ```
  - **Output**: A DataFrame with the additional "Win Rate (%)" column.

- **`get_nickname(df)`**

  - **Purpose**: Generates nicknames for fighters.
  - **Details**:
    - If `nickname` is missing, it uses the fighter's first name.
    - Handles duplicate nicknames by appending a unique suffix based on a counter and win-loss ratio.
    - Example:
      - Fighter A: Nickname = "John"
      - Fighter B: Nickname = "John_1_2.50" (indicating 2.5 win-loss ratio)
  - **Output**: A DataFrame with updated nicknames.

- **`generate_visualizations(df)`**

  - **Purpose**: Creates visualizations from the data.
  - **Details**:
    1. **Bar Chart**: Nickname vs Win Rate (%)
    2. **Scatter Plot**: Height (cm) vs Reach (cm)
  - **Output**: Saves visualizations as `win_rate_bar_chart.png` and `height_vs_reach_scatter.png`.

### `run_autograder.py`

This script validates your implementation. It:

1. Runs `score_assignment.py`.
2. Compares `student_output.csv` with `nicknames.csv`.
3. Executes the tests in `tests/test_fight.py` using `pytest`.

---

## How to Run and Submit the Assignment

### Step 1: Accept the Assignment

You will be provided a link to accept the assignment. Click on the link and follow the prompts.

### Step 2: Clone the Repository

Once you accept the assignment, clone the repository to your local machine using:

```bash
git clone <repository_url>
```

### Step 3: Install Dependencies

Install the required Python libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Run `score_assignment.py`

Run the `score_assignment.py` script to generate `student_output.csv`:

```bash
python score_assignment.py
```

Verify that the file `student_output.csv` matches `nicknames.csv`.

### Step 5: Create `test_fight.py`

Create the `test_fight.py` file under the `tests` folder. Add the tests as described in the "File Requirements" section.

### Step 6: Test Your Implementation

Run the `pytest` tests to validate your implementation:

```bash
pytest tests/test_fight.py
```

### Step 7: Commit and Push Your Code

Follow these steps to push your code to GitHub:

1. Add all changes:
   ```bash
   git add .
   ```
2. Commit your changes:
   ```bash
   git commit -m "Completed assignment implementation"
   ```
3. Push to the repository:
   ```bash
   git push origin main
   ```

### Step 8: Submit the Assignment

Once you have pushed your code to GitHub, ensure all files are present and tests pass. Submit your repository link as instructed.

---

## Additional Notes

- Ensure your code is well-commented and adheres to Python best practices.
- Verify that all tests pass before submission.
- If you encounter any issues, consult your instructor or teaching assistant.

Good luck with the assignment!

