# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityPlaceBlockAfterServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityPlaceBlockAfterServerEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.fullName_ = None
        self.auxData_ = None
        self.entityId_ = None
        self.dimensionId_ = None
        self.face_ = None

    def CreateFromArgs(self, args):
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.fullName_ = args.get("fullName")
        self.auxData_ = args.get("auxData")
        self.entityId_ = args.get("entityId")
        self.dimensionId_ = args.get("dimensionId")
        self.face_ = args.get("face")
