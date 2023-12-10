# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class RemoveEffectServerEvent(ServerEvent):

    def __init__(self, callback):
        super(RemoveEffectServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.effectName_ = None
        self.effectDuration_ = None
        self.effectAmplifier_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.effectName_ = args.get("effectName")
        self.effectDuration_ = args.get("effectDuration")
        self.effectAmplifier_ = args.get("effectAmplifier")
