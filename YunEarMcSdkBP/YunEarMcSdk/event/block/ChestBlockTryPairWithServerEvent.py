# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChestBlockTryPairWithServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChestBlockTryPairWithServerEvent, self).__init__(callback)
        self.cancel = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.otherBlockX = None
        self.otherBlockY = None
        self.otherBlockZ = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.otherBlockX = args.get("otherBlockX")
        self.otherBlockY = args.get("otherBlockY")
        self.otherBlockZ = args.get("otherBlockZ")
        self.dimensionId = args.get("dimensionId")
