# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnBeforeFallOnBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnBeforeFallOnBlockServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.blockName_ = None
        self.fallDistance_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.blockName_ = args["blockName"]
        self.fallDistance_ = args["fallDistance"]
        self.cancel_ = args["cancel"]
