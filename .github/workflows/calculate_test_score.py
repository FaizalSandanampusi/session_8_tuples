import re
import os
import sys

def extract_test_results_line(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if re.match(r'test_.*\.py\s+', line):
            return line.strip()
    return ""

def count_dots_and_failures(line):
    # Extract the part of the line after `test_session8.py`
    match = re.search(r'test_.*\.py\s+(.*)\s+\[', line)
    if match:
        line_content = match.group(1)
        dots = line_content.count('.')
        failures = line_content.count('F')
        return dots, failures
    return 0, 0

def main():
    log_file = os.getenv('LOG_FILE', '.github/workflows/pytest.log')
    test_results_line = extract_test_results_line(log_file)
    
    if test_results_line:
        passed_tests, failed_tests = count_dots_and_failures(test_results_line)
        
        points_per_assert = 50
        max_score = 1000
        score = min(passed_tests * points_per_assert, max_score)
        total_tests = passed_tests + failed_tests
        
        print("Test runner summary")
        print("┌────────────────────┬─────────────┬─────────────┐")
        print("│ Test Runner Name   │ Test Score  │ Max Score   │")
        print("├────────────────────┼─────────────┼─────────────┤")
        print(f"│ test_session      │ {score}     │{max_score}  │")
        print("├────────────────────┼─────────────┼─────────────┤")
        print(f"│ Total:            │ {score}     │{max_score}  │")
        print("└────────────────────┴─────────────┴─────────────┘")
        print(f"🏆 Grand total tests passed: {passed_tests}/{total_tests}")
        print(f"🚨 Tests failed: {failed_tests}")

        if failed_tests > 0:
            sys.exit(1)
    else:
        print("No test results line found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
