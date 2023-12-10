# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnMobHitBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnMobHitBlockServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.blockId_ = None
        self.auxValue_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.blockId_ = args["blockId"]
        self.auxValue_ = args["auxValue"]
        self.dimensionId_ = args["dimensionId"]
