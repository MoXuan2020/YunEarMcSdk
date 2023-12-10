# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPlayerTryTouchEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPlayerTryTouchEvent, self).__init__(callback)
        self.playerId = None
        self.entityId = None
        self.itemDict = None
        self.cancel = None
        self.pickupDelay = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.entityId = args.get("entityId")
        self.itemDict = args.get("itemDict")
        self.cancel = args.get("cancel")
        self.pickupDelay = args.get("pickupDelay")
