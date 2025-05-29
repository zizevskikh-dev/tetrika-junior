from typing import Dict, List, Set, Tuple


def appearance(lesson_data: Dict[str, List[int]]) -> int:
    """Calculates the effective lesson durations.

    For each lesson, computes the overlapping intervals during which both the pupil
    and tutor are present within the lesson timeframe. The total overlapping time is
    calculated and stored for each lesson.
    """
    lesson_start = lesson_data["lesson"][0]
    lesson_end = lesson_data["lesson"][1]
    pupil_intervals = _get_lesson_intervals_by_role(lesson=lesson_data, role="pupil")
    tutor_intervals = _get_lesson_intervals_by_role(lesson=lesson_data, role="tutor")

    connections = _get_connection_intervals(
        pupil_intervals, tutor_intervals, lesson_start, lesson_end
    )
    connections_intersected = _intersect_pure_intervals(connections)

    lesson_duration = sum(
        [connection[1] - connection[0] for connection in connections_intersected]
    )
    return lesson_duration


def _get_lesson_intervals_by_role(
    lesson: Dict[str, List[int]], role: str
) -> Set[Tuple[int, int]]:
    """Extracts login/logout time intervals for a given role.

    Args:
        lesson (Dict[str, List[int]]): A dictionary containing time intervals for all roles.
        role (str): The role to extract intervals for ('pupil' or 'tutor').

    Returns:
        List[Tuple[int, int]]: A list of (login, logout) time pairs.
    """
    logins = [interval for interval in lesson[role]][::2]
    logouts = [interval for interval in lesson[role]][1::2]
    return set(zip(logins, logouts))


def _get_connection_intervals(
    pupil_intervals: Set[Tuple[int, int]],
    tutor_intervals: Set[Tuple[int, int]],
    lesson_start: int,
    lesson_end: int,
) -> List[Tuple[int, int]]:
    """Computes overlapping intervals within the lesson timeframe.

    Args:
        pupil_intervals (List[Tuple[int, int]]): Time intervals for the pupil.
        tutor_intervals (List[Tuple[int, int]]): Time intervals for the tutor.
        lesson_start (int): Start timestamp of the lesson.
        lesson_end (int): End timestamp of the lesson.

    Returns:
        List[Tuple[int, int]]: A list of time intervals where both tutor and pupil
        are present and within the lesson time.
    """
    intervals = []
    for tutor_start, tutor_end in tutor_intervals:
        for pupil_start, pupil_end in pupil_intervals:
            connection_start = max(pupil_start, tutor_start, lesson_start)
            connection_end = min(pupil_end, tutor_end, lesson_end)

            if connection_start < connection_end:
                intervals.append((connection_start, connection_end))
    return intervals


def _intersect_pure_intervals(
    intervals: List[Tuple[int, int]],
) -> List[Tuple[int, int]]:
    """
    Реализацию слияния пересечений интервалов подсмотрел у GPT.
    Каюсь 🥺

    Пробовал реализовать через reduce() но сталкивался с исключениями при итерации.
    Надеюсь, мое откровение растопит ваше сердечко ❤️‍🔥
    """
    intervals.sort()
    intervals_intersected = [intervals[0]]

    for current_start, current_end in intervals[1:]:
        last_start, last_end = intervals_intersected[-1]
        if current_start <= last_end:
            intervals_intersected[-1] = (last_start, max(last_end, current_end))
        else:
            intervals_intersected.append((current_start, current_end))
    return intervals_intersected
