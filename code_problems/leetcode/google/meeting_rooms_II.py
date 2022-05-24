def min_meeting_room_self(intervals: list[list[int]]) -> int:
    start = [i[0] for i in intervals]
    end = [i[1] for i in intervals]
    start.sort()
    end.sort()

    start_ptr, end_ptr = 0, 0
    room_count = 0
    max_room = 0
    while start_ptr < len(start) and end_ptr < len(end):
        if start[start_ptr] < end[end_ptr]:
            room_count += 1
            start_ptr += 1
        else:
            room_count -= 1
            end_ptr += 1
        max_room = max(max_room, room_count)

    while start_ptr < len(start):
        room_count += 1
        start_ptr += 1

    while end_ptr < len(end):
        room_count -= 1
        end_ptr += 1

    return max_room


def min_meeting_room(intervals: list[list[int]]) -> int:
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    res, count = 0, 0
    s, e = 0, 0

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)

    return res


def test_case(test_input):
    intervals = test_input
    result = min_meeting_room(intervals)
    print(result)


def main():
    test_case([[0, 30], [5, 10], [15, 20]])  # 2
    test_case([[7, 10], [2, 4]])  # 1
    test_case([[5, 8], [6, 8]])  # 2
    test_case([[9, 10], [4, 9], [4, 17]])  # 2


if __name__ == "__main__":
    main()
