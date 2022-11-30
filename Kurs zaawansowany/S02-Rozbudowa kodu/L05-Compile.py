import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)


results_list = []

for formula in formulas_list:
    print('Aktualny wzór: ', formula)
    start = time.time()
    for x in argument_list: ## Jako argument for - x. Dzięki temu bezpośrednie wykorzystanie we wzorze.
        results_list.append(eval(formula))
    print('Min = {}, Max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    time_nc = stop - start

results_list = []

for formula in formulas_list:
    print('Aktualny wzór: ', formula)
    start = time.time()
    compiled = compile(formula, 'in program str', 'eval')
    for x in argument_list:
        results_list.append(eval(compiled))
    print('Min = {}, Max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    time_c = stop - start

print(time_nc, time_c, time_nc/time_c, sep='\n')