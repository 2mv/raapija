class Transaction:

  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      setattr(self, key, value)

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

  def __str__(self):
    return self.date + " " + self.name + ": " + self.action + " [" + self.symbol + " x " + self.amount + "]"
