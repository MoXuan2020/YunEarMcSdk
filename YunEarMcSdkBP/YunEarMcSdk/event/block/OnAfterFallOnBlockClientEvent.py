# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnAfterFallOnBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnAfterFallOnBlockClientEvent, self).__init__(callback)
        self.entityId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.motionX_ = None
        self.motionY_ = None
        self.motionZ_ = None
        self.blockName_ = None
        self.calculate_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
        self.motionX_ = args.get("motionX")
        self.motionY_ = args.get("motionY")
        self.motionZ_ = args.get("motionZ")
        self.blockName_ = args.get("blockName")
        self.calculate_ = args.get("calculate")
