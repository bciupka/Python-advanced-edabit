# 1

price = 123
bonus = 23
bonus_granted = True

print(price - bonus) if bonus_granted else print(price)

print(price - bonus if bonus_granted else price)

price = price - bonus if bonus_granted else price
print(price)

# 2

rating = 5

print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')

# 3

day = 2

if day == 1:
    print('Pomagam mamie')
elif day == 2 or day == 3:
    print('Ty masz w domu pranie')
elif day == 4:
    print('Mam dyżur')
elif day == 5:
    print('Mam dwa zebrania')
elif day == 6:
    print('Ty na lekcje ganiasz')
else:
    print('Niedziela będzie dla nas')


print('Pomagam mamie' if day == 1 else
      'Ty masz w domu pranie' if day == 2 or day == 3 else
      'Mam dyżur' if day == 4 else 'Mam dwa zebrania' if day ==5 else
      'Ty na lekcje ganiasz' if day == 6 else 'Niedziela będzie dla nas')

import datetime as dt

today_weekday = dt.date.today().strftime("%A")

print(today_weekday)

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")

print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")
