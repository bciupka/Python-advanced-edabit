# 1

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for i, j in zip(projects, leaders):
    print('The leader of', i, 'is', j)

# 2

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for i, j, k in zip(dates, projects, leaders):
    print('The leader of', j, 'started', i, 'is', k)

# 3

for x, (i, j, k) in enumerate(zip(dates, projects, leaders)):
    print(x+1, '-', 'The leader of', j, 'started', i, 'is', k)
