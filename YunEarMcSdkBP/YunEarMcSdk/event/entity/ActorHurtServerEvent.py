# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActorHurtServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActorHurtServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.cause_ = None
        self.damage_ = None
        self.damage_f_ = None
        self.absorbedDamage_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.cause_ = args["cause"]
        self.damage_ = args["damage"]
        self.damage_f_ = args["damage_f"]
        self.absorbedDamage_ = args["absorbedDamage"]
