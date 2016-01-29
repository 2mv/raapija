from marrow.mailer import Message as MarrowMessage


class Message(MarrowMessage):

  def __bytes__(self):
    return bytes(str(self), self.encoding)
