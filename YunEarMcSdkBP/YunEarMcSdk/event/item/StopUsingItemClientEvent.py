# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StopUsingItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StopUsingItemClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.itemDict_ = args["itemDict"]
