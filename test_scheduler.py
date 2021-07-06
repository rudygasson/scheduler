import scheduler 

def test_find_time_slots():
    BUSY_1 = [["9:00","10:30"], ["11:30","12:30"], ["13:30","15:00"], ["9:00","10:30"]]
    BUSY_2 = [["11:00","12:30"], ["13:00","14:00"], ["9:00","10:30"], ["9:00","10:30"]]
    BOUND_P1 = ["9:00", "20:00"]
    BOUND_P2 = ["10:00", "18:30"]
    MEET_TIME = 30
    OUTPUT = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]

    assert scheduler.find_time_slots(BUSY_1, BOUND_P1, BUSY_2, BOUND_P2, MEET_TIME) == OUTPUT

def test_convert_to_minutes():
    assert scheduler.convert_to_minutes("9:10") == 9 * 60 + 10
    assert scheduler.convert_to_minutes("0:60") == 60
    assert scheduler.convert_to_minutes("23:50") == 23 * 60 + 50

def test_busy_number_list():
    BUSY_TIMES = [["10:00", "11:30"], ["12:00", "12:30"]]
    BOUNDARY = ["9:00", "20:00"]
    OUTPUT = [[0, 540], [600, 690], [720, 750], [1200, 1440]]
    assert scheduler.busy_number_list(BUSY_TIMES, BOUNDARY) == OUTPUT
