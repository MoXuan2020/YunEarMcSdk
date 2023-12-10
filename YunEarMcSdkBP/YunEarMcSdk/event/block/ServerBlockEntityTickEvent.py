# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerBlockEntityTickEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerBlockEntityTickEvent, self).__init__(callback)
        self.blockName_ = None
        self.dimension_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None

    def CreateFromArgs(self, args):
        self.blockName_ = args.get("blockName")
        self.dimension_ = args.get("dimension")
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
