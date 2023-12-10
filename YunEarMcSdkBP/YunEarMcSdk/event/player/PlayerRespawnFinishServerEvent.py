# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerRespawnFinishServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerRespawnFinishServerEvent, self).__init__(callback)
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
