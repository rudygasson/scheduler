import scheduler 

def test_find_time_slots():
    BUSY_1 = [["9:00","10:30"], ["12:00","13:00"], ["16:00","18:00"]]
    BUSY_2 = [["10:00","11:30"], ["12:30","14:30"], ["14:30","15:00"], ["16:00","17:00"]]
    BOUND_P1 = ["9:00", "20:00"]
    BOUND_P2 = ["10:00", "18:30"]
    MEET_TIME = 30
    OUTPUT = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]

    assert scheduler.find_time_slots(BUSY_1, BOUND_P1, BUSY_2, BOUND_P2, MEET_TIME) == OUTPUT

def test_to_minutes():
    assert scheduler.to_minutes("9:10") == 9 * 60 + 10
    assert scheduler.to_minutes("0:60") == 60
    assert scheduler.to_minutes("23:50") == 23 * 60 + 50

def test_to_hour_string():
    assert scheduler.to_hour_string(0) == "00:00"
    assert scheduler.to_hour_string(1440) == "00:00"
    assert scheduler.to_hour_string(800) == "13:20"

def test_busy_number_list():
    BUSY_TIMES = [["10:00", "11:30"], ["12:00", "12:30"]]
    BOUNDARY = ["9:00", "20:00"]
    OUTPUT = [[0, 540], [600, 690], [720, 750], [1200, 1440]]
    assert scheduler.busy_number_list(BUSY_TIMES, BOUNDARY) == OUTPUT

def test_to_schedule_list():
    NUM_LIST = [[0, 60], [600, 630], [1000, 1200], [1230, 1440]]
    OUTPUT = [["00:00", "01:00"], ["10:00", "10:30"], ["16:40", "20:00"], ["20:30", "00:00"]]
    assert scheduler.to_schedule_list(NUM_LIST) == OUTPUT

def test_merge_independent():
    list_1 = [[480, 540], [660, 780]]
    list_2 = [[240, 360], [550, 660]]
    merged = [[240, 360], [480, 540], [550, 780]]
    assert scheduler.merge(list_1, list_2) == merged

def test_merge_list_1_longer():
    list_1 = [[480, 540], [660, 780], [800,900], [900,1000]]
    list_2 = [[240, 360], [550, 660]]
    merged = [[240, 360], [480, 540], [550, 780], [800,1000]]
    assert scheduler.merge(list_1, list_2) == merged

def test_merge_list_2_longer():
    list_1 = [[240, 360], [550, 660]]
    list_2 = [[480, 540], [660, 780], [800,900], [900,1000]]
    merged = [[240, 360], [480, 540], [550, 780], [800,1000]]
    assert scheduler.merge(list_1, list_2) == merged

def test_merge_overlapping():
    list_1 = [[480, 540], [660, 780]]
    list_2 = [[420, 510], [720, 810]]
    merged = [[420, 540], [660, 810]]
    assert scheduler.merge(list_1, list_2) == merged

def test_merge_containing():
    list_1 = [[480, 540], [660, 810]]
    list_2 = [[420, 660], [780, 810]]
    merged = [[420, 810]]
    assert scheduler.merge(list_1, list_2) == merged 

def test_merge_boundaries():
    list_1 = [[0, 480], [1200, 1440]]
    list_2 = [[0, 660], [1100, 1360]]
    merged = [[0, 660], [1100, 1440]]
    assert scheduler.merge(list_1, list_2) == merged

def test_free_slots_small():
    busy_times = [[0, 480], [500,1200]]
    assert scheduler.free_slots(busy_times, 30) == [[1200, 1440]]

def test_free_slots_not_free():
    busy_times = [[0,600], [630,1000], [1030,1400]]
    assert scheduler.free_slots(busy_times, 60) == []

def test_free_slots_multiple_free():
    busy_times = [[400, 600], [900, 960], [1000,1100]]
    assert scheduler.free_slots(busy_times, 30) == [[0, 400], [600, 900], [960, 1000], [1100, 1440]]
