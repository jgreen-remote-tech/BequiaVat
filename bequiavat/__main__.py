import argparse
import requests


class ApiError(Exception):
    """An API Error Exception"""

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"APIError: {self.msg}"


argument_parser = argparse.ArgumentParser('bequiavat')
argument_parser.add_argument('--type',
                             required=True,
                             help="VAY type currently on 'flat' supported")
argument_parser.add_argument('--total-sales',
                             required=True,
                             help="Decimal number. Total Sales in pounds")
argument_parser.add_argument('--dry-run',
                             action='store_true',
                             default=False,
                             help="Optional: If set then the return will "
                                  "not be sent")
argument_parser.add_argument('--debug',
                             action='store_true',
                             default=False,
                             help="Optional: Increases output")
arguments = argument_parser.parse_args()


resp = requests.get("https://test-api.service.hmrc.gov.uk/hello/user",
                    headers={'Accept': 'application/vnd.hmrc.1.0+json',
                             'Authorization': 'Bearer c9187bb612db499483b364345d7f5f8d'})
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError(f"{resp.status_code} {resp.content}")
print(f'{resp.json()}')





print(f"hello {arguments.total_sales}")

