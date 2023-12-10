# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ShearsUseToBlockBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ShearsUseToBlockBeforeServerEvent, self).__init__(callback)
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.auxData_ = None
        self.dropName_ = None
        self.dropCount_ = None
        self.entityId_ = None
        self.dimensionId_ = None
        self.cancelShears_ = None

    def CreateFromArgs(self, args):
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.blockName_ = args.get("blockName")
        self.auxData_ = args.get("auxData")
        self.dropName_ = args.get("dropName")
        self.dropCount_ = args.get("dropCount")
        self.entityId_ = args.get("entityId")
        self.dimensionId_ = args.get("dimensionId")
        self.cancelShears_ = args.get("cancelShears")
