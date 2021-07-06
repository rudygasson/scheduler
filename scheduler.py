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

    return convert_to_schedule_array(available)


def convert_to_minutes(time_string):
    hours = int(time_string.split(":")[0])
    minutes = int(time_string.split(":")[1])
    return hours * 60 + minutes


def busy_number_list(busy_array, boundary_time):
    number_list = [[0, convert_to_minutes(boundary_time[0])]]
    for slot in busy_array:
        number_list.append([
            convert_to_minutes(slot[0]),
            convert_to_minutes(slot[1])
        ])
    number_list.append([convert_to_minutes(boundary_time[1]), 1440])
    return number_list


def merge(s1, s2):

    return


def free_slots(busy_times, duration):
    return


def convert_to_schedule_array(number_array):
    return 
