# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlayerTryDropItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlayerTryDropItemClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.itemDict_ = args["itemDict"]
        self.cancel_ = args["cancel"]
