days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()

# workdays[5:] = []
workdays.remove('sun')
workdays.remove('sat')


print(days, workdays, sep='\n')