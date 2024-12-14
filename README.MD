# 🥋 **MMA Fighter Statistics Assignment** 🥊

![📸 UFC Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/UFC_Logo.svg/2560px-UFC_Logo.svg.png)


Welcome to the **MMA Fighter Statistics Assignment**! 🚀 This guide provides everything you need to know about completing the assignment. Follow these instructions carefully to achieve your goals.

---

## 🎯 **Objective**

You will analyze an **MMA dataset**, process the data, and validate your implementation through testing. Your results will be compared with an expected dataset for accuracy.

### Deliverables:
1. **`tests/test_fight.py`** (under the `tests` folder): Test file to ensure your code works correctly.
2. **`score_assignment.py`** (in the root directory): Python script to process the MMA dataset and generate the required output.

---

## 📂 **Files Provided**

1. **Dataset**: `ufc-fighters-statistics.csv` - Input data for the assignment.
2. **Expected Output**: `nicknames.csv` - A reference for validation.
3. **Autograder Script**: `run_autograder.py` - Script to automate testing and evaluation.

---

## 📝 **File Requirements**

### 🔍 `tests/test_fight.py`

A **`pytest`** file to test your implementation. Here’s what you need to include:

#### **Test 1: `test_clean_data`**
- Ensure missing values in `height_cm` and `stance` are handled correctly.
- Verify that duplicates are removed successfully.

#### **Test 2: `test_add_win_rate`**
- Check that the "Win Rate (%)" column is added and calculated accurately.
- **Formula:**
  ```
  Win Rate (%) = (wins / (wins + losses + draws)) * 100
  ```

#### **Test 3: `test_get_nickname`**
- Ensure nicknames are generated for fighters without one.
- Validate duplicate nicknames are handled with unique suffixes.
- Prevent division by zero errors.

---

### ⚙️ `score_assignment.py`

A script that processes the MMA dataset and generates `student_output.csv`. Key functions:

#### **`load_data(file_path)`**
- **Purpose**: Load the dataset from a CSV file.
- **Input**: Path to the file.
- **Output**: A pandas DataFrame.

#### **`clean_data(df)`**
- **Purpose**: Handle missing values and remove duplicates.
- **Details**:
  - Replace missing values in `height_cm`, `weight_in_kg`, and `reach_in_cm` with `0`.
  - Fill missing `stance` with "Unknown".
  - Drop duplicate records.
- **Output**: Cleaned DataFrame.

#### **`add_win_rate(df)`**
- **Purpose**: Add a column for "Win Rate (%)".
- **Formula:**
  ```
  Win Rate (%) = (wins / (wins + losses + draws)) * 100
  ```
- **Output**: DataFrame with "Win Rate (%)".

#### **`get_nickname(df)`**
- **Purpose**: Generate nicknames for fighters.
- **Details**:
  - Use the fighter's first name if `nickname` is missing.
  - Handle duplicates by appending a unique suffix, e.g., "John_1_2.50".
  - Suffix indicates the win-loss ratio.
- **Output**: DataFrame with updated nicknames.

#### **`generate_visualizations(df)`**
- **Purpose**: Create visualizations from the data.
- **Visualizations:**
  1. **Bar Chart**: Nickname vs Win Rate (%).
  2. **Scatter Plot**: Height (cm) vs Reach (cm).
- **Output**: Save charts as `win_rate_bar_chart.png` and `height_vs_reach_scatter.png`.

---

### 🧪 `run_autograder.py`

This script validates your implementation:
1. Runs `score_assignment.py`.
2. Compares `student_output.csv` with `nicknames.csv`.
3. Executes `tests/test_fight.py` using `pytest`.

---

## 🚀 **How to Run and Submit the Assignment**

### Step 1: Accept the Assignment
🔗 Click the link provided to accept the assignment.

### Step 2: Clone the Repository
```bash
💻 git clone <repository_url>
```

### Step 3: Install Dependencies
```bash
📦 pip install -r requirements.txt
```

### Step 4: Run `score_assignment.py`
```bash
⚙️ python score_assignment.py
```
- Ensure `student_output.csv` matches `nicknames.csv`.

### Step 5: Create `test_fight.py`
- Write tests as per the "File Requirements" section.

### Step 6: Run Tests
```bash
🧪 pytest tests/test_fight.py
```

### Step 7: Commit and Push Your Code
```bash
📤 git add .
📝 git commit -m "Completed assignment implementation"
🌐 git push origin master
```

### Step 8: Submit the Assignment
- Verify all files are correct.
- Submit the repository link as instructed.

---

## 🔔 **Additional Notes**

- Reach out to me for help if needed.

✨ **Good luck! You’ve got this!** ✨

