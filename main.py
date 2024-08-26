class Task():
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = 0
    def mark_task_done(self):
        self.status = 1
    def print_all_tasks_undone(self):
        if self.status == 0:
            print(self.name, self.description, self.due_date, self.status)
tasks = []
tasks.append(Task('Первая задача', 'Описание задачи', '01.09.2024'))
tasks.append(Task('Вторая задача', 'Описание задачи', '02.09.2024'))
tasks.append(Task('Третья задача', 'Описание задачи', '03.09.2024'))

tasks[1].mark_task_done()

for task in tasks:
    task.print_all_tasks_undone()