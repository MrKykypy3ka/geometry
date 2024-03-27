import sqlite3


class Data:
    def __init__(self, filename):
        self.data = []
        self.filename = filename
        self.connect()

    def connect(self):
        self.db = sqlite3.connect(self.filename)
        self.cur = self.db.cursor()

    def get_task(self, task):
        try:
            request = """SELECT Tasks.question, Statements.text, Answers.right, Tasks.image FROM Answers
                         JOIN Statements ON Statements.statement_id = Answers.statement_id
                         JOIN Tasks ON Tasks.task_id = Answers.task_id
                         WHERE Answers.task_id = ?"""
            self.data = self.cur.execute(request, (task, )).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_all_answers(self):
        try:
            request = """SELECT statement_id, text FROM Statements"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_all_tasks(self):
        try:
            request = """SELECT task_id, question, image FROM Tasks"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def get_all_topic(self):
        try:
            request = """SELECT topic_id, topic FROM Topics"""
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            print(e)

    def add_question(self, **kwargs):
        try:
            sqlite_insert_query = """INSERT INTO Tasks (question, image)
                                      VALUES (?, ?);"""
            data = (kwargs['question'], kwargs['image'])
            self.cur.execute(sqlite_insert_query, data)
            self.db.commit()
        except sqlite3.Error as e:
            print(e)

    def add_answer(self, **kwargs):
        try:
            sqlite_insert_query = """INSERT INTO Answers (statement_id, task_id, right)
                                      VALUES (?, ?, ?);"""
            data = (kwargs['statement_id'], kwargs['task_id'], kwargs['right'])
            self.cur.execute(sqlite_insert_query, data)
            self.db.commit()
            return True
        except sqlite3.Error as e:
            print(e)

    def add_statement(self, **kwargs):
        try:
            sqlite_insert_query = """INSERT INTO Statements (topic_id, text)
                                      VALUES (?, ?);"""
            data = (kwargs['topic_id'], kwargs['text'])
            self.cur.execute(sqlite_insert_query, data)
            self.db.commit()
            return True
        except sqlite3.Error as e:
            print(e)
