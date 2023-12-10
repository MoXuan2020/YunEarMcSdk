# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class SpawnProjectileServerEvent(ServerEvent):

    def __init__(self, callback):
        super(SpawnProjectileServerEvent, self).__init__(callback)
        self.projectileId = None
        self.projectileIdentifier = None
        self.spawnerId = None

    def CreateFromArgs(self, args):
        self.projectileId = args.get("projectileId")
        self.projectileIdentifier = args.get("projectileIdentifier")
        self.spawnerId = args.get("spawnerId")
