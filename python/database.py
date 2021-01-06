import peycopg2

conn = psycopg2.connect(host="localhost",
                        port="5432",
                        database="iris",
                        user="postgres",
                        password="danial1393")

insert_query = "INSERT INTO iris (sepal_l,sepal_w,petal_l,petal_w,class) " \
"VALUES {},{},{},{},{}".format(one_row[0], one_row[1], one_row[2], one_row[3],
target[iris_lst.index(line)])
cursor = conn.cursor()
cursor.execute(insert_query)

#
# cursor = conn.cursor()
# select_query2 = "insert into iris_table(sepal_length,sepal_width,petal_length,petal_width,variety) values {}".format(
# tuple(lst2))
# cursor.execute(select_query2)
# conn.commit()

