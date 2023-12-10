# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class WillTeleportToServerEvent(ServerEvent):

    def __init__(self, callback):
        super(WillTeleportToServerEvent, self).__init__(callback)
        self.cancel = None
        self.entityId = None
        self.fromDimensionId = None
        self.toDimensionId = None
        self.fromX = None
        self.fromY = None
        self.fromZ = None
        self.toX = None
        self.toY = None
        self.toZ = None
        self.cause = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
        self.entityId = args.get("entityId")
        self.fromDimensionId = args.get("fromDimensionId")
        self.toDimensionId = args.get("toDimensionId")
        self.fromX = args.get("fromX")
        self.fromY = args.get("fromY")
        self.fromZ = args.get("fromZ")
        self.toX = args.get("toX")
        self.toY = args.get("toY")
        self.toZ = args.get("toZ")
        self.cause = args.get("cause")
