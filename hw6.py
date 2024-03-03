class SprintTeam:
    def calculate_velocity(self, previous_sprints):
        # Subtask 1: Sum up the completion points of previous sprints
        total_points_completed = sum(previous_sprints)
        # Subtask 2: Calculate the average velocity
        if not previous_sprints:
            return 0
        average_velocity = total_points_completed / len(previous_sprints)
        return average_velocity
    
    def calculate_effort_hour_capacity(self, num_sprint_days, team_members):
        total_available_hours = 0
        available_hours_per_person = []

        for member in team_members:
            # Subtask 1: Calculate the total number of available hours for each team member
            total_available_hours_per_member = (num_sprint_days - member['pto_days']) * member['hours_per_day']
            available_hours_per_person.append(total_available_hours_per_member)
            total_available_hours += total_available_hours_per_member

        # Subtask 2: Sum up the total available effort-hours for the team
        return available_hours_per_person, total_available_hours
    
# Test data
previous_sprints = [20, 30, 25, 28]
num_sprint_days = 10
team_members = [
    {'pto_days': 1, 'hours_per_day': 8},
    {'pto_days': 0, 'hours_per_day': 8},
    {'pto_days': 2, 'hours_per_day': 7}
]

sprint_team = SprintTeam()

# Feature A - Calculate sprint team's velocity
velocity = sprint_team.calculate_velocity(previous_sprints)
print("Average Velocity:", velocity)

# Feature B - Calculate Team Effort-Hour Capacity
effort_hours_per_person, total_effort_hours_team = sprint_team.calculate_effort_hour_capacity(num_sprint_days, team_members)
print("Available Effort-Hours per Person:", effort_hours_per_person)
print("Total Available Effort-Hours for Team:", total_effort_hours_team)
