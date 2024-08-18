import re
import os

def main():
    max_score = 1000
    points_per_assert = 50

    log_file = os.getenv('LOG_FILE', 'result.log')

    # Parse the pytest output to count the number of tests passed and failed
    with open(log_file, 'r') as f:
        log_content = f.read()

    passed_tests = len(re.findall(r'\.\.\.\.', log_content))
    failed_tests = len(re.findall(r'\[FAILED\]', log_content))

    total_tests = passed_tests + failed_tests
    score = min(passed_tests * points_per_assert, max_score)

    # Print the summary table
    print("Test runner summary")
    print("┌────────────────────┬─────────────┬─────────────┐")
    print("│ Test Runner Name   │ Test Score  │ Max Score   │")
    print("├────────────────────┼─────────────┼─────────────┤")
    print(f"│ test_session      │ {score:4}   │{max_score:4}│")
    print("├────────────────────┼─────────────┼─────────────┤")
    print(f"│ Total:            │ {score:4}   │{max_score:4}│")
    print("└────────────────────┴─────────────┴─────────────┘")
    print(f"🏆 Grand total tests passed: {passed_tests}/{total_tests}")

if __name__ == "__main__":
    main()
