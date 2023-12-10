# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActuallyHurtServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActuallyHurtServerEvent, self).__init__(callback)
        self.srcId = None
        self.projectileId = None
        self.entityId = None
        self.damage = None
        self.damage_f = None
        self.cause = None

    def CreateFromArgs(self, args):
        self.srcId = args.get("srcId")
        self.projectileId = args.get("projectileId")
        self.entityId = args.get("entityId")
        self.damage = args.get("damage")
        self.damage_f = args.get("damage_f")
        self.cause = args.get("cause")
