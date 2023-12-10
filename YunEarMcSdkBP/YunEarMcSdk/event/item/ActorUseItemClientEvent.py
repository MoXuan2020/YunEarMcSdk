# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ActorUseItemClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ActorUseItemClientEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None
        self.useMethod = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
        self.useMethod = args.get("useMethod")
