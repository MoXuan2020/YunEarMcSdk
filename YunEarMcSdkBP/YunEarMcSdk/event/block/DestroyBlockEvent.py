# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class DestroyBlockEvent(ServerEvent):

    def __init__(self, callback):
        super(DestroyBlockEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.face_ = None
        self.fullName_ = None
        self.auxData_ = None
        self.playerId_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.face_ = args["face"]
        self.fullName_ = args["fullName"]
        self.auxData_ = args["auxData"]
        self.playerId_ = args["playerId"]
        self.dimensionId_ = args["dimensionId"]
