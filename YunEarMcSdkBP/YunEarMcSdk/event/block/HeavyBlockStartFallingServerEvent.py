# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HeavyBlockStartFallingServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HeavyBlockStartFallingServerEvent, self).__init__(callback)
        self.fallingBlockId_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.fallingBlockId_ = args.get("fallingBlockId")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.blockName_ = args.get("blockName")
        self.dimensionId_ = args.get("dimensionId")
