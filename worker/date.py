from datetime import datetime


def get_year():
    year = datetime.today().strftime('%Y')
    return year


def convert_datetime(date):
    if '/' in date:
        date = get_year() + '/' + date
        date = datetime.strptime(date, '%Y/%m/%d')
    elif '.' in date:
        date = get_year() + '/' + date
        date = datetime.strptime(date, '%Y/%m.%d')
        
    return date
