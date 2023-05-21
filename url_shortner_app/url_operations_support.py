import time
from random import randint

from .constants import BASE_62_CONVERSION_MAPPING


def generate_unique_id():
    timestamp = int(time.time() * 1000)  # Current timestamp
    generated_number = randint(10000, 9999999)  # Random max 7 digit number
    unique_number = int(str(timestamp)[-6:] + str(generated_number))
    return unique_number


def get_short_url(remainder_list):
    short_url = ""
    for remainder in remainder_list:
        short_url += BASE_62_CONVERSION_MAPPING[remainder]
    return short_url


def generate_short_url(unique_id):
    remainders = []
    temp = unique_id
    while temp > 0:
        rem = temp % 62
        remainders.append(rem)
        temp = temp // 62
    short_url_mapping = get_short_url(remainders)
    return short_url_mapping
