import unittest
from consultation import build_consultation_schedule

class TestConsultation(unittest.TestCase):
    def test_normal_case(self):
        intervals = ["09:00", "10:00"]
        requests = [{"name": "Sidorov"}, {"name": "Bondar"}]
        expected = [{"name": "Sidorov", "time": "09:00"}, {"name": "Bondar", "time": "10:00"}]
        self.assertEqual(build_consultation_schedule(intervals, requests), expected)

    def test_more_students_than_intervals(self):
        intervals = ["12:00"]
        requests = [{"name": "A"}, {"name": "B"}]
        result = build_consultation_schedule(intervals, requests)
        self.assertEqual(result[1]["time"], None)

if __name__ == "__main__":
    unittest.main()