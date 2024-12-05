import threading
import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        while True:
            stroka=file.readline()
            all_data.append(stroka)
            if stroka=="":
                break




filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Линейный вызов
"""start_time=time.time()
for i in filenames:
    read_info(i)
print(time.time()-start_time)"""
# Многопроцессный
if __name__== '__main__':
    start_time = time.time()
    #замена
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(time.time() - start_time)
