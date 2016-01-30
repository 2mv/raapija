import csv
import tempfile
import os


class LastTransactionsParser:

  LAST_TRANSACTIONS_FILENAME = os.path.join(tempfile.gettempdir(), 'raapija_transactions_last.csv')

  @staticmethod
  def read():
    try:
      with open(LastTransactionsParser.LAST_TRANSACTIONS_FILENAME, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [transaction for transaction in reader]
    except FileNotFoundError:
      return None

  @staticmethod
  def write(transactions):
    with open(LastTransactionsParser.LAST_TRANSACTIONS_FILENAME, 'w', encoding='utf-8') as csvfile:
      csv_fieldnames = transactions[0].keys()
      writer = csv.DictWriter(csvfile, csv_fieldnames)
      writer.writeheader()
      for transaction in transactions:
        writer.writerow(transaction)
