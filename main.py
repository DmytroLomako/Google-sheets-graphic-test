from modules import *
from random import randint

connection = connect('sheets', 'v4')
data = []
for i in range(COUNT_VALUE):
    value = [randint(0, MAX_VALUE)]
    data.append(value)
write_data(connection, SPREADSHEET_ID, data, RANGE_NAME)
result = read_data(connection, RANGE_NAME, SPREADSHEET_ID)
for index, value in enumerate(result):
    result[index] = int(value[0])
result = sorted(result)
data_dict = {}
for i in range(MAX_VALUE + 1):
    data_dict[i] = result.count(i)
print(data_dict)
create_graphic(data_dict.values(), 'green', 'Graphic', COUNT_VALUE)