# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class CraftItemOutputChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(CraftItemOutputChangeServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None
        self.screenContainerType_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.itemDict_ = args["itemDict"]
        self.screenContainerType_ = args["screenContainerType"]
        self.cancel_ = args["cancel"]
