import sqlite3


class Data:
    def __init__(self, filename):
        self.data = []
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

    def get_all_answers(self):
        try:
            request = """SELECT text FROM Axioms"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_task(self, task):
        self.send_request(task)
        return self.data

    def get_all_tasks(self):
        try:
            request = """SELECT task_id, question, image FROM Tasks"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def add_question(self, **kwargs):
        try:
            sqlite_insert_query = """INSERT INTO Answers (axioms_id, task_id, right)
                                      VALUES (?, ?, ?);"""
            data = (kwargs['axioms_id'], kwargs['task_id'], kwargs['right'])
            self.cur.execute(sqlite_insert_query, data)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def add_answer(self, **kwargs):
        try:
            sqlite_insert_query = """INSERT INTO Axioms (group, text)
                                      VALUES (?, ?);"""
            data = (kwargs['group'], kwargs['text'])
            self.cur.execute(sqlite_insert_query, data)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)
