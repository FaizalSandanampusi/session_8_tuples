import pytest
import sys

def main():
    max_score = 1000
    points_per_assert = 50
    
    # Run pytest and capture the output
    result = pytest.main(["--maxfail=20", "--disable-warnings"])
    
    # Parse the number of tests passed
    passed = result.testscollected - result.testsfailed - result.testspassed
    
    # Calculate the score
    score = min(passed * points_per_assert, max_score)

    # Print the summary table
    print("Test runner summary")
    print(" ┌────────────────────┬─────────────┬─────────────┐")
    print(" │ Test Runner Name   │ Test Score  │ Max Score   │")
    print(" ├────────────────────┼─────────────┼─────────────┤")
    print(f"│ test_session       │ {score}     │ {max_score} │")
    print(" ├────────────────────┼─────────────┼─────────────┤")
    print(f"│ Total:             │ {score}     │ {max_score} │")
    print(" └────────────────────┴─────────────┴─────────────┘")
    print(f"🏆 Grand total tests passed: {passed}/{result.testscollected}")

if __name__ == "__main__":
    sys.exit(main())
