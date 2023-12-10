# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityChangeDimensionServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityChangeDimensionServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.fromDimensionId_ = None
        self.toDimensionId_ = None
        self.fromX_ = None
        self.fromY_ = None
        self.fromZ_ = None
        self.toX_ = None
        self.toY_ = None
        self.toZ_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.fromDimensionId_ = args.get("fromDimensionId")
        self.toDimensionId_ = args.get("toDimensionId")
        self.fromX_ = args.get("fromX")
        self.fromY_ = args.get("fromY")
        self.fromZ_ = args.get("fromZ")
        self.toX_ = args.get("toX")
        self.toY_ = args.get("toY")
        self.toZ_ = args.get("toZ")
