import datetime as dt

# SET PYTHONOPTIMZE=TRUE/SET PYTHONOPTIMIZE=  - dla Windowsa
# PYTHONOPTIMIZE=TRUE/PYTHONOPTIMIZE=  - dla Unixów
# Te zmienne środowiskowe 'wyłączeją' sprawdzanie assert, jest ono pomijane. Assert przydaje się w srodowisku TST/DEV, inaczej jest zbyt łatwe do obejścia.

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) != 0, "Title is empty!"
        assert self.start <= self.end, "Start date is later than end date!"

    @classmethod
    def publish_offer(cls, listOfTrips):
        list_of_errors = []
        for i in listOfTrips:
            try:
                i.check_data()
            except ValueError as e:
                list_of_errors.append('{} : {}'.format(i.symbol, e))
            except Exception as e:
                list_of_errors.append('{} : {}'.format(i.symbol, e))
        assert not list_of_errors, 'List of errors:\n{}'.format(list_of_errors)
        print('Publishing...')





trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]


try:
    print('Checking...')
    Trip.publish_offer(trips)
    print('Done!')
except Exception as e:
    print('Problem:\n{}'.format(e))