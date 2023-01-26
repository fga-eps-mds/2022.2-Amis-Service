import requests
from datetime import datetime
import sys
import os

COMPONENT_KEY='fga-eps-mds_2022.2-Amis-Service'
SONAR_API=F'https://sonarcloud.io/api/measures/component_tree?component={COMPONENT_KEY}'
TODAY=datetime.now()
REPOSITORY=sys.argv[1]
RELEASE_VERSION=sys.argv[2]
FILE_PATH = f'./analytics-raw-data/fga-eps-mds-{REPOSITORY}-{TODAY.strftime("%m-%d-%Y-%H-%M-%S")}-{RELEASE_VERSION}.json'

metric_list = [
    'files',
    'functions',
    'complexity',
    'comment_lines_density',
    'duplicated_lines_density',
    'coverage',
    'ncloc',
    'tests',
    'test_errors',
    'test_failures',
    'test_execution_time',
    'security_rating'
]

body = {
    'metricKeys': ','.join(metric_list),
    'componentKey': COMPONENT_KEY
}


if __name__ == '__main__':
    response = requests.get(SONAR_API, params=body)
    text_response = response.text

    if not os.path.exists('./analytics-raw-data'):
        os.makedirs('./analytics-raw-data')


    with open(FILE_PATH, 'w') as file:
        file.write(text_response)
        file.close()

    