# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ModBlockEntityLoadedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ModBlockEntityLoadedClientEvent, self).__init__(callback)
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.dimensionId_ = None
        self.blockName_ = None

    def CreateFromArgs(self, args):
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.dimensionId_ = args["dimensionId"]
        self.blockName_ = args["blockName"]
