# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnPlayerActiveShieldServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnPlayerActiveShieldServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.isActive_ = None
        self.itemDict_ = None
        self.cancelable_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.isActive_ = args["isActive"]
        self.itemDict_ = args["itemDict"]
        self.cancelable_ = args["cancelable"]
        self.cancel_ = args["cancel"]
