# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ModBlockEntityLoadedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ModBlockEntityLoadedClientEvent, self).__init__(callback)
        self.posX = None
        self.posY = None
        self.posZ = None
        self.dimensionId = None
        self.blockName = None

    def CreateFromArgs(self, args):
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.dimensionId = args.get("dimensionId")
        self.blockName = args.get("blockName")
