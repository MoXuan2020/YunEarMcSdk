# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerEatFoodServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerEatFoodServerEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None
        self.hunger = None
        self.nutrition = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
        self.hunger = args.get("hunger")
        self.nutrition = args.get("nutrition")
