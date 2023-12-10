# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class DestroyBlockEvent(ServerEvent):

    def __init__(self, callback):
        super(DestroyBlockEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.face = None
        self.fullName = None
        self.auxData = None
        self.playerId = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.face = args.get("face")
        self.fullName = args.get("fullName")
        self.auxData = args.get("auxData")
        self.playerId = args.get("playerId")
        self.dimensionId = args.get("dimensionId")
