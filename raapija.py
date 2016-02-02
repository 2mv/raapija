from transaction_scraper import TransactionScraper
from last_transactions_parser import LastTransactionsParser
from mailer import Mailer

import itertools
import sys


def ensure_printable(str_to_print):
  sys_encoding = sys.stdout.encoding
  str_as_bytes = str_to_print.encode(sys_encoding, 'replace')
  return str(str_as_bytes, sys_encoding)

to_addr = Mailer.get_cli_email_addr()
transactions = TransactionScraper.scrape()

last_transactions = LastTransactionsParser.read()
if last_transactions is None:
  print("Last transactions file not found. Skipping checks for new transactions.")
else:
  new_transactions = list(itertools.filterfalse(lambda x: x in last_transactions, transactions))
  if len(new_transactions) > 0:
    print(ensure_printable(Mailer.get_new_transactions_str(new_transactions)))
    if to_addr is not None:
      Mailer.send_transactions(new_transactions, to_addr)
  else:
    print("No new transactions")

LastTransactionsParser.write(transactions)
