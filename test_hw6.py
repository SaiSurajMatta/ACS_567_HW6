import unittest
from hw6 import SprintTeam

class TestCalculateVelocity(unittest.TestCase):

    def setUp(self):
        self.sprint_team = SprintTeam()

    def test_average_velocity_happy_path(self):
        previous_sprints = [20, 30, 25, 28]
        expected_velocity = 25.75
        self.assertEqual(self.sprint_team.calculate_velocity(previous_sprints), expected_velocity)

    def test_average_velocity_empty_list(self):
        previous_sprints = []
        expected_velocity = 0
        self.assertEqual(self.sprint_team.calculate_velocity(previous_sprints), expected_velocity)

class TestCalculateEffortHourCapacity(unittest.TestCase):

    def setUp(self):
        self.sprint_team = SprintTeam()

    def test_effort_hour_capacity_happy_path(self):
        num_sprint_days = 10
        team_members = [{'pto_days': 1, 'hours_per_day': 8}, {'pto_days': 0, 'hours_per_day': 8}, {'pto_days': 2, 'hours_per_day': 7}]
        expected_output = ([72, 80, 56], 208)
        self.assertEqual(self.sprint_team.calculate_effort_hour_capacity(num_sprint_days, team_members), expected_output)

    def test_effort_hour_capacity_edge_case(self):
        num_sprint_days = 10
        team_members = [{'pto_days': 10, 'hours_per_day': 8}]  # Team member taking the entire sprint off
        expected_output = ([0], 0)  # Expecting 0 hours for both individual and total team effort-hours
        self.assertEqual(self.sprint_team.calculate_effort_hour_capacity(num_sprint_days, team_members), expected_output)

if __name__ == '__main__':
    unittest.main()
