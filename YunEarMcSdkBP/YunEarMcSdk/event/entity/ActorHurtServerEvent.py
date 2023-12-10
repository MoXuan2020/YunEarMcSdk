# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ActorHurtServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ActorHurtServerEvent, self).__init__(callback)
        self.entityId = None
        self.cause = None
        self.damage = None
        self.damage_f = None
        self.absorbedDamage = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.cause = args.get("cause")
        self.damage = args.get("damage")
        self.damage_f = args.get("damage_f")
        self.absorbedDamage = args.get("absorbedDamage")
