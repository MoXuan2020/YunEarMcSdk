# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerEntityTryPlaceBlockEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerEntityTryPlaceBlockEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.fullName = None
        self.auxData = None
        self.entityId = None
        self.dimensionId = None
        self.face = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.fullName = args.get("fullName")
        self.auxData = args.get("auxData")
        self.entityId = args.get("entityId")
        self.dimensionId = args.get("dimensionId")
        self.face = args.get("face")
        self.cancel = args.get("cancel")
