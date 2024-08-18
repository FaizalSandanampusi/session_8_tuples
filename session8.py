from datetime import date
from faker import Faker
from collections import namedtuple, Counter
from functools import wraps
from time import perf_counter
from typing import Tuple, Optional, Dict, List

"""
--------------------------------------------------------------------------------------------------------------
1. Use the **Faker** library to get 10000 random profiles. Using namedtuple, calculate the largest blood type,
    mean-current_location, oldest_person_age, and average age.
--------------------------------------------------------------------------------------------------------------
"""

# Creating Faker instance
fake = Faker()

# Define namedtuple
Profile = namedtuple('Profile', 'blood_type latitude longitude age')

def generate_profiles_namedtuple(n: int) -> tuple:
    """
    Generates `n` profiles using namedtuple.

    Args:
        n (int): Number of profiles to generate.

    Returns:
        tuple: A tuple containing `n` Profile namedtuples.
    """
    profiles = []
    append = profiles.append
    for _ in range(n):
        profile = fake.profile()
        birthdate = profile['birthdate']
        append(Profile(
            blood_type=profile['blood_group'],
            latitude=profile['current_location'][0],
            longitude=profile['current_location'][1],
            age=date.today().year - birthdate.year
        ))
    return tuple(profiles)

# Writing a timing decorator to time the function runtimes
def timing_decorator(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Function {func.__name__} Execution Time: {end - start:.6f} seconds")
        return result
    return wrapper

# Defining functions as per assignment
@timing_decorator
def largest_blood_type_namedtuple(profiles: Tuple) -> Optional[str]:
    """
    Returns the blood type with the highest frequency.

    Args:
        profiles (Tuple): A tuple of Profile namedtuples.

    Returns:
        Optional[str]: The blood type with the highest frequency. If multiple blood types have the same frequency, one of them is returned.
        Returns None if the profiles list is empty.
    """
    if not profiles:
        return None
    blood_type_counts = Counter(profile.blood_type for profile in profiles)
    return blood_type_counts.most_common(1)[0][0]

@timing_decorator
def mean_current_location_namedtuple(profiles: Tuple) -> Tuple[float, float]:
    """
    Returns the mean latitude and longitude from a list of namedtuple profiles.

    Args:
        profiles (Tuple): A tuple of Profile namedtuples.

    Returns:
        Tuple[float, float]: A tuple containing the mean latitude and mean longitude as floats.
    """
    total_lat = sum(profile.latitude for profile in profiles)
    total_long = sum(profile.longitude for profile in profiles)
    count = len(profiles)
    return (float(total_lat / count), float(total_long / count))

@timing_decorator
def oldest_person_age_namedtuple(ages: Tuple[int, ...]) -> int:
    """
    Returns the age of the oldest person.

    Args:
        ages (Tuple[int, ...]): A tuple of integers representing ages.

    Returns:
        int: The age of the oldest person.
    """
    return int(max(ages))

@timing_decorator
def average_age_namedtuple(ages: Tuple[int, ...]) -> float:
    """
    Returns the average age from a list of namedtuple profiles.

    Args:
        ages (Tuple[int, ...]): A tuple of integers representing ages.

    Returns:
        float: The average of age.
    """
    return round(sum(ages) / len(ages), 2)

"""
--------------------------------------------------------------------------------------------------------------
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)
--------------------------------------------------------------------------------------------------------------
"""

def generate_profiles_dict(n: int) -> List[Dict]:
    """
    Generates `n` profiles using dictionaries.

    Args:
        n (int): Number of profiles to generate.

    Returns:
        List[Dict]: A list of dictionaries, each representing a profile with keys 'blood_type', 'latitude', 'longitude', and 'age'.
    """
    profiles = []
    append = profiles.append
    for _ in range(n):
        profile = fake.profile()
        birthdate = profile['birthdate']
        append({
            'blood_type': profile['blood_group'],
            'latitude': profile['current_location'][0],
            'longitude': profile['current_location'][1],
            'age': date.today().year - birthdate.year
        })
    return profiles

@timing_decorator
def largest_blood_type_dict(profiles: List[Dict]) -> str:
    """
    Returns the blood type with the highest frequency using dictionary operations.

    Args:
        profiles (List[Dict]): A list of dictionaries representing profiles.

    Returns:
        str: The blood type that occurs most frequently.
    """
    blood_type_counts = {}
    for profile in profiles:
        blood_type = profile['blood_type']
        blood_type_counts[blood_type] = blood_type_counts.get(blood_type, 0) + 1
    return max(blood_type_counts, key=blood_type_counts.get)

@timing_decorator
def mean_current_location_dict(profiles: List[Dict]) -> Tuple[float, float]:
    """
    Returns the mean latitude and longitude using dictionary operations.

    Args:
        profiles (List[Dict]): A list of dictionaries representing profiles.

    Returns:
        Tuple[float, float]: A tuple containing the mean latitude and longitude.
    """
    latitude_sum = 0
    longitude_sum = 0
    count = len(profiles)
    for profile in profiles:
        latitude_sum += profile['latitude']
        longitude_sum += profile['longitude']
    return (float(latitude_sum / count), float(longitude_sum / count))

@timing_decorator
def oldest_person_age_dict(profiles: List[Dict]) -> int:
    """
    Returns the age of the oldest person using dictionary operations.

    Args:
        profiles (List[Dict]): A list of dictionaries representing profiles.

    Returns:
        int: The age of the oldest person.
    """
    return max(profile['age'] for profile in profiles)

@timing_decorator
def average_age_dict(profiles: List[Dict]) -> float:
    """
    Returns the average age using dictionary operations.

    Args:
        profiles (List[Dict]): A list of dictionaries representing profiles.

    Returns:
        float: The average age.
    """
    age_sum = sum(profile['age'] for profile in profiles)
    return round(age_sum / len(profiles), 2)

def compare_performance(n: int) -> None:
    """
    Compares the performance of metric calculations using namedtuple vs dictionary implementations.

    Args:
        n (int): The number of profiles to generate and evaluate.

    Returns:
        str: A string indicating whether namedtuple or dictionary implementation is faster.
    """
    profiles_tuples = generate_profiles_namedtuple(n)
    ages_tuple = tuple(profile.age for profile in profiles_tuples)

    start = perf_counter()
    print("Calculating metrics using Named Tuple operations...")
    largest_blood_type_namedtuple(profiles_tuples)
    mean_current_location_namedtuple(profiles_tuples)
    oldest_person_age_namedtuple(ages_tuple)
    average_age_namedtuple(ages_tuple)
    end = perf_counter()
    total_elapsed_named_tuple = end - start
    print("\nTotal Elapsed time for Named Tuple calculations: {:.4f} seconds\n".format(total_elapsed_named_tuple))

    profiles_dict = generate_profiles_dict(n)
    start = perf_counter()
    print("Calculating metrics using Dictionary operations...")
    largest_blood_type_dict(profiles_dict)
    mean_current_location_dict(profiles_dict)
    oldest_person_age_dict(profiles_dict)
    average_age_dict(profiles_dict)
    end = perf_counter()
    total_elapsed_dict = end - start
    print("Total Elapsed time for Dictionary calculations: {:.4f} seconds\n".format(total_elapsed_dict))

    if total_elapsed_dict > total_elapsed_named_tuple:
        return f"Namedtuple is {total_elapsed_dict / total_elapsed_named_tuple:.2f} times faster than Dictionary."
    else:
        return f"Dictionary is {total_elapsed_named_tuple / total_elapsed_dict:.2f} times faster than Namedtuple."

"""
--------------------------------------------------------------------------------------------------------------
3. Create fake data (you can use Faker for company names) for an imaginary stock exchange for the top 100 companies 
    (name, symbol, open, high, close). Assign a random weight to all the companies. Stock Market Value would be the sum 
    of each_stock_value*random number/(sum of random values) or for 100 companies. Calculate and show what value the 
    stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high,
    and close are not totally random. You can only use namedtuple. - 500 (including 10 test cases)
--------------------------------------------------------------------------------------------------------------
"""

import random
import re

# Define the Stock namedtuple
Stock = namedtuple('Stock', ['name', 'symbol', 'open', 'high', 'low', 'close', 'weight'])

fake = Faker()

def generate_stock_data(num_stocks: int = 100, start_range: int = 10, end_range: int = 500) -> Tuple[Stock, ...]:
    """
    Generates fake stock data for a specified number of stocks.

    Args:
        num_stocks (int): The number of stocks to generate. Default is 100.
        start_range (int): The minimum value for the stock price. Default is 10.
        end_range (int): The maximum value for the stock price. Default is 500.

    Returns:
        Tuple[Stock, ...]: A tuple of Stock namedtuples, each containing:
            - name (str): The name of the company.
            - symbol (str): The stock ticker symbol.
            - open (float): The opening price of the stock.
            - high (float): The highest price of the stock during the day.
            - low (float): The lowest price of the stock during the day.
            - close (float): The closing price of the stock.
            - weight (float): The weight of the stock in a portfolio, normalized to sum to 1.

    Raises:
        ValueError: If the start_range is not less than the end_range.
    """
    if start_range >= end_range:
        raise ValueError("start_range must be less than end_range")

    stocks = []
    total_weight = 0.0
    weights = []
    used_symbols = set()

    while len(stocks) < num_stocks:
        name = fake.company()
        x = ''.join(set(re.sub(r'[^a-zA-Z]', '', name.upper())))

        for _ in range(20):
            symbol = ''.join(random.choices(x, k=3))
            if symbol not in used_symbols:
                used_symbols.add(symbol)
                break
        else:
            continue  # Retry with a new company name if no unique symbol was found

        open_price = round(random.uniform(start_range, end_range), 4)
        high_price = round(random.uniform(1.001, 1.15) * open_price, 4)
        low_price = round(random.uniform(0.85, 1) * open_price, 4)
        close_price = round(random.uniform(low_price, high_price), 4)

        weight = round(random.random(), 4)
        weights.append(weight)
        total_weight += weight

        stock = Stock(name, symbol, open_price, high_price, low_price, close_price, weight)
        stocks.append(stock)

    # Normalize weights so they sum to 1
    normalized_stocks = tuple(stock._replace(weight=round(stock.weight / total_weight, 4)) for stock in stocks)

    return tuple(normalized_stocks)

def calculate_market_values(stocks: Tuple[Stock, ...]) -> Tuple[float, float, float]:
    """
    Calculate the weighted market values for open, high, and close prices.

    Args:
        stocks (Tuple[Stock, ...]): A tuple of Stock namedtuples, each containing the open, high, close prices, and a weight.

    Returns:
        Tuple[float, float, float]: The weighted market open, high, and close values, rounded to two decimal places.
    """
    market_open = sum(stock.open * stock.weight for stock in stocks)
    market_high = sum(stock.high * stock.weight for stock in stocks)
    market_close = sum(stock.close * stock.weight for stock in stocks)
    return round(market_open, 4), round(market_high, 4), round(market_close, 4)
