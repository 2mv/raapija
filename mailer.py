from marrow.mailer import Mailer as MarrowMailer
from message import Message

import sys
import os
import pwd
import socket


class Mailer:

  MAILER = MarrowMailer(dict(manager=dict(use='immediate'), transport=dict(use='sendmail')))
  DEFAULT_AUTHOR = pwd.getpwuid(os.getuid()).pw_name + '@' + socket.getfqdn()

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
        author=Mailer.DEFAULT_AUTHOR,
        to=to_addr,
        subject='New transactions',
        plain=Mailer.get_new_transactions_str(transactions)
    )
    Mailer.send(message)

    Mailer.stop()

  @staticmethod
  def get_cli_email_addr():
    try:
      return sys.argv[1]
    except IndexError:
      return None

  @staticmethod
  def get_new_transactions_str(transactions):
    message_str = "New transactions:\n"
    message_str += "\n".join([str(tr) for tr in transactions])
    return message_str
