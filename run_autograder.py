import subprocess
import pytest
import os
import pandas as pd

# Function to run the score_assignment.py script
def run_score_assignment():
    try:
        result = subprocess.run(["python3", "score_assignment.py"], capture_output=True, text=True)
        print("Score Assignment Output:\n", result.stdout)
        if result.returncode != 0:
            print("Error running score_assignment.py")
            print(result.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error running score_assignment.py: {e}")
        return False

# Function to run pytest tests/test_fight.py
def run_pytest():
    try:
        result = subprocess.run(["pytest", "tests/test_fight.py", "--maxfail=1", "--disable-warnings", "-q"], capture_output=True, text=True)
        print("Pytest Output:\n", result.stdout)
        if result.returncode != 0:
            print("Error running pytest")
            print(result.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error running pytest: {e}")
        return False

# Function to compare the generated DataFrame with the expected DataFrame
def compare_dataframes(student_df, expected_df):
    if student_df.equals(expected_df):
        print("DataFrames match! Assignment passed.")
        return True
    else:
        print("DataFrames do not match! Assignment failed.")
        student_df.to_csv("student_output.csv", index=False)  # Save the student's output for review
        return False

def main():
    # Run the student's assignment script
    score_assignment_success = run_score_assignment()
    
    if not score_assignment_success:
        print("Score assignment failed. Exiting.")
        return

    # Load the expected DataFrame
    expected_df = pd.read_csv("nicknames.csv")
    
    # Assuming the student's code generates 'nickname_df' (or similar)
    student_df = pd.read_csv("student_output.csv")  # This is where the student's output will be saved
    compare_dataframes(student_df, expected_df)

    # Run the tests using pytest
    pytest_success = run_pytest()
    if not pytest_success:
        print("Pytest tests failed. Check the test results above.")
        return

    print("All checks passed. Assignment complete.")

if __name__ == "__main__":
    main()
