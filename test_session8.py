import pytest
import os
import inspect
import re
from session8 import *
import session8

README_CONTENT_CHECK_FOR = [
    "stock",
    "namedtuple",
    "generate",
    "fake",
    'blood_type',
    'birthdate',
    'blood_group',
    'current_location',
    'average',
    'symbol',
    'open',
    'high',
    'low',
    'close',
    'weight'
]

def test_session8_readme_exists():
    """ 
        This test checks whether a README.md file exists in the current project
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_session8_readme_500_words():
    """ 
        This test checks whether the readme file contains atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session8_readme_proper_description():
    """ 
        This test cheecks whether the readme file contains good description of the assignment and
        checks if it has expected keywords. The keywords are defined globally in this file.
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c.lower() not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_session8_readme_file_for_more_than_10_hashes():
    """ 
        This code checks for formatting for readme file exisits. 
        It checks if there are hashes in the file which indicates
        usage of heading and comments in the readme file.There must 
        be atleast 10 hashes for function test to pass. 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_session8_indentations():
    """ 
        Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
    """
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session8_function_name_had_cap_letter():
    """
        This test checks whether the functions defined in the assignment
        file contains captial letters. As per the standard functions must
        not be defined in capital letters.
    """
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



############################## Assignment Validations###########################


############################## Validations for Named Tuple profiles ###########################


 # Test 1: The function returns the correct number of profiles as specified by the input parameter `n`.
 # Test 2: The returned value is a tuple.
 # Test 3: Each element within the returned tuple is an instance of the Profile namedtuple.

def test_generate_profiles_namedtuple():
    """
    Tests the generate_profiles_namedtuple function to ensure it generates the correct output.

    This test verifies the following:
    1. The function returns the correct number of profiles as specified by the input parameter `n`.
    2. The returned value is a tuple.
    3. Each element within the returned tuple is an instance of the Profile namedtuple.

    The test will raise an assertion error if any of these conditions are not met.
    If all checks pass, a confirmation message is printed.

    """
    profiles = generate_profiles_namedtuple(100)
    
    assert len(profiles) == 100, "Profile count does not match"
    
    assert isinstance(profiles, tuple), "Profiles should be a tuple"
    
    assert all(isinstance(profile, Profile) for profile in profiles), "All elements should be of type Profile"

#Test 4: Tests the largest_blood_type_namedtuple function to ensure it returns the correct output type.

def test_largest_blood_type_namedtuple():
    """
    Tests the largest_blood_type_namedtuple function to ensure it returns the correct output type.

    This test verifies the following:
    1. The function returns a value of type `str`, which indicates the blood type that occurs most frequently in the provided profiles.

    The test will raise an assertion error if the returned value is not a string.
    If the check passes, a confirmation message is printed.

    Example:
        >>> test_largest_blood_type_namedtuple()
        test_largest_blood_type_namedtuple passed
    """
    profiles = generate_profiles_namedtuple(100)
    result = largest_blood_type_namedtuple(profiles)
    
    assert isinstance(result, str), "Result should be a string"

#Few Tests for mean_current_location_namedtuple function.
#Test 5 : The function returns a value of type `tuple`.
#Test 6 : The returned tuple contains exactly two elements.
#Test 7 : Both elements of the tuple are of type `float`, representing the mean latitude and mean longitude.

def test_mean_current_location_namedtuple():
    """
    Tests the mean_current_location_namedtuple function to ensure it returns the correct output format.

    This test verifies the following:
    1. The function returns a value of type `tuple`.
    2. The returned tuple contains exactly two elements.
    3. Both elements of the tuple are of type `float`, representing the mean latitude and mean longitude.

    The test will raise an assertion error if any of these conditions are not met.
    If all checks pass, a confirmation message is printed.

    Example:
        >>> test_mean_current_location_namedtuple()
        test_mean_current_location_namedtuple passed
    """

    profiles = generate_profiles_namedtuple(100)
    result = mean_current_location_namedtuple(profiles)
    
    assert isinstance(result, tuple), "Result should be a tuple"
    
    assert len(result) == 2, "Result tuple should have two elements"
    
    assert isinstance(result[0], float) and isinstance(result[1], float), "Tuple elements should be floats"

# Test 8: Tests the oldest_person_age_namedtuple function to ensure it returns the correct output format.

def test_oldest_person_age_namedtuple():
    """
    Tests the oldest_person_age_namedtuple function to ensure it returns the correct output format.

    This test verifies the following:
    1. The function returns a value of type `int`, representing the age of the oldest person.
    2. The returned age is a non-negative integer.

    The test will raise an assertion error if any of these conditions are not met.
    If all checks pass, a confirmation message is printed.

    Example:
        >>> test_oldest_person_age_namedtuple()
        test_oldest_person_age_namedtuple passed
    """
    profiles = generate_profiles_namedtuple(100)
    ages = tuple(profile.age for profile in profiles)
    result = oldest_person_age_namedtuple(ages)
    
    assert isinstance(result, int), "Result should be an integer"
    assert result >= 0, "Age should be non-negative"
    
#Test 9:  Tests the average_age_namedtuple function to ensure it returns the correct output format.

def test_average_age_namedtuple():
    """
    Tests the average_age_namedtuple function to ensure it returns the correct output format.

    This test verifies the following:
    1. The function returns a value of type `float`, representing the average age.
    2. The returned average age is a non-negative float.

    The test will raise an assertion error if any of these conditions are not met.
    If all checks pass, a confirmation message is printed.

    Example:
        >>> test_average_age_namedtuple()
        test_average_age_namedtuple passed
    """
    profiles = generate_profiles_namedtuple(100)
    ages=tuple(profile.age for profile in profiles)
    result = average_age_namedtuple(ages)
    
    assert isinstance(result, float), "Result should be a float"
    assert result >= 0, "Average age should be non-negative"

#Test 10: Tests the functions using a predefined list of namedtuple profiles with known values to check if it returns expected output

def test_functions_with_sample_data():
    """
    Tests the functions using a predefined list of namedtuple profiles with known values.

    This test verifies that the following functions return the expected results when applied to a 
    set of sample profiles:

    The test will raise an assertion error if any of these functions do not return the expected 
    results. If all assertions pass, a confirmation message is printed.

    Example:
        >>> test_functions_with_sample_data()
        All tests passed
    """
    
    Profile = namedtuple('Profile', 'blood_type latitude longitude age')

    # Sample profiles with known values
    sample_profiles = [
        Profile('A+', -40.7, -74.0, 30),  
        Profile('B-', 34.0, 118.2, 25), 
        Profile('AB+', 41.8, -87.6, 35), 
        Profile('O-', -37.7, -122.4, 28), 
        Profile('A+', 40.7, 74.0, 40),  
        Profile('B-', -34.0, -118.2, 22), 
        Profile('AB+', 41.8, 87.6, 31), 
        Profile('A+', 37.7, -122.4, 29), 
    ]

    expected_largest_blood_type = 'A+'
    expected_mean_current_location = (10.45, -30.6)
    expected_oldest_person_age = 40
    expected_average_age = 30
    
    # Sample data
    profiles = sample_profiles
    ages = tuple(profile.age for profile in profiles)
    
    # Test largest_blood_type_namedtuple
    result_largest_blood_type = largest_blood_type_namedtuple(profiles)
    assert result_largest_blood_type == expected_largest_blood_type, (
        f"Expected {expected_largest_blood_type}, got {result_largest_blood_type}"
    )
    
    # Test mean_current_location_namedtuple
    result_mean_location = mean_current_location_namedtuple(profiles)
    assert result_mean_location == expected_mean_current_location, (
        f"Expected {expected_mean_current_location}, got {result_mean_location}"
    )
    
    # Test oldest_person_age_namedtuple
    result_oldest_age = oldest_person_age_namedtuple(ages)
    assert result_oldest_age == expected_oldest_person_age, (
        f"Expected {expected_oldest_person_age}, got {result_oldest_age}"
    )
    
    # Test average_age_namedtuple
    result_average_age = average_age_namedtuple(ages)
    assert result_average_age == expected_average_age, (
        f"Expected {expected_average_age}, got {result_average_age}"
    )

############################## Validations for Dictionary profiles ###########################


# Test 1: The function returns the correct number of profiles as specified by the input parameter `n`.
def test_generate_profiles_dict():
    profiles = generate_profiles_dict(100)
    assert len(profiles) == 100, "Profile count does not match"

# Test 2: The function returns a list.
def test_generate_profiles_dict_returns_list():
    profiles = generate_profiles_dict(100)
    assert isinstance(profiles, list), "Profiles should be a list"

# Test 3: Each element within the returned list is a dictionary.
def test_generate_profiles_dict_elements_are_dict():
    profiles = generate_profiles_dict(100)
    assert all(isinstance(profile, dict) for profile in profiles), "All elements should be of type dict"

# Test 4: The function largest_blood_type_dict returns a string.
def test_largest_blood_type_dict():
    profiles = generate_profiles_dict(100)
    result = largest_blood_type_dict(profiles)
    assert isinstance(result, str), "Result should be a string"

# Test 5: The function mean_current_location_dict returns a tuple.
# Test 6: The returned tuple contains exactly two elements.
# Test 7: Both elements of the tuple are of type `float`, representing the mean latitude and mean longitude.
def test_mean_current_location_dict():
    profiles = generate_profiles_dict(100)
    result = mean_current_location_dict(profiles)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Result tuple should have two elements"
    assert isinstance(result[0], float) and isinstance(result[1], float), "Tuple elements should be floats"

# Test 8: The function oldest_person_age_dict returns an integer.
# Test 9: The returned age is a non-negative integer.
def test_oldest_person_age_dict():
    profiles = generate_profiles_dict(100)
    result = oldest_person_age_dict(profiles)
    assert isinstance(result, int), "Result should be an integer"
    assert result >= 0, "Age should be non-negative"

# Test 10: The function average_age_dict returns a float.
# Test 11: The returned average age is a non-negative float.
def test_average_age_dict():
    profiles = generate_profiles_dict(100)
    result = average_age_dict(profiles)
    assert isinstance(result, float), "Result should be a float"
    assert result >= 0, "Average age should be non-negative"

# Test 12: Tests the functions using a predefined list of dictionary profiles with known values.
def test_functions_with_sample_data():
    sample_profiles = [
        {'blood_type': 'A+', 'latitude': -40.7, 'longitude': -74.0, 'age': 30},
        {'blood_type': 'B-', 'latitude': 34.0, 'longitude': 118.2, 'age': 25},
        {'blood_type': 'AB+', 'latitude': 41.8, 'longitude': -87.6, 'age': 35},
        {'blood_type': 'O-', 'latitude': -37.7, 'longitude': -122.4, 'age': 28},
        {'blood_type': 'A+', 'latitude': 40.7, 'longitude': 74.0, 'age': 40},
        {'blood_type': 'B-', 'latitude': -34.0, 'longitude': -118.2, 'age': 22},
        {'blood_type': 'AB+', 'latitude': 41.8, 'longitude': 87.6, 'age': 31},
        {'blood_type': 'A+', 'latitude': 37.7, 'longitude': -122.4, 'age': 29},
    ]

    expected_largest_blood_type = 'A+'
    expected_mean_current_location = (10.45, -30.6)
    expected_oldest_person_age = 40
    expected_average_age = 30.0

    result_largest_blood_type = largest_blood_type_dict(sample_profiles)
    assert result_largest_blood_type == expected_largest_blood_type, (
        f"Expected {expected_largest_blood_type}, got {result_largest_blood_type}"
    )

    result_mean_location = mean_current_location_dict(sample_profiles)
    assert result_mean_location == expected_mean_current_location, (
        f"Expected {expected_mean_current_location}, got {result_mean_location}"
    )

    result_oldest_age = oldest_person_age_dict(sample_profiles)
    assert result_oldest_age == expected_oldest_person_age, (
        f"Expected {expected_oldest_person_age}, got {result_oldest_age}"
    )

    result_average_age = average_age_dict(sample_profiles)
    assert result_average_age == expected_average_age, (
        f"Expected {expected_average_age}, got {result_average_age}"
    )
##########################################################################################
# Proving Name Tuples are faster than dictionary
##########################################################################################

def test_compare_performance_faster_namedtuple():
    n = 10000
    result = compare_performance(n)

    if "faster than Dictionary" in result:
        print("Test passed: Namedtuple implementation is faster than Dictionary.")
    else:
        print("Test failed: Make your Namedtuple calculations faster.")

    assert "faster than Dictionary" in result, "Make your Namedtuple calculations faster."


############################## Validations for Stock Index Estimator ###########################


# fake=Faker()

@pytest.fixture
def stock_data():
    """
    Fixture to generate stock data for testing.
    """
    return generate_stock_data(10, 100, 2000)

# Test 1: Check if the return type is tuple 
# Test 2: Check if all elements of tuple is Named Tuple
def test_return_type(stock_data):
    """
    Test that generate_stock_data returns a tuple of Stock namedtuples.
    """
    assert isinstance(stock_data, tuple), "The returned data is not a tuple."
    assert all(isinstance(stock, Stock) for stock in stock_data), "Not all elements are Stock namedtuples."

# Test 3: Check if Company name is of string type
def test_company_name_is_string(stock_data):
    """
    Test that the company name is a string.
    """
    for stock in stock_data:
        assert isinstance(stock.name, str), f"Company name {stock.name} for stock {stock.symbol} is not a string."

# Test 4: Check if stock symbol contains alphabets only and not special characters
# Test 5: Check if length of all ticker symbols generated is of length 3
def test_symbol_is_alphabetic_and_length(stock_data):
    """
    Test that the symbol contains only alphabetic characters and is exactly 3 characters long.
    """
    for stock in stock_data:
        assert stock.symbol.isalpha(), f"Symbol {stock.symbol} contains non-alphabetic characters."
        assert len(stock.symbol) == 3, f"Symbol {stock.symbol} is not exactly 3 characters long."

# Test 6: Check if all stock symbols generated are unique
def test_unique_stock_symbols(stock_data):
    """
    Test that all stock symbols are unique.
    """
    symbols = [stock.symbol for stock in stock_data]
    assert len(symbols) == len(set(symbols)), "Duplicate stock symbols found."

# Test 7: Check constraints on stock prices (high >= open, close <= high, close >= low, low <= high)
def test_stock_value_constraints(stock_data):
    """
    Test stock value constraints to ensure high >= open, close <= high and close >= low.
    """
    for stock in stock_data:
        assert stock.high >= stock.open, f"High price {stock.high} is less than open price {stock.open} for stock {stock.symbol}."
        assert stock.high >= stock.close, f"High price {stock.high} is less than close price {stock.close} for stock {stock.symbol}."
        assert stock.close >= stock.low, f"Close price {stock.close} is less than low price {stock.low} for stock {stock.symbol}."
        assert stock.low <= stock.high, f"Low price {stock.low} is greater than high price {stock.high} for stock {stock.symbol}."

# Test 8: Check market value constraints to ensure high >= open, close between low and high, and low <= high and open
def test_market_value_constraints(stock_data):
    """
    Test market values to ensure high >= open, close between low and high, and low <= high and open.
    """
    market_open, market_high, market_close = calculate_market_values(stock_data)
    assert market_high >= market_open, f"Market high value {market_high} is less than market open value {market_open}."
    assert market_high >= market_close, f"Market high value {market_high} is less than market close value {market_close}."
    assert market_close >= min(stock.low for stock in stock_data), f"Market close value {market_close} is less than the minimum low value."
    assert market_close <= market_high, f"Market close value {market_close} is greater than market high value {market_high}."

# Test 9: Check if ValueError is raised if start_range is greater than end_range
def test_value_error_on_invalid_range():
    """
    Test that a ValueError is raised when start_range is not less than end_range.
    """
    with pytest.raises(ValueError):
        generate_stock_data(10, 200, 100)

# Test 10: Check if weights are normalized to sum to 1
def test_weight_normalization(stock_data):
    """
    Test that the weights are normalized to sum to 1.
    """
    total_weight = sum(stock.weight for stock in stock_data)
    assert round(total_weight) == 1.0, f"Total weight {total_weight} does not sum to 1.0."

# Test 11: Check if the length of the stock data tuple matches the expected number of stocks
def test_stock_data_length():
    """
    Test that the length of the stock data tuple matches the expected number of stocks.
    """
    expected_length=100
    stock_data=generate_stock_data(expected_length, 100, 2000)
    assert len(stock_data) ==expected_length, f"Length of stock data tuple is {len(stock_data)}, expected {expected_length}."