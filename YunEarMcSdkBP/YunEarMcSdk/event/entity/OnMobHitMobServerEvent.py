# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnMobHitMobServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnMobHitMobServerEvent, self).__init__(callback)
        self.mobId_ = None
        self.hittedMobList_ = None

    def CreateFromArgs(self, args):
        self.mobId_ = args["mobId"]
        self.hittedMobList_ = args["hittedMobList"]
