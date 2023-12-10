# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class WillAddEffectServerEvent(ServerEvent):

    def __init__(self, callback):
        super(WillAddEffectServerEvent, self).__init__(callback)
        self.entityId = None
        self.effectName = None
        self.effectDuration = None
        self.effectAmplifier = None
        self.cancel = None
        self.damage = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.effectName = args.get("effectName")
        self.effectDuration = args.get("effectDuration")
        self.effectAmplifier = args.get("effectAmplifier")
        self.cancel = args.get("cancel")
        self.damage = args.get("damage")
