# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnPlayerBlockedByShieldBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnPlayerBlockedByShieldBeforeServerEvent, self).__init__(callback)
        self.playerId = None
        self.sourceId = None
        self.itemDict = None
        self.damage = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.sourceId = args.get("sourceId")
        self.itemDict = args.get("itemDict")
        self.damage = args.get("damage")
