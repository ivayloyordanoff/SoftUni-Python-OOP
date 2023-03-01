from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            current_task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        current_task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = [current_task for current_task in self.tasks if current_task.completed]
        self.tasks = [current_task for current_task in self.tasks if not current_task.completed]

        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        section_info = [f"Section {self.name}:"]

        for current_task in self.tasks:
            section_info.append(current_task.details())

        return "\n".join(section_info)
