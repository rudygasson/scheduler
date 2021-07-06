import scheduler 

def test_find_time_slots():
    BUSY_1 = [["9:00","10:30"], ["11:30","12:30"], ["13:30","15:00"], ["9:00","10:30"]]
    BUSY_2 = [["11:00","12:30"], ["13:00","14:00"], ["9:00","10:30"], ["9:00","10:30"]]
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
