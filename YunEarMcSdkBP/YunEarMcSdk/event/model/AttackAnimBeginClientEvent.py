# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AttackAnimBeginClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AttackAnimBeginClientEvent, self).__init__(callback)
        self.id = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
