# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActuallyHurtServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActuallyHurtServerEvent, self).__init__(callback)
        self.srcId_ = None
        self.projectileId_ = None
        self.entityId_ = None
        self.damage_ = None
        self.damage_f_ = None
        self.cause_ = None

    def CreateFromArgs(self, args):
        self.srcId_ = args["srcId"]
        self.projectileId_ = args["projectileId"]
        self.entityId_ = args["entityId"]
        self.damage_ = args["damage"]
        self.damage_f_ = args["damage_f"]
        self.cause_ = args["cause"]
