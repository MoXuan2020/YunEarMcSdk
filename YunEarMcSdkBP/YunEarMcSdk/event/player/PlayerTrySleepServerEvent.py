# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerTrySleepServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerTrySleepServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.cancel_ = args.get("cancel")
