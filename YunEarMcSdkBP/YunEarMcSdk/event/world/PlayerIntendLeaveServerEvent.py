# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerIntendLeaveServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerIntendLeaveServerEvent, self).__init__(callback)
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
