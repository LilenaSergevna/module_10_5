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
    proc1=multiprocessing.Process(target=read_info, args=(filenames[0],))
    proc2=multiprocessing.Process(target=read_info, args=(filenames[1],))
    proc3=multiprocessing.Process(target=read_info, args=(filenames[2],))
    proc4=multiprocessing.Process(target=read_info, args=(filenames[3],))
    proc1.start()
    proc2.start()
    proc3.start()
    proc4.start()
    proc1.join()
    proc2.join()
    proc3.join()
    proc4.join()
    print(time.time() - start_time)