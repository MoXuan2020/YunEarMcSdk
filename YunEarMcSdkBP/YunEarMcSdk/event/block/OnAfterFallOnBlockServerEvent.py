# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnAfterFallOnBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnAfterFallOnBlockServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.motionX_ = None
        self.motionY_ = None
        self.motionZ_ = None
        self.blockName_ = None
        self.calculate_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.motionX_ = args["motionX"]
        self.motionY_ = args["motionY"]
        self.motionZ_ = args["motionZ"]
        self.blockName_ = args["blockName"]
        self.calculate_ = args["calculate"]
