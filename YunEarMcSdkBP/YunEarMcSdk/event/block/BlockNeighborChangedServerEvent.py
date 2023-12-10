# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockNeighborChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockNeighborChangedServerEvent, self).__init__(callback)
        self.dimensionId = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.blockName = None
        self.auxValue = None
        self.neighborPosX = None
        self.neighborPosY = None
        self.neighborPosZ = None
        self.fromBlockName = None
        self.fromBlockAuxValue = None
        self.toBlockName = None
        self.toAuxValue = None

    def CreateFromArgs(self, args):
        self.dimensionId = args.get("dimensionId")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.blockName = args.get("blockName")
        self.auxValue = args.get("auxValue")
        self.neighborPosX = args.get("neighborPosX")
        self.neighborPosY = args.get("neighborPosY")
        self.neighborPosZ = args.get("neighborPosZ")
        self.fromBlockName = args.get("fromBlockName")
        self.fromBlockAuxValue = args.get("fromBlockAuxValue")
        self.toBlockName = args.get("toBlockName")
        self.toAuxValue = args.get("toAuxValue")
