import re
import os

def main():
    max_score = 1000
    points_per_assert = 50
    log_file = os.getenv('LOG_FILE', '.github/workflows/pytest.log')

    # Read the pytest output from the log file
    with open(log_file, 'r') as f:
        log_content = f.read()

    # Count dots and failed tests
    passed_tests = len(re.findall(r'\.', log_content))
    failed_tests = len(re.findall(r'F', log_content))

    # Calculate the total score
    total_tests = passed_tests + failed_tests
    score = min(passed_tests * points_per_assert, max_score)

    # Print the summary table
    print("Test runner summary")
    print("┌────────────────────┬─────────────┬─────────────┐")
    print("│ Test Runner Name   │ Test Score  │ Max Score   │")
    print("├────────────────────┼─────────────┼─────────────┤")
    print(f"│ test_session       │ {score:4}       │ {max_score:4}       │")
    print("├────────────────────┼─────────────┼─────────────┤")
    print(f"│ Total:             │ {score:4}       │ {max_score:4}       │")
    print("└────────────────────┴─────────────┴─────────────┘")
    print(f"🏆 Grand total tests passed: {passed_tests}/{total_tests}")
    print(f"🚨 Tests failed: {failed_tests}")

if __name__ == "__main__":
    main()
