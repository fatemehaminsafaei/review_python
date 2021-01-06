import codecs
import csv
import urllib.request
import copy
from python.extend import ExtendList


def main():
    url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
    stream = urllib.request.urlopen(url)
    csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))

    iris_lst = []
    for row in csv_file:
        IRIS = ExtendList(row)
        iris_lst.append(IRIS)

    iris_lst = iris_lst[1:]

    for item in iris_lst:
        lst2 = []
        it = iter(ExtendList.NextVal(item))
        while True:
            try:
                lst2.append(next(it))
            except:
                break
        item.lst = lst2  # .deepcopy()

        print(item.lst)


if __name__ == '__main__':
    main()



# iris_lst2=[]
# for item in iris_lst:
# lst2 = []
# it = iter(ExtendedList.NextVal(item))
# while True:
# try:
# lst2.append(next(it))
# except StopIteration:
# break
# iris_lst2.append(lst2)
# print(iris_lst2)
