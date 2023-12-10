# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FallingBlockBreakServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FallingBlockBreakServerEvent, self).__init__(callback)
        self.fallingBlockId = None
        self.fallingBlockX = None
        self.fallingBlockY = None
        self.fallingBlockZ = None
        self.blockName = None
        self.fallTickAmount = None
        self.dimensionId = None
        self.cancelDrop = None

    def CreateFromArgs(self, args):
        self.fallingBlockId = args.get("fallingBlockId")
        self.fallingBlockX = args.get("fallingBlockX")
        self.fallingBlockY = args.get("fallingBlockY")
        self.fallingBlockZ = args.get("fallingBlockZ")
        self.blockName = args.get("blockName")
        self.fallTickAmount = args.get("fallTickAmount")
        self.dimensionId = args.get("dimensionId")
        self.cancelDrop = args.get("cancelDrop")
