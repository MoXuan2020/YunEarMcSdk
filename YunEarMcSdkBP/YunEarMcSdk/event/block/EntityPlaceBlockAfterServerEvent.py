# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityPlaceBlockAfterServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityPlaceBlockAfterServerEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.fullName = None
        self.auxData = None
        self.entityId = None
        self.dimensionId = None
        self.face = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.fullName = args.get("fullName")
        self.auxData = args.get("auxData")
        self.entityId = args.get("entityId")
        self.dimensionId = args.get("dimensionId")
        self.face = args.get("face")
