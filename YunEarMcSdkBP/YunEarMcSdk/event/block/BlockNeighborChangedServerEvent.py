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
        self.dimensionId_ = args["dimensionId"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.blockName_ = args["blockName"]
        self.auxValue_ = args["auxValue"]
        self.neighborPosX_ = args["neighborPosX"]
        self.neighborPosY_ = args["neighborPosY"]
        self.neighborPosZ_ = args["neighborPosZ"]
        self.fromBlockName_ = args["fromBlockName"]
        self.fromBlockAuxValue_ = args["fromBlockAuxValue"]
        self.toBlockName_ = args["toBlockName"]
        self.toAuxValue_ = args["toAuxValue"]
