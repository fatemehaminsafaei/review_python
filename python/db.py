import psycopg2


class database:
    def __init__(self):
        pass
    @staticmetod
    def create_tables():
        connection = psycopg2.connect(host='localhost',
                                      database='quize',
                                      user='postgres',
                                      password='mahnaz1376/01/28')
        cursor = connection.cursor()
        table_answer = [('short_answer_question', 'VARCHAR(100)'),
                        ('multiple_choice_question', 'INTEGER'),
                        ('true_false_question', 'Boolean')]
        for (table_name, answer) in table_answer:
            query_create_table = 'create table {}(' \
                                 'id serial PRIMARY KEY ,' \
                                 'question TEXT,' \
                                 'answer {});'.format(table_name, answer)
        cursor.execute(query_create_table)
        connection.commit()
