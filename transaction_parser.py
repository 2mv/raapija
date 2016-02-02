from transaction import Transaction


class TransactionParser:

  ROW_ORDER = ['date', 'name', 'role', 'action', 'amount', 'symbol', 'sum', 'dragspel']

  @staticmethod
  def from_row(row):
    cells = [cell for cell in row.children if cell.name == 'td']
    cells_dict = dict(zip(TransactionParser.ROW_ORDER, cells))
    transaction_dict = {key: str(value.string).strip() for key, value in cells_dict.items()}
    transaction_dict['name'] = TransactionParser.extract_name(cells_dict['name'])
    return Transaction(**transaction_dict)

  @staticmethod
  def extract_name(cell):
    return cell.a.string.strip()

  @staticmethod
  def is_transaction_row(row):
    num_cells = len([cell for cell in row.children if cell.name == 'td'])
    return num_cells == len(TransactionParser.ROW_ORDER)
