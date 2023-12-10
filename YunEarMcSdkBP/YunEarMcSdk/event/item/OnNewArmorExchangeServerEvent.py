# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnNewArmorExchangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnNewArmorExchangeServerEvent, self).__init__(callback)
        self.slot = None
        self.oldArmorDict = None
        self.newArmorDict = None
        self.playerId = None

    def CreateFromArgs(self, args):
        self.slot = args.get("slot")
        self.oldArmorDict = args.get("oldArmorDict")
        self.newArmorDict = args.get("newArmorDict")
        self.playerId = args.get("playerId")
