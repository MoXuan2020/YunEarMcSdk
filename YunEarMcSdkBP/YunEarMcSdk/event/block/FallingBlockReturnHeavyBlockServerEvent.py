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
        self.fallingBlockId_ = args["fallingBlockId"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.heavyBlockName_ = args["heavyBlockName"]
        self.prevHereBlockName_ = args["prevHereBlockName"]
        self.dimensionId_ = args["dimensionId"]
        self.fallTickAmount_ = args["fallTickAmount"]
