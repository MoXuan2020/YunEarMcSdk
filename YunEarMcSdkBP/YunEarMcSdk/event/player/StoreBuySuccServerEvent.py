# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class StoreBuySuccServerEvent(ServerEvent):

    def __init__(self, callback):
        super(StoreBuySuccServerEvent, self).__init__(callback)
        self.playerId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
