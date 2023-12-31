# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerEatFoodServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerEatFoodServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None
        self.hunger_ = None
        self.nutrition_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.itemDict_ = args["itemDict"]
        self.hunger_ = args["hunger"]
        self.nutrition_ = args["nutrition"]
