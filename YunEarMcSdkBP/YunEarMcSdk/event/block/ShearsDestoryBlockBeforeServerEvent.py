# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ShearsDestoryBlockBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ShearsDestoryBlockBeforeServerEvent, self).__init__(callback)
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.blockName = None
        self.auxData = None
        self.dropName = None
        self.dropCount = None
        self.playerId = None
        self.dimensionId = None
        self.cancelShears = None

    def CreateFromArgs(self, args):
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.blockName = args.get("blockName")
        self.auxData = args.get("auxData")
        self.dropName = args.get("dropName")
        self.dropCount = args.get("dropCount")
        self.playerId = args.get("playerId")
        self.dimensionId = args.get("dimensionId")
        self.cancelShears = args.get("cancelShears")
