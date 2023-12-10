# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockRandomTickServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockRandomTickServerEvent, self).__init__(callback)
        self.posX = None
        self.posY = None
        self.posZ = None
        self.blockName = None
        self.fullName = None
        self.auxValue = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.blockName = args.get("blockName")
        self.fullName = args.get("fullName")
        self.auxValue = args.get("auxValue")
        self.dimensionId = args.get("dimensionId")
