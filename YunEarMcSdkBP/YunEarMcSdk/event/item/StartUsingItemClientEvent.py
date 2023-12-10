# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StartUsingItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StartUsingItemClientEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
