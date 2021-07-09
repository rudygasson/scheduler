# Given two different day schedules
# And two different availability windows for the day
# And a duration for a meeting to be scheduled
# Find the time slots that are available and long enough for both schedules
#
# Sample Input:
# Person 1 
# Schedule:         [["9:00","10:30"], ["12:00","13:00"], ["16:00","18:00"]]
# Availability:     ["9:00", "20:00"]
# Person 2 
# Schedule:         [["10:00","11:30"], ["12:30","14:30"], ["14:30","15:00"], ["16:00","17:00"]]
# Availability:     ["10:00", "18:30"]
# Meeting duration: 30
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
    merged_list = number_list_1 + number_list_2
    merged_list.sort()
   
    # Merge two slots if they overlap
    squashed = [merged_list[0]]
    index = 0
    for slot in merged_list:
        if slot[0] > squashed[index][1]:   # Slots do not overlap
            squashed.append(slot)
            index += 1
        elif slot[1] > squashed[index][1]: # Slots overlap
            squashed[index][1] = slot[1]

    return squashed

def free_slots(busy_times, duration):
    print(busy_times)
    free = []
    if busy_times[0][0] > duration:
        free.append([0, busy_times[0][0]])
    i = 0
    while i < len(busy_times) - 1:
        if busy_times[i+1][0] - busy_times[i][1] >= duration:
            free.append([busy_times[i][1], busy_times[i+1][0]])
        i += 1
    if 1440 - busy_times[i][1] > duration:
        free.append([busy_times[i][1], 1440])

    return free

def to_schedule_list(number_array):
    schedule_list = []
    for slot in number_array:
        schedule_list.append(
            [to_hour_string(slot[0]), to_hour_string(slot[1])])
    return schedule_list
