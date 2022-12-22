class Task:
    def __init__(self, name, completed, max_score):
        self.name = name
        self.completed = completed
        self.max_score = max_score


class AllOrNothing(Task):
    def __init__(self, name, completed, max_score):
        super().__init__(name, completed, max_score)


class FasterIsBetter(Task):
    def __init__(self, name, completed, max_score, time_to_solve, score_for_task, percent, time_of_participant):
        super().__init__(name, completed, max_score)
        self.time_to_solve = time_to_solve
        self.score_for_task = score_for_task
        self.percent = percent
        self.time_of_participant = time_of_participant


class Participant:
    def __init__(self, name, tasks, total):
        self.name = name
        self.tasks = tasks
        self.total = total