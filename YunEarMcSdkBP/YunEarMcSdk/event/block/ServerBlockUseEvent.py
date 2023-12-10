# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerBlockUseEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerBlockUseEvent, self).__init__(callback)
        self.playerId_ = None
        self.blockName_ = None
        self.aux_ = None
        self.cancel_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.face_ = None
        self.itemDict_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.blockName_ = args["blockName"]
        self.aux_ = args["aux"]
        self.cancel_ = args["cancel"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.face_ = args["face"]
        self.itemDict_ = args["itemDict"]
        self.dimensionId_ = args["dimensionId"]
