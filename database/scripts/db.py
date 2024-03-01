import sqlite3


class Data:
    def __init__(self, filename):
        self.filename = filename
        self.connect()

    def connect(self):
        self.db = sqlite3.connect(self.filename)
        self.cur = self.db.cursor()

    def send_request(self, task):
        try:
            request = """SELECT Tasks.question, Axioms.text, Answers.right, Tasks.image FROM Answers
                         JOIN Axioms ON Axioms.axiom_id = Answers.axiom_id
                         JOIN Tasks ON Tasks.task_id = Answers.task_id
                         WHERE Answers.task_id = ?"""
            self.data = self.cur.execute(request, (task, )).fetchall()
        except sqlite3.Error as e:
            print(e)


    def get_task(self, task):
        self.send_request(task)
        return self.data