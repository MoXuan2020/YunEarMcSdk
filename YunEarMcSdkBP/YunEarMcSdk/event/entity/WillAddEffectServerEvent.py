# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class WillAddEffectServerEvent(ServerEvent):

    def __init__(self, callback):
        super(WillAddEffectServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.effectName_ = None
        self.effectDuration_ = None
        self.effectAmplifier_ = None
        self.cancel_ = None
        self.damage_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.effectName_ = args["effectName"]
        self.effectDuration_ = args["effectDuration"]
        self.effectAmplifier_ = args["effectAmplifier"]
        self.cancel_ = args["cancel"]
        self.damage_ = args["damage"]
