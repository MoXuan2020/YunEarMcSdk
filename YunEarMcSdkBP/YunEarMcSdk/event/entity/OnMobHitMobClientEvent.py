# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnMobHitMobClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnMobHitMobClientEvent, self).__init__(callback)
        self.mobId_ = None
        self.hittedMobList_ = None

    def CreateFromArgs(self, args):
        self.mobId_ = args["mobId"]
        self.hittedMobList_ = args["hittedMobList"]
