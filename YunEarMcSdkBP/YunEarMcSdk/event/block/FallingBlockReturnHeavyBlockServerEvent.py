# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FallingBlockReturnHeavyBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FallingBlockReturnHeavyBlockServerEvent, self).__init__(callback)
        self.fallingBlockId = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.heavyBlockName = None
        self.prevHereBlockName = None
        self.dimensionId = None
        self.fallTickAmount = None

    def CreateFromArgs(self, args):
        self.fallingBlockId = args.get("fallingBlockId")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.heavyBlockName = args.get("heavyBlockName")
        self.prevHereBlockName = args.get("prevHereBlockName")
        self.dimensionId = args.get("dimensionId")
        self.fallTickAmount = args.get("fallTickAmount")
