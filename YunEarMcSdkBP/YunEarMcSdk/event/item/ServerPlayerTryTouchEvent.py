# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPlayerTryTouchEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPlayerTryTouchEvent, self).__init__(callback)
        self.playerId_ = None
        self.entityId_ = None
        self.itemDict_ = None
        self.cancel_ = None
        self.pickupDelay_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.entityId_ = args["entityId"]
        self.itemDict_ = args["itemDict"]
        self.cancel_ = args["cancel"]
        self.pickupDelay_ = args["pickupDelay"]
