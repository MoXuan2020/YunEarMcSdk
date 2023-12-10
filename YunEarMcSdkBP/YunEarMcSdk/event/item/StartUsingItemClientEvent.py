# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StartUsingItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StartUsingItemClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.itemDict_ = args.get("itemDict")
