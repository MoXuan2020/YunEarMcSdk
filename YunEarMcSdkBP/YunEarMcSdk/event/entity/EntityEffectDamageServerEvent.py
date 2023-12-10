# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityEffectDamageServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityEffectDamageServerEvent, self).__init__(callback)
        self.entityId = None
        self.damage = None
        self.attributeBuffType = None
        self.duration = None
        self.lifeTimer = None
        self.isInstantaneous = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.damage = args.get("damage")
        self.attributeBuffType = args.get("attributeBuffType")
        self.duration = args.get("duration")
        self.lifeTimer = args.get("lifeTimer")
        self.isInstantaneous = args.get("isInstantaneous")
