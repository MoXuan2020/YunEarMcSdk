# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnModBlockNeteaseEffectCreatedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnModBlockNeteaseEffectCreatedClientEvent, self).__init__(callback)
        self.effectName = None
        self.id = None
        self.effectType = None
        self.blockPos = None

    def CreateFromArgs(self, args):
        self.effectName = args.get("effectName")
        self.id = args.get("id")
        self.effectType = args.get("effectType")
        self.blockPos = args.get("blockPos")
