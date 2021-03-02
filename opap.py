import json
import requests
from datetime import date, timedelta
import statistics  

"""finding dates of the 1st day of this month and today"""
firstDay = date.today().replace(day=1)
lastDay = date.today()

"""function for getting all the winning numbers for a specific date via OPAP's API"""
def get_winning_numbers(date: str):
    url = f'https://api.opap.gr/draws/v3.0/1100/draw-date/{date}/{date}'
    r = requests.get(url).json()
    winning_numbers = [game['winningNumbers']['list'] for game in r['content']]
    return winning_numbers

"""function for finding the most frequent element in a list"""
def most_frequent(List): 
    return max(set(List), key = List.count) 
  
"""getting all the winning numbers for this month"""
all_numbers_nested = []
day_counter = firstDay
while day_counter <= lastDay:
    all_numbers_nested += get_winning_numbers(day_counter.strftime("%Y-%m-%d"))
    day_counter += timedelta(days=1)

"""converting the nested list to a flat list"""
all_numbers_flat = []
for elem in all_numbers_nested:
    all_numbers_flat.extend(elem)
    
print("The most frequent number appeared on this month's KINO draws is:", most_frequent(all_numbers_flat))