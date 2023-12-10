# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class DamageEvent(ServerEvent):

    def __init__(self, callback):
        super(DamageEvent, self).__init__(callback)
        self.srcId_ = None
        self.projectileId_ = None
        self.entityId_ = None
        self.damage_ = None
        self.damage_f_ = None
        self.absorption_ = None
        self.cause_ = None
        self.knock_ = None
        self.ignite_ = None

    def CreateFromArgs(self, args):
        self.srcId_ = args.get("srcId")
        self.projectileId_ = args.get("projectileId")
        self.entityId_ = args.get("entityId")
        self.damage_ = args.get("damage")
        self.damage_f_ = args.get("damage_f")
        self.absorption_ = args.get("absorption")
        self.cause_ = args.get("cause")
        self.knock_ = args.get("knock")
        self.ignite_ = args.get("ignite")
