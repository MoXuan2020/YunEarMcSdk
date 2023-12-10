# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerTrySleepServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerTrySleepServerEvent, self).__init__(callback)
        self.playerId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.cancel = args.get("cancel")
