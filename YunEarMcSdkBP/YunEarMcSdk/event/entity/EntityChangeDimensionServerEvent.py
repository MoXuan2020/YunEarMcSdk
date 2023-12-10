# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityChangeDimensionServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityChangeDimensionServerEvent, self).__init__(callback)
        self.entityId = None
        self.fromDimensionId = None
        self.toDimensionId = None
        self.fromX = None
        self.fromY = None
        self.fromZ = None
        self.toX = None
        self.toY = None
        self.toZ = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.fromDimensionId = args.get("fromDimensionId")
        self.toDimensionId = args.get("toDimensionId")
        self.fromX = args.get("fromX")
        self.fromY = args.get("fromY")
        self.fromZ = args.get("fromZ")
        self.toX = args.get("toX")
        self.toY = args.get("toY")
        self.toZ = args.get("toZ")
