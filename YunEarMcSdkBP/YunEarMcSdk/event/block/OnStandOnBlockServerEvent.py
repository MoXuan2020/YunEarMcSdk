# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnStandOnBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnStandOnBlockServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.dimensionId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.motionX_ = None
        self.motionY_ = None
        self.motionZ_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.dimensionId_ = args.get("dimensionId")
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
        self.motionX_ = args.get("motionX")
        self.motionY_ = args.get("motionY")
        self.motionZ_ = args.get("motionZ")
        self.blockX_ = args.get("blockX")
        self.blockY_ = args.get("blockY")
        self.blockZ_ = args.get("blockZ")
        self.blockName_ = args.get("blockName")
        self.cancel_ = args.get("cancel")
