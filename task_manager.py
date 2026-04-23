class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def get_completion_rate(self):
        if len(self.tasks) == 0:
            return 0
        completed = 0
        for t in self.tasks:
            if t["completed"]:
                completed += 1
        return completed / len(self.tasks)
