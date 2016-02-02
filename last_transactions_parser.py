import csv
import tempfile
import os

from transaction import Transaction


class LastTransactionsParser:

  LAST_TRANSACTIONS_FILENAME = os.path.join(tempfile.gettempdir(), 'raapija_transactions_last.csv')

  @staticmethod
  def read():
    try:
      with open(LastTransactionsParser.LAST_TRANSACTIONS_FILENAME, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [Transaction(**transaction_dict) for transaction_dict in reader]
    except FileNotFoundError:
      return None

  @staticmethod
  def write(transactions):
    with open(LastTransactionsParser.LAST_TRANSACTIONS_FILENAME, 'w', encoding='utf-8') as csvfile:
      csv_fieldnames = transactions[0].__dict__.keys()
      writer = csv.DictWriter(csvfile, csv_fieldnames)
      writer.writeheader()
      for transaction in transactions:
        writer.writerow(transaction.__dict__)
