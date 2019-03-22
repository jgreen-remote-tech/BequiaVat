import argparse


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

print(f"hello {arguments.total_sales}")

