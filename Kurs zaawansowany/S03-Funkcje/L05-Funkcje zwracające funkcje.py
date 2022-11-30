# używając if

def calculate(unit, date1, date2):
    import datetime
    x = datetime.timedelta.total_seconds(date1 - date2)
    if unit == "m":
        x = x/60
        print('Ilość minut:', round(x,2))
    elif unit =='h':
        x = x/60/60
        print('Ilość godzin:', round(x,2))
    elif unit == 'd':
        x = x/60/60/24
        print('Ilość dni:', round(x,2))


# używając 3 funkcji

def calulate_m(date1, date2):
    import datetime
    x = datetime.timedelta.total_seconds(date1 - date2)
    x = x/60
    print('Ilość minut:', round(x, 2))

def calulate_h(date1, date2):
    import datetime
    x = datetime.timedelta.total_seconds(date1 - date2)
    x = x/60/60
    print('Ilość godzin:', round(x, 2))

def calulate_d(date1, date2):
    import datetime
    x = datetime.timedelta.total_seconds(date1 - date2)
    x = x/60/60/24
    print('Ilość dni:', round(x, 2))


# używając funkcji tworzącej

def beCreative(unit):
    import datetime
    divide = {'m':60, 'h':60*60, 'd':60*60*24}
    text = {'m':'minut', 'h':'godzin', 'd':'dni'}
    fun = '''def calc(date1, date2):
    x = datetime.timedelta.total_seconds(date1 - date2)
    x = x/{0:d}
    #print('Ilość {1:s}: %.2f' % round(x, 2))
    print('Ilość {1:s}:', round(x, 2))  
'''.format(divide[unit], text[unit])
    exec(fun, globals())
    return calc


import datetime

date1 = datetime.datetime(2021, 9, 14)
date2 = datetime.datetime.now()

calculate('m', date1, date2)
calculate('h', date1, date2)
calculate('d', date1, date2)
print(30*'-')
calulate_m(date1, date2)
calulate_h(date1, date2)
calulate_d(date1, date2)
print(30*'-')
minutes = beCreative('m')
hours = beCreative('h')
days = beCreative('d')
minutes(date1, date2)
hours(date1, date2)
days(date1, date2)