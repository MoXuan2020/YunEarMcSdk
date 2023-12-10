# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class RemovePlayerAOIClientEvent(ClientEvent):

    def __init__(self, callback):
        super(RemovePlayerAOIClientEvent, self).__init__(callback)
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
