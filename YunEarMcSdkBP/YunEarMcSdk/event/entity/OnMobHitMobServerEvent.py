# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnMobHitMobServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnMobHitMobServerEvent, self).__init__(callback)
        self.mobId = None
        self.hittedMobList = None

    def CreateFromArgs(self, args):
        self.mobId = args.get("mobId")
        self.hittedMobList = args.get("hittedMobList")
