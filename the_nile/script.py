# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:03:45 2021

@author: =GV=
"""
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function


def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    from_lat, from_long = from_coords
    to_lat, to_lat = to_coords
    distance = get_distance(*from_coords, *to_coords)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    return format_price(price)


def calculate_driver_cost(distance, *drivers):
    pass

# Test the function by calling 
# test_function(calculate_driver_cost)

# Define calculate_money_made() here


# Test the function by calling 
# test_function(calculate_money_made)
