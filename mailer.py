from marrow.mailer import Mailer as MarrowMailer
from marrow.mailer import Message

import sys


class Mailer:

  MAILER = MarrowMailer(dict(manager=dict(use='immediate'), transport=dict(use='sendmail')))

  @staticmethod
  def send(message):
    Mailer.MAILER.send(message)

  @staticmethod
  def start():
    Mailer.MAILER.start()

  @staticmethod
  def stop():
    Mailer.MAILER.stop()

  @staticmethod
  def send_transactions(transactions, to_addr):
    Mailer.start()

    message = Message(
        to=to_addr,
        subject='New transactions',
        plain=repr(transactions)
    )
    Mailer.send(message)

    Mailer.stop()

  @staticmethod
  def get_cli_email_addr():
    try:
      return sys.argv[1]
    except IndexError:
      return None
