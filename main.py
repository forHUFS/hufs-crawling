from worker.slack         import Slack
from crawling.scholarship import Scholarship


def lambda_handler(event, context):
    scholarship       = Scholarship()
    required_data     = scholarship.get_scholarship_data()
    scholarship_slack = Slack(channel = '10-게시판-관리', content = required_data)
    response          = scholarship_slack.post_message()

    return response


if __name__ == '__main__':
    response = lambda_handler(None, None)
    print(response)