# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class GrassBlockToDirtBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(GrassBlockToDirtBlockServerEvent, self).__init__(callback)
        self.dimension_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None

    def CreateFromArgs(self, args):
        self.dimension_ = args["dimension"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
