class TransactionParser:

  ROW_ORDER = ['date', 'name', 'role', 'action', 'amount', 'symbol', 'sum']

  @staticmethod
  def from_row(row):
    cells = [cell for cell in row.children if cell.name == 'td']
    cells_dict = dict(zip(TransactionParser.ROW_ORDER, cells))
    transaction_dict = {key: str(value.string).strip() for key, value in cells_dict.items()}
    transaction_dict['name'] = TransactionParser.extract_name(cells_dict['name'])
    return transaction_dict

  @staticmethod
  def extract_name(cell):
    return cell.a.string.strip()
