# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerRespawnFinishServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerRespawnFinishServerEvent, self).__init__(callback)
        self.playerId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
