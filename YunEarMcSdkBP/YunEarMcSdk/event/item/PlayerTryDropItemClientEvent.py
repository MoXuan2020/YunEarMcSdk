# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlayerTryDropItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlayerTryDropItemClientEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
        self.cancel = args.get("cancel")
