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
        self.id_ = args["id"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.dimensionId_ = args["dimensionId"]
        self.isBaby_ = args["isBaby"]
        self.engineTypeStr_ = args["engineTypeStr"]
        if "itemName" in args:
            self.itemName_ = args["itemName"]
        if "auxValue" in args:
            self.auxValue_ = args["auxValue"]
