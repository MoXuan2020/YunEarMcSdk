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
        self.cancel_ = args.get("cancel")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.otherBlockX_ = args.get("otherBlockX")
        self.otherBlockY_ = args.get("otherBlockY")
        self.otherBlockZ_ = args.get("otherBlockZ")
        self.dimensionId_ = args.get("dimensionId")
