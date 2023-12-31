# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ActorUseItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ActorUseItemClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None
        self.useMethod_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.itemDict_ = args["itemDict"]
        self.useMethod_ = args["useMethod"]
