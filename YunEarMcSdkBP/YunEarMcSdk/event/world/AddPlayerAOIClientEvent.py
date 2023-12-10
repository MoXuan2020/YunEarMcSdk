# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AddPlayerAOIClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AddPlayerAOIClientEvent, self).__init__(callback)
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
