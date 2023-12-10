# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AttackAnimEndClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AttackAnimEndClientEvent, self).__init__(callback)
        self.id = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
