import csv

with open(r'D:\Projekty\PyCharm\temp\S08-L03\123.csv', newline='') as csvfile: # newline = '' oznacza, żę znak nowych lini nie jest tłumaczony na \n, \r, \r\n
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row)) # | łączy stringi podane jako argumenty w funkcji join
    while True:
        try:
            print(','.join(next(csvreader)))
        except StopIteration:
            break


