from worker.slack         import Slack
from crawling.scholarship import Scholarship


def lambda_handler(event, context):
    print(event['body'])
    # Scholarship.insert_scholarship_data()

    # required_data     = Scholarship.get_scholarship_data()
    # scholarship_slack = Slack(channel = '10-게시판-관리', content = required_data)
    # response          = scholarship_slack.post_message()

    # return response