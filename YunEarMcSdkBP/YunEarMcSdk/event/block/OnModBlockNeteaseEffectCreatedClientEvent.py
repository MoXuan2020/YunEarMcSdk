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
        self.effectName_ = args["effectName"]
        self.id_ = args["id"]
        self.effectType_ = args["effectType"]
        self.blockPos_ = args["blockPos"]
