# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChestBlockTryPairWithServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChestBlockTryPairWithServerEvent, self).__init__(callback)
        self.cancel_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.otherBlockX_ = None
        self.otherBlockY_ = None
        self.otherBlockZ_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args["cancel"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.otherBlockX_ = args["otherBlockX"]
        self.otherBlockY_ = args["otherBlockY"]
        self.otherBlockZ_ = args["otherBlockZ"]
        self.dimensionId_ = args["dimensionId"]
