# # 1

options = {1:'load data', 2:'export data', 3:'analyze & predict'}

choice = input('1 - Load, 2 - Export, 3 - Predict\nWprowadź swój wybór: ')


while choice:
    try:
        print(options[int(choice)])
        break
    except ValueError as e:
        print('Wpisz liczbę!!!', e)
        break
    except KeyError:
        print('Wartość poza zakresem (1-3) !!!')
        choice = input('1 - Load, 2 - Export, 3 - Predict\nWprowadź swój wybór: ')

# 2
choice = 'x'

def DisplayOptions(list):
    x = input('1 - {0:s}\n2 - {1:s}\n3 - {2:s}\nSelect option above or press enter to exit: '.format(list[0],list[1],list[2]))
    return x

opt = ['load data', 'export data', 'analyze & predict']
while choice:
    choice = DisplayOptions(opt)
    if choice:
        try:
            choice_num = int(choice)
            if choice_num > 0 and choice_num <= len(opt):
                print(opt[choice_num-1])
                break
            else:
                print('Dokonano wyboru poza zakresem (1-3)')
        except:
            print('Koniec zabawy!')
            break
