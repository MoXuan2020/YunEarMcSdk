# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class SpawnProjectileServerEvent(ServerEvent):

    def __init__(self, callback):
        super(SpawnProjectileServerEvent, self).__init__(callback)
        self.projectileId_ = None
        self.projectileIdentifier_ = None
        self.spawnerId_ = None

    def CreateFromArgs(self, args):
        self.projectileId_ = args.get("projectileId")
        self.projectileIdentifier_ = args.get("projectileIdentifier")
        self.spawnerId_ = args.get("spawnerId")
