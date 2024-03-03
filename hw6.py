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