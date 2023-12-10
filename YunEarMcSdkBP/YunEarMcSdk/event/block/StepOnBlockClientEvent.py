# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StepOnBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StepOnBlockClientEvent, self).__init__(callback)
        self.cancel_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.entityId_ = None
        self.blockName_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args["cancel"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.entityId_ = args["entityId"]
        self.blockName_ = args["blockName"]
        self.dimensionId_ = args["dimensionId"]
