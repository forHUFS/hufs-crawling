import pymysql

from config import SQL_INFO


def create_connection(db_info = SQL_INFO):
    conn   = pymysql.connect(**db_info)
    cursor = conn.cursor()

    return conn, cursor


def close_connection():
    conn, _ = create_connection()
    conn.close()


def find_data(table, column, value):
    conn, cursor = create_connection()

    query = f'SELECT id FROM {table} WHERE ({column} = "{value}")'
    cursor.execute(query)
    conn.commit()
    
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False


def get_id(table, column, value):
    conn, cursor = create_connection()

    if isinstance(value, str):
        query = f'SELECT id FROM {table} WHERE ({column} = "{value}")'
    else:
        # Datetime
        query = f'SELECT id FROM {table} WHERE ({column} = "{value}")'
    cursor.execute(query)
    conn.commit()

    result = cursor.fetchone()
    _id = result[0]

    return _id
       

def insert_option(option, table):
    conn, cursor = create_connection()
    try:
        if option:
            query = f'INSERT INTO {table} (name) VALUES ("{option}")'
        else:
            query = f'INSERT INTO {table} (name) VALUES ("미지정")'
        
        cursor.execute(query)
        conn.commit()
    except:
        pass


def insert_date(date, table):
    conn, cursor = create_connection()
    try:
        if date:
            query = f'INSERT INTO {table} (date) VALUES ("{date}")'

        cursor.execute(query)
        conn.commit()
    except:
        pass


def insert_data(_id, table, school, option, title, date, link):
    conn, cursor = create_connection()
    
    school_id = get_id('scholarship_school_options', 'name', school)
    option_id = get_id('scholarship_options', 'name', option)

    columns = '(id, title, link, scholarship_school_option_id, scholarship_option_id'
    values  = f'VALUES ("{_id}", "{title}", "{link}", "{school_id}", "{option_id}"'

    if date:
        date_id = get_id('scholarship_dates', 'date', date)
        columns += ', scholarship_date_id'
        values  += f', "{date_id}"'
    
    columns += ')'
    values  += ')'
    query    = f'INSERT INTO {table} {columns} {values}'

    cursor.execute(query)
    conn.commit()

