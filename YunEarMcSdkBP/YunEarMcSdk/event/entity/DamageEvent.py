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
        self.srcId_ = args["srcId"]
        self.projectileId_ = args["projectileId"]
        self.entityId_ = args["entityId"]
        self.damage_ = args["damage"]
        self.damage_f_ = args["damage_f"]
        self.absorption_ = args["absorption"]
        self.cause_ = args["cause"]
        self.knock_ = args["knock"]
        self.ignite_ = args["ignite"]
