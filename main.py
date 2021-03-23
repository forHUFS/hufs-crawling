from worker.slack         import Slack
from crawling.scholarship import get_scholarship_data


def lambda_handler(event, context):
    required_data     = get_scholarship_data()
    scholarship_slack = Slack(channel = '10-게시판-관리', content = required_data)
    response          = scholarship_slack.post_message()

    return response