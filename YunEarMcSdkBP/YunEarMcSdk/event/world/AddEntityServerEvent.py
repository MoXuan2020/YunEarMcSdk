# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddEntityServerEvent(ServerEvent):

    def __init__(self, callback):
        super(AddEntityServerEvent, self).__init__(callback)
        self.id = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.dimensionId = None
        self.isBaby = None
        self.engineTypeStr = None
        self.itemName = None
        self.auxValue = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.dimensionId = args.get("dimensionId")
        self.isBaby = args.get("isBaby")
        self.engineTypeStr = args.get("engineTypeStr")
        self.itemName = args.get("itemName")
        self.auxValue = args.get("auxValue")
