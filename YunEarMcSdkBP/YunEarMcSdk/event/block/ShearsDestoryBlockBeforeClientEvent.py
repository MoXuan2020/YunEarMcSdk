# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ShearsDestoryBlockBeforeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ShearsDestoryBlockBeforeClientEvent, self).__init__(callback)
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.auxData_ = None
        self.dropName_ = None
        self.dropCount_ = None
        self.playerId_ = None
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
        self.playerId_ = args["playerId"]
        self.dimensionId_ = args["dimensionId"]
        self.cancelShears_ = args["cancelShears"]
