# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ShearsUseToBlockBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ShearsUseToBlockBeforeServerEvent, self).__init__(callback)
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.auxData_ = None
        self.dropName_ = None
        self.dropCount_ = None
        self.entityId_ = None
        self.dimensionId_ = None
        self.cancelShears_ = None

    def CreateFromArgs(self, args):
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.blockName_ = args["blockName"]
        self.auxData_ = args["auxData"]
        self.dropName_ = args["dropName"]
        self.dropCount_ = args["dropCount"]
        self.entityId_ = args["entityId"]
        self.dimensionId_ = args["dimensionId"]
        self.cancelShears_ = args["cancelShears"]
