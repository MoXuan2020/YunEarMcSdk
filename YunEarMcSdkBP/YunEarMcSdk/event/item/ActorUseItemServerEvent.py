# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActorUseItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActorUseItemServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None
        self.useMethod_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.itemDict_ = args["itemDict"]
        self.useMethod_ = args["useMethod"]
