# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ShearsUseToBlockBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ShearsUseToBlockBeforeServerEvent, self).__init__(callback)
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.blockName = None
        self.auxData = None
        self.dropName = None
        self.dropCount = None
        self.entityId = None
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
        self.entityId = args.get("entityId")
        self.dimensionId = args.get("dimensionId")
        self.cancelShears = args.get("cancelShears")
