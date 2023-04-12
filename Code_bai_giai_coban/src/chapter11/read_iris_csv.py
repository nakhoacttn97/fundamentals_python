
from csv import reader

with open('iris_setosa.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        print(row)

from csv import reader

with open('iris_setosa.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    list_of_rows = list(csv_reader)

print(list_of_rows)    

