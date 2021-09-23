# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:51:02 2021

@author: Anon
"""

gamers = []


def add_gamer(gamer, gamers_list):
    assert 'name' in gamer and 'availability' in gamer, 'Gamer needs a name and availability'
    gamers_list.append(gamer)
    

kimberly = {'name': 'Kimberly Warner', 'availability': ['Monday','Tuesday','Friday']}
add_gamer(kimberly, gamers)


add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


def build_daily_frequency_table():
    return {'Sunday':0, 'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0}

count_availability = build_daily_frequency_table()


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)

print(count_availability)

def find_best_night(availability_table):
    days = []
    target = max(availability_table.values())
    for day, availability in availability_table.items():
        if availability == target:
            days.append(day)
    return days

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    names = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            names.append(gamer['name'])
    return names

attending_game_night = available_on_night(gamers, game_night[0])
print(attending_game_night)


form_email = 'Good news {name}! We have a schedule on {day_of_week} to play "{game}"'


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, day_of_week = day, game = game))

send_email(attending_game_night, game_night[0], 'Abruptly Goblins!')

print('\n\n***second night***\n\n')
unable_to_attend_best_night = [gamer for gamer in gamers if gamer['name'] not in attending_game_night]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
print(second_night)

available_second_game_night = available_on_night(gamers, second_night[0])

send_email(available_second_game_night, second_night, 'Abruptly Goblins!')