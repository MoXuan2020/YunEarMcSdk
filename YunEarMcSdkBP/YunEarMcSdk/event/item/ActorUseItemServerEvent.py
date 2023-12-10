# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActorUseItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActorUseItemServerEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None
        self.useMethod = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
        self.useMethod = args.get("useMethod")
