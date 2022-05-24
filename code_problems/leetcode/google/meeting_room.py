def can_attend_meetings_self(intervals: list[list[int]]) -> bool:
    """didn't work, keep as remainder"""
    if len(intervals) <= 1:
        return True
    attend = intervals[0]
    can_attend = True
    for i in range(1, len(intervals)):
        if (intervals[i][0] >= min(attend) and intervals[i][0] < max(attend)) or (
            intervals[i][1] > min(attend) and intervals[i][1] <= max(attend)
        ):
            can_attend = False
        else:
            attend.extend(intervals[i])

    return can_attend


def can_attend_meetings(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True


def main():
    intervals = [[0, 30], [5, 10], [15, 20]]
    result = can_attend_meetings(intervals)
    print(result)  # False

    intervals = [[7, 10], [2, 4]]
    result = can_attend_meetings(intervals)
    print(result)  # True

    intervals = [[9, 10], [4, 9], [4, 17]]
    result = can_attend_meetings(intervals)
    print(result)  # False

    intervals = [[13, 15], [1, 13]]
    result = can_attend_meetings(intervals)
    print(result)  # True

    intervals = [[12, 13], [6, 11], [2, 19]]
    result = can_attend_meetings(intervals)
    print(result)  # False


if __name__ == "__main__":
    main()
