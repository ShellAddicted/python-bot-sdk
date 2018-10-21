# coding: utf-8
import sys

print(sys.version)
import dialog_bot_sdk
from dialog_bot_sdk.peers import private_peer
from dialog_bot_sdk.bot import DialogBot
from threading import Thread
import time


def on_msg(*params):
    d.messaging.send_message(params[0].peer, "Echo: " + str(params[0].message.textMessage.text))


def receiver():
    d.messaging.on_message(on_msg)


if __name__ == '__main__':
    d = DialogBot.get_insecure_bot("grpc-test.transmit.im:8080", "eb48c8233ba00476fbc84bd0ff9b3c961db8afcc")

    pqd = private_peer(706340607)
    d.messaging.send_message(pqd, "Ready", )
    th = Thread(target=receiver)
    th.start()

    th.join()
