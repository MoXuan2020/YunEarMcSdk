# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class RefreshEffectServerEvent(ServerEvent):

    def __init__(self, callback):
        super(RefreshEffectServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.effectName_ = None
        self.effectDuration_ = None
        self.effectAmplifier_ = None
        self.damage_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.effectName_ = args.get("effectName")
        self.effectDuration_ = args.get("effectDuration")
        self.effectAmplifier_ = args.get("effectAmplifier")
        self.damage_ = args.get("damage")
