class SprintTeam:
    def calculate_velocity(self, previous_sprints):
        # Subtask 1: Sum up the completion points of previous sprints
        total_points_completed = sum(previous_sprints)
        # Subtask 2: Calculate the average velocity
        if not previous_sprints:
            return 0
        average_velocity = total_points_completed / len(previous_sprints)
        return average_velocity