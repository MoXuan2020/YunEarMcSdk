# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPlaceBlockEntityEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPlaceBlockEntityEvent, self).__init__(callback)
        self.blockName_ = None
        self.dimension_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None

    def CreateFromArgs(self, args):
        self.blockName_ = args["blockName"]
        self.dimension_ = args["dimension"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
