# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnMobHitBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnMobHitBlockServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.blockId_ = None
        self.auxValue_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
        self.blockId_ = args.get("blockId")
        self.auxValue_ = args.get("auxValue")
        self.dimensionId_ = args.get("dimensionId")
