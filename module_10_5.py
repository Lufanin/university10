from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        while data:
            data = file.readlines()
            all_data.append(data[0:-1])
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.now()
# read_info(filenames[0])
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])
# end = datetime.now()
# print(f'{end - start} (линейный)')


if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'{end - start} (параллельный)')

