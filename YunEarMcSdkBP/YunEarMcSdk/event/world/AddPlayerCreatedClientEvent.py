# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AddPlayerCreatedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AddPlayerCreatedClientEvent, self).__init__(callback)
        self.playerId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
