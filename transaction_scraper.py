from mechanicalsoup import Browser
from transaction_parser import TransactionParser


class TransactionScraper:

  LATEST_TRANSACTIONS_URL = "https://www.nordnet.fi/mux/web/analys/experterna/oversikt.html?subflik=avslut"
  BROWSER = Browser(soup_config={'features': 'html5lib'})

  @staticmethod
  def scrape():
    latest_transactions_page = TransactionScraper.BROWSER.get(TransactionScraper.LATEST_TRANSACTIONS_URL)
    transactions_heading = latest_transactions_page.soup.find_all('h2', string="Tapahtumat")[0]
    transactions_table = transactions_heading.parent.table

    transaction_rows = [row for row in transactions_table.descendants if TransactionScraper.is_transaction_row(row)]
    return [TransactionParser.from_row(row) for row in transaction_rows]

  @staticmethod
  def is_transaction_row(element):
    return element.name == 'tr' and TransactionParser.is_transaction_row(element)
