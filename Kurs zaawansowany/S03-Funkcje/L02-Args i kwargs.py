# 1

def calculate_paint(efficiency, *area):
    print('Ilość farby: ', sum(area) * efficiency)

calculate_paint(1, 30, 30, 40, 10)
calculate_paint(2, *(30,70))
calculate_paint(2, *[30,70])


rooms = [10, 30, 20, 40, 10]

calculate_paint(2, *rooms)

# 2

def log_it(*args):
    import os
    path = r'D:\Projekty\PyCharm\temp\S03-L02'
    filename = 'log'
    file_path = os.path.join(path, filename+'.txt')
    with open(file_path, 'a') as file:
        for i in args:
            if i != args[len(args) - 1]:
                file.write(i+', ')
            else:
                file.write(i+'\n')

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')

# testy

def give(**x):
    print('To jest:', x)

y = {'a':1, 'b':2, 'c':3}

give(a=1, b=2, c=3)
give(**y)
