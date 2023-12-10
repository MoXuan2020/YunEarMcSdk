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
        self.fallingBlockId_ = args["fallingBlockId"]
        self.fallingBlockX_ = args["fallingBlockX"]
        self.fallingBlockY_ = args["fallingBlockY"]
        self.fallingBlockZ_ = args["fallingBlockZ"]
        self.blockName_ = args["blockName"]
        self.fallTickAmount_ = args["fallTickAmount"]
        self.dimensionId_ = args["dimensionId"]
        self.cancelDrop_ = args["cancelDrop"]
