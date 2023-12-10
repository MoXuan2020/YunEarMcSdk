# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnNewArmorExchangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnNewArmorExchangeServerEvent, self).__init__(callback)
        self.slot_ = None
        self.oldArmorDict_ = None
        self.newArmorDict_ = None
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.slot_ = args["slot"]
        self.oldArmorDict_ = args["oldArmorDict"]
        self.newArmorDict_ = args["newArmorDict"]
        self.playerId_ = args["playerId"]
