def build_consultation_schedule(intervals: list[str], requests: list[dict]) -> list[dict]:
    """
    Призначає час консультації для кожного студента.
    
    >>> intervals = ["10:00", "11:00"]
    >>> requests = [{"name": "Ivanov"}, {"name": "Petrov"}]
    >>> build_consultation_schedule(intervals, requests)
    [{'name': 'Ivanov', 'time': '10:00'}, {'name': 'Petrov', 'time': '11:00'}]
    """
    result = []
    for i in range(len(requests)):
        student_name = requests[i].get("name")
        # Якщо інтервалів менше, ніж студентів, ставимо None
        assigned_time = intervals[i] if i < len(intervals) else None
        result.append({"name": student_name, "time": assigned_time})
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()