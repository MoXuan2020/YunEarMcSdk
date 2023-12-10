# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPlayerTryDestroyBlockEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPlayerTryDestroyBlockEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.face = None
        self.fullName = None
        self.auxData = None
        self.playerId = None
        self.dimensionId = None
        self.cancel = None
        self.spawnResources = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.face = args.get("face")
        self.fullName = args.get("fullName")
        self.auxData = args.get("auxData")
        self.playerId = args.get("playerId")
        self.dimensionId = args.get("dimensionId")
        self.cancel = args.get("cancel")
        self.spawnResources = args.get("spawnResources")
