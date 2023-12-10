# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnStandOnBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnStandOnBlockClientEvent, self).__init__(callback)
        self.entityId_ = None
        self.dimensionId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.motionX_ = None
        self.motionY_ = None
        self.motionZ_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.dimensionId_ = args["dimensionId"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.motionX_ = args["motionX"]
        self.motionY_ = args["motionY"]
        self.motionZ_ = args["motionZ"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.blockName_ = args["blockName"]
        self.cancel_ = args["cancel"]
