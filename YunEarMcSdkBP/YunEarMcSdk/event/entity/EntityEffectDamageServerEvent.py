# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityEffectDamageServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityEffectDamageServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.damage_ = None
        self.attributeBuffType_ = None
        self.duration_ = None
        self.lifeTimer_ = None
        self.isInstantaneous_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.damage_ = args.get("damage")
        self.attributeBuffType_ = args.get("attributeBuffType")
        self.duration_ = args.get("duration")
        self.lifeTimer_ = args.get("lifeTimer")
        self.isInstantaneous_ = args.get("isInstantaneous")
