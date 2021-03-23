import re


pattern = {
    'school'  : '\[공통\]|\[서울\]|\[글로벌\]|\(공통\)|\(서울\)|\(글로벌\)',
    'option'  : '\[교외\]|\[국가\]|\[교내\]|\[국가근로\]|\[기금\]|\[대출\]|\(교외\)|\(국가\)|\(교내\)|\(국가근로\)|\(기금\)|\(대출\)',
    'date'    : '(\~[0-9]\/[0-9]+)|(\~\s[0-9]\/[0-9]+)',
    'date_sub': '(\(~\))|(\(~\s\))'
}


def remove_option_special_character(string):
    if string:
        string = string[0].lstrip('/[').lstrip('\]').rstrip('\]').rstrip('\)')
    else:
        string = "미지정"

    return string


def remove_date_special_character(date):
    if date:
        if date[0][0]:
            date = date[0][0].lstrip('~').strip()
        elif date[0][1]:
            date = date[0][1].lstrip('~').strip()
    else:
        date = ""
    
    return date


def find_by_pattern(pattern, data):
    result = re.findall(pattern, data)

    return result


def sub_option(pattern, data):
    result = re.sub(pattern, "", data)
    result = result.rstrip('~').strip()

    return result


def sub_date(data, date, pattern = pattern['date_sub']):
    data = data.replace(date, "")
    data = re.sub(pattern, "", data)

    return data