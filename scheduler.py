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
    len1 = len(number_list_1)
    len2 = len(number_list_2)
    index1 = index2 = 0
    index_m = 0
    merged_list = []
    while index1 < len1 and index2 < len2:
        print(index1, index2)
        if number_list_1[index1][0] <= number_list_2[index2][0]:
            merged_list.append([number_list_1[index1][0], 0])
            if number_list_1[index1][1] < number_list_2[index2][0]:
                # l1 and l2 separate
                merged_list[index_m][1] = number_list_1[index1][1]
                index1 += 1
                index_m += 1
            elif number_list_1[index1][1] <= number_list_2[index2][1]:
                # l1 overlaps l2 left
                merged_list[index_m][1] = number_list_2[index2][1]
                index1 += 1
                index2 += 1
                index_m += 1
            else:
                # l1 contains l2
                merged_list[index_m][1] = number_list_1[index1][1]
                index1 += 1
                index2 += 1
                index_m += 1
        else:
            # l2 < l1
            merged_list.append([number_list_2[index2][0], 0])
            if number_list_2[index2][1] < number_list_1[index1][0]:
                # l2 and l1 separate
                merged_list[index_m][1] = number_list_2[index2][1]
                index2 += 1
                index_m +=1
            elif number_list_2[index2][1] <= number_list_1[index1][1]:
                # l2 overlaps l1 left
                merged_list[index_m][1] = number_list_1[index1][1]
                index2 += 1
                index1 += 1
                index_m += 1
            else:
                # l2 contains l1
                merged_list[index_m][1] = number_list_2[index2][1]
                index2 += 1
                index1 += 1
                index_m += 1
            
    return merged_list

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
        schedule_list.append([to_hour_string(slot[0]), to_hour_string(slot[1])])
    return schedule_list
