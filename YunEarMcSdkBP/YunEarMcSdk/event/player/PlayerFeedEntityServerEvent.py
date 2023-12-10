# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerFeedEntityServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerFeedEntityServerEvent, self).__init__(callback)
        self.playerId = None
        self.entityId = None
        self.itemDict = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.entityId = args.get("entityId")
        self.itemDict = args.get("itemDict")
        self.cancel = args.get("cancel")
