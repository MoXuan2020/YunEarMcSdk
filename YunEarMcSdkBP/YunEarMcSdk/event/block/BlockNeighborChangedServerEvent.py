# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockNeighborChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockNeighborChangedServerEvent, self).__init__(callback)
        self.dimensionId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.blockName_ = None
        self.auxValue_ = None
        self.neighborPosX_ = None
        self.neighborPosY_ = None
        self.neighborPosZ_ = None
        self.fromBlockName_ = None
        self.fromBlockAuxValue_ = None
        self.toBlockName_ = None
        self.toAuxValue_ = None

    def CreateFromArgs(self, args):
        self.dimensionId_ = args.get("dimensionId")
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
        self.blockName_ = args.get("blockName")
        self.auxValue_ = args.get("auxValue")
        self.neighborPosX_ = args.get("neighborPosX")
        self.neighborPosY_ = args.get("neighborPosY")
        self.neighborPosZ_ = args.get("neighborPosZ")
        self.fromBlockName_ = args.get("fromBlockName")
        self.fromBlockAuxValue_ = args.get("fromBlockAuxValue")
        self.toBlockName_ = args.get("toBlockName")
        self.toAuxValue_ = args.get("toAuxValue")
