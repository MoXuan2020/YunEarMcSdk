# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnModBlockNeteaseEffectCreatedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnModBlockNeteaseEffectCreatedClientEvent, self).__init__(callback)
        self.effectName_ = None
        self.id_ = None
        self.effectType_ = None
        self.blockPos_ = None

    def CreateFromArgs(self, args):
        self.effectName_ = args.get("effectName")
        self.id_ = args.get("id")
        self.effectType_ = args.get("effectType")
        self.blockPos_ = args.get("blockPos")
