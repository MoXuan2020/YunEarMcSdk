# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class RemoveEffectServerEvent(ServerEvent):

    def __init__(self, callback):
        super(RemoveEffectServerEvent, self).__init__(callback)
        self.entityId = None
        self.effectName = None
        self.effectDuration = None
        self.effectAmplifier = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.effectName = args.get("effectName")
        self.effectDuration = args.get("effectDuration")
        self.effectAmplifier = args.get("effectAmplifier")
