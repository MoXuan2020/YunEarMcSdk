# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FallingBlockReturnHeavyBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FallingBlockReturnHeavyBlockServerEvent, self).__init__(callback)
        self.fallingBlockId_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.heavyBlockName_ = None
        self.prevHereBlockName_ = None
        self.dimensionId_ = None
        self.fallTickAmount_ = None

    def CreateFromArgs(self, args):
        self.fallingBlockId_ = args.get("fallingBlockId")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.heavyBlockName_ = args.get("heavyBlockName")
        self.prevHereBlockName_ = args.get("prevHereBlockName")
        self.dimensionId_ = args.get("dimensionId")
        self.fallTickAmount_ = args.get("fallTickAmount")
