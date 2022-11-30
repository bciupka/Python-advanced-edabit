import os
import functools

def wrapperParam(logPath, action):
    def wrapper(fun):
        def newFun(newPath):
            from datetime import datetime
            fun(newPath)
            with open(logPath, 'a') as file:
                file.write('Action: {} executed on {} on {}\n'.format(action, newPath, datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")))
        return newFun
    return wrapper

# Małpa działą na zasadzie wykorzystania nazwy funkcji poniżej małpy w nawiasie za treścią przy małpie,
# parametru funkcji poniżej w nawiasie za nawiasem z nazwą funkcji za treścią przy małpie itd.

@wrapperParam(r'D:\Projekty\PyCharm\temp\S04-L02\create_log.txt', 'FILE_CREATE')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+").close()

# Podwójne przepisanie funkcji, pierwsze powoduje zapamiętanie parametrów i przejście do wrappera,
# drugie powoduje uruchomienie wrappera z nazwą funkcji jako parametrem

create_wrap = wrapperParam(r'D:\Projekty\PyCharm\temp\S04-L02\create_log.txt', 'FILE_CREATE_WRAP')(create_file)

@wrapperParam(r'D:\Projekty\PyCharm\temp\S04-L02\delete_log.txt', 'FILE_DELETE')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)

delete_wrap = wrapperParam(r'D:\Projekty\PyCharm\temp\S04-L02\delete_log.txt', 'FILE_DELETE_WRAP')(delete_file)

create_file(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')
delete_file(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')
create_file(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')
delete_file(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')

# create_wrap(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')
# delete_wrap(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')
# create_wrap(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')
# delete_wrap(r'D:\Projekty\PyCharm\temp\S04-L02\dummy_file.txt')
