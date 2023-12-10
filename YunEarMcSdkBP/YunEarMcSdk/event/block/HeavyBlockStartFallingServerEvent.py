# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HeavyBlockStartFallingServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HeavyBlockStartFallingServerEvent, self).__init__(callback)
        self.fallingBlockId = None
        self.blockX = None
        self.blockY = None
        self.blockZ = None
        self.blockName = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.fallingBlockId = args.get("fallingBlockId")
        self.blockX = args.get("blockX")
        self.blockY = args.get("blockY")
        self.blockZ = args.get("blockZ")
        self.blockName = args.get("blockName")
        self.dimensionId = args.get("dimensionId")
