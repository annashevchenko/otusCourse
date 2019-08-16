import random
import sys

date = ['+', '-']
sym_generator = (random.choice(date) for i in range(sys.maxsize ** 10))
line_List = [line.rstrip('\n') for line in open('data.csv', 'r')]
fio_List = [line.split(',')[0].strip() for line in line_List]
city_List = [line.split(',')[1].strip() for line in line_List]
fio_generator = (random.choice(fio_List) for i in range(sys.maxsize ** 10))
city_generator = (random.choice(city_List) for i in range(sys.maxsize ** 10))

with open('result.txt', 'w') as my_file_result:
    for x in range(100):
        line = fio_generator.__next__() + ', ' + city_generator.__next__() \
               + '\t' + sym_generator.__next__() \
               + '\t' + sym_generator.__next__() \
               + '\t' + sym_generator.__next__() \
               + '\n'
        my_file_result.write(line)
