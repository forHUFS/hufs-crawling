from config        import CRAWLING_URL
from worker.driver import WebDriver
from worker.date   import convert_datetime
from worker.regex  import (
                    pattern,
                    remove_option_special_character,
                    remove_date_special_character,
                    find_by_pattern,
                    sub_option,
                    sub_date
                    )
from worker.sql    import (
                    find_data,
                    insert_option,
                    insert_date,
                    insert_data,
                    close_connection
                    )


class Scholarship:
    def get_scholarship_data(self):
        url    = CRAWLING_URL +  '1'
        driver = WebDriver()
        driver.get(url = url)

        tables = driver.find_elements_by_xpath('//*[@id="board-container"]/div[2]/form[1]/table/tbody/tr')

        data          = []
        required_data = []

        for table in tables:
            _id = table.find_element_by_class_name("no").text
            if not _id:
                pass
            else:
                if not find_data('scholarships', 'id', _id):
                    content = table.find_element_by_class_name("title")
                    link    = content.find_element_by_css_selector("a").get_attribute("href")
                    title   = content.text

                    campus = remove_option_special_character(find_by_pattern(pattern['campus'], title))
                    option = remove_option_special_character(find_by_pattern(pattern['option'], title))
                    date   = remove_date_special_character(find_by_pattern(pattern['date'], title))

                    title  = sub_date(title, date)
                    title  = sub_option(pattern['campus'], title)
                    title  = sub_option(pattern['option'], title)
                    
                    temp = []

                    if campus == '미지정':
                        temp.append('캠퍼스')

                    if option == '미지정':
                        temp.append('장학 종류')

                    if date:
                        date = convert_datetime(date)
                    else:
                        temp.append('요일')
                
                    temp_required_data = {
                        '누락된 사항': temp
                    }


                    if temp:
                        temp_required_data['해당 장학금 URL'] = link
                        required_data.append(temp_required_data)

        
                    temp_data = {
                        'id'    : int(_id),
                        'campus': campus,
                        'option': option,
                        'title' : title,
                        'date'  : date,
                        'link'  : link
                    }

                    data.append(temp_data)

        driver.close()

        for row in data:
            insert_option(row['campus'], 'scholarship_campus_options')
            insert_option(row['option'], 'scholarship_options')
            insert_date(row['date'], 'scholarship_dates')

            insert_data(
                _id    = int(row['id']),
                table  = 'scholarships',
                campus = row['campus'],
                option = row['option'],
                title  = row['title'],
                date   = row['date'],
                link   = row['link']
            )
        
        close_connection()

        for idx in range(len(required_data)):
            required_data[idx] = str(required_data[idx])

        required_data = '\n'.join(required_data)

        return required_data


    def insert_scholarship_data(self):
        data = []

        for page_num in range(1, 6):
            url    = CRAWLING_URL + str(page_num)
            driver = WebDriver()
            driver.get(url = url)

            tables = driver.find_elements_by_xpath('//*[@id="board-container"]/div[2]/form[1]/table/tbody/tr')

            for table in tables:
                _id = table.find_element_by_class_name("no").text
                if not _id:
                    pass
                else:
                    content = table.find_element_by_class_name("title")
                    link    = content.find_element_by_css_selector("a").get_attribute("href")
                    title   = content.text

                    campus = remove_option_special_character(find_by_pattern(pattern['campus'], title))
                    option = remove_option_special_character(find_by_pattern(pattern['option'], title))
                    date   = remove_date_special_character(find_by_pattern(pattern['date'], title))

                    title  = sub_date(title, date)
                    title  = sub_option(pattern['campus'], title)
                    title  = sub_option(pattern['option'], title)
                    
                    if date:
                        date = convert_datetime(date)

                    temp_data = {
                        'id'    : int(_id),
                        'campus': campus,
                        'option': option,
                        'title' : title,
                        'date'  : date,
                        'link'  : link
                    }

                    data.append(temp_data)

        driver.close()

        for row in data:
            insert_option(row['campus'], 'campuses')
            insert_option(row['option'], 'scholarship_options')
            insert_date(row['date'], 'scholarship_dates')

            insert_data(
                _id    = int(row['id']),
                table  = 'scholarships',
                campus = row['campus'],
                option = row['option'],
                title  = row['title'],
                date   = row['date'],
                link   = row['link']
            )


        close_connection()