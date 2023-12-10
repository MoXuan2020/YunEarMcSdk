# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPlayerTryDestroyBlockEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPlayerTryDestroyBlockEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.face_ = None
        self.fullName_ = None
        self.auxData_ = None
        self.playerId_ = None
        self.dimensionId_ = None
        self.cancel_ = None
        self.spawnResources_ = None

    def CreateFromArgs(self, args):
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.face_ = args.get("face")
        self.fullName_ = args.get("fullName")
        self.auxData_ = args.get("auxData")
        self.playerId_ = args.get("playerId")
        self.dimensionId_ = args.get("dimensionId")
        self.cancel_ = args.get("cancel")
        self.spawnResources_ = args.get("spawnResources")
