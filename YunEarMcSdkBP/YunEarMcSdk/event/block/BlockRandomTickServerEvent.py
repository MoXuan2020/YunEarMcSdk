# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockRandomTickServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockRandomTickServerEvent, self).__init__(callback)
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.blockName_ = None
        self.fullName_ = None
        self.auxValue_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
        self.blockName_ = args.get("blockName")
        self.fullName_ = args.get("fullName")
        self.auxValue_ = args.get("auxValue")
        self.dimensionId_ = args.get("dimensionId")
