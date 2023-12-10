# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class DimensionChangeFinishClientEvent(ClientEvent):

    def __init__(self, callback):
        super(DimensionChangeFinishClientEvent, self).__init__(callback)
        self.playerId = None
        self.fromDimensionId = None
        self.toDimensionId = None
        self.toPos = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.fromDimensionId = args.get("fromDimensionId")
        self.toDimensionId = args.get("toDimensionId")
        self.toPos = args.get("toPos")
