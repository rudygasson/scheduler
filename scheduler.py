# Given two different day schedules
# And two different time boundaries for the day
# And a duration for a meeting to be scheduled
# Find the time slots that are available and long enough for both schedules
#
# Sample Input:
# [["9:00","10:30"], ["12:00","13:00"], ["16:00","18:00"]]
# ["9:00", "20:00"]
# [["10:00","11:30"], ["12:30","14:30"], ["14:30","15:00"], ["16:00","17:00"]]
# ["10:00", "18:30"]
# 30
#
# Sample Output:
# [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]


def find_time_slots(busy_p1, bound_p1, busy_p2, bound_p2, time_requested):
    schedule_p1 = busy_number_list(busy_p1, bound_p1)
    schedule_p2 = busy_number_list(busy_p2, bound_p2)
    busy = merge(schedule_p1, schedule_p2)
    available = free_slots(busy, time_requested)

    return to_schedule_list(available)


def to_minutes(time_string):
    hours = int(time_string.split(":")[0])
    minutes = int(time_string.split(":")[1])
    return hours * 60 + minutes

def to_hour_string(minutes_sum):
    hours = minutes_sum // 60 % 24
    minutes = minutes_sum % 60
    return f'{hours:02}:{minutes:02}'
    
def busy_number_list(busy_array, boundary_time):
    number_list = [[0, to_minutes(boundary_time[0])]]
    for slot in busy_array:
        number_list.append([
            to_minutes(slot[0]),
            to_minutes(slot[1])
        ])
    number_list.append([to_minutes(boundary_time[1]), 1440])
    return number_list

def merge(number_list_1, number_list_2):
    return

def free_slots(busy_times, duration):
    return

def to_schedule_list(number_array):
    schedule_list = []
    for slot in number_array:
        schedule_list.append([to_hour_string(slot[0]), to_hour_string(slot[1])])
    return schedule_list
