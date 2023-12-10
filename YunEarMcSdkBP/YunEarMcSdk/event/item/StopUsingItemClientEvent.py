# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StopUsingItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StopUsingItemClientEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
