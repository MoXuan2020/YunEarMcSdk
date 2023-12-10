# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class DimensionChangeFinishClientEvent(ClientEvent):

    def __init__(self, callback):
        super(DimensionChangeFinishClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.fromDimensionId_ = None
        self.toDimensionId_ = None
        self.toPos_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.fromDimensionId_ = args["fromDimensionId"]
        self.toDimensionId_ = args["toDimensionId"]
        self.toPos_ = args["toPos"]
