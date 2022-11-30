import datetime as dt

class TripException(Exception):


    def __init__(self, text, description):
        super().__init__(text)
        self.description = description

    def __str__(self):
        return '{}, Aadditional info - {}'.format(super().__str__(), self.description)

class TripNameException(TripException):


    def __init__(self, text):
        super().__init__(text, 'Name is missing')

class TripDateException(TripException):


    def __init__(self, text):
        super().__init__(text, 'The Start date is later than the end date')


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException('Name Exeption')
        if self.start > self.end:
            raise TripDateException('Date Exception')

    @classmethod
    def publish_offer(cls, listOfTrips):
        list_of_errors = []
        for i in listOfTrips:
            try:
                i.check_data()
            except TripNameException as e:
                list_of_errors.append('{} : {}'.format(i.symbol, e))
            except TripDateException as e:
                list_of_errors.append('{} : {}'.format(i.symbol, e))
        if list_of_errors:
                raise TripException('Data error', list_of_errors)
        else:
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