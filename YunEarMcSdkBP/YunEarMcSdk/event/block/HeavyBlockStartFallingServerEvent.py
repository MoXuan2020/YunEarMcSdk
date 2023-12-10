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
        self.fallingBlockId_ = args["fallingBlockId"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.blockName_ = args["blockName"]
        self.dimensionId_ = args["dimensionId"]
