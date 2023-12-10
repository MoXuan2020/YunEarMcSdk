# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnMobHitMobClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnMobHitMobClientEvent, self).__init__(callback)
        self.mobId = None
        self.hittedMobList = None

    def CreateFromArgs(self, args):
        self.mobId = args.get("mobId")
        self.hittedMobList = args.get("hittedMobList")
