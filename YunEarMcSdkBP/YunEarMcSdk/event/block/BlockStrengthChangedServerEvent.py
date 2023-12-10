# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class BlockStrengthChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(BlockStrengthChangedServerEvent, self).__init__(callback)
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.blockName_ = None
        self.auxValue_ = None
        self.newStrength_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.blockName_ = args["blockName"]
        self.auxValue_ = args["auxValue"]
        self.newStrength_ = args["newStrength"]
        self.dimensionId_ = args["dimensionId"]
