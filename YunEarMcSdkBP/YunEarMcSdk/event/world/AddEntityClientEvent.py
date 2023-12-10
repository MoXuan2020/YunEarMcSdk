# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AddEntityClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AddEntityClientEvent, self).__init__(callback)
        self.id_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.dimensionId_ = None
        self.isBaby_ = None
        self.engineTypeStr_ = None
        self.itemName_ = None
        self.auxValue_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
        self.dimensionId_ = args.get("dimensionId")
        self.isBaby_ = args.get("isBaby")
        self.engineTypeStr_ = args.get("engineTypeStr")
        self.itemName_ = args.get("itemName")
        self.auxValue_ = args.get("auxValue")
