# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class FurnaceBurnFinishedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(FurnaceBurnFinishedServerEvent, self).__init__(callback)
        self.dimensionId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.itemDict_ = None

    def CreateFromArgs(self, args):
        self.dimensionId_ = args["dimensionId"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.itemDict_ = args["itemDict"]
