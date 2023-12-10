# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FallingBlockBreakServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FallingBlockBreakServerEvent, self).__init__(callback)
        self.fallingBlockId_ = None
        self.fallingBlockX_ = None
        self.fallingBlockY_ = None
        self.fallingBlockZ_ = None
        self.blockName_ = None
        self.fallTickAmount_ = None
        self.dimensionId_ = None
        self.cancelDrop_ = None

    def CreateFromArgs(self, args):
        self.fallingBlockId_ = args.get("fallingBlockId")
        self.fallingBlockX_ = args.get("fallingBlockX")
        self.fallingBlockY_ = args.get("fallingBlockY")
        self.fallingBlockZ_ = args.get("fallingBlockZ")
        self.blockName_ = args.get("blockName")
        self.fallTickAmount_ = args.get("fallTickAmount")
        self.dimensionId_ = args.get("dimensionId")
        self.cancelDrop_ = args.get("cancelDrop")
