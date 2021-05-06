from worker.slack         import Slack
from crawling.scholarship import Scholarship


def lambda_handler(event, context):
    scholarship = Scholarship()
    scholarship.insert_scholarship_data()

    # required_data     = scholarship.get_scholarship_data()
    # scholarship_slack = Slack(channel = '10-게시판-관리', content = required_data)
    # response          = scholarship_slack.post_message()


if __name__ == '__main__':
    lambda_handler(None, None)