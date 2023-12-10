# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class WillTeleportToServerEvent(ServerEvent):

    def __init__(self, callback):
        super(WillTeleportToServerEvent, self).__init__(callback)
        self.cancel_ = None
        self.entityId_ = None
        self.fromDimensionId_ = None
        self.toDimensionId_ = None
        self.fromX_ = None
        self.fromY_ = None
        self.fromZ_ = None
        self.toX_ = None
        self.toY_ = None
        self.toZ_ = None
        self.cause_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args["cancel"]
        self.entityId_ = args["entityId"]
        self.fromDimensionId_ = args["fromDimensionId"]
        self.toDimensionId_ = args["toDimensionId"]
        self.fromX_ = args["fromX"]
        self.fromY_ = args["fromY"]
        self.fromZ_ = args["fromZ"]
        self.toX_ = args["toX"]
        self.toY_ = args["toY"]
        self.toZ_ = args["toZ"]
        self.cause_ = args["cause"]
