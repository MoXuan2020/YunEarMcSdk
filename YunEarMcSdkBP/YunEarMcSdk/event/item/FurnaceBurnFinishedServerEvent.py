# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FurnaceBurnFinishedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FurnaceBurnFinishedServerEvent, self).__init__(callback)
        self.dimensionId = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.itemDict = None

    def CreateFromArgs(self, args):
        self.dimensionId = args.get("dimensionId")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.itemDict = args.get("itemDict")
