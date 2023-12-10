# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class StoreBuySuccServerEvent(ServerEvent):

    def __init__(self, callback):
        super(StoreBuySuccServerEvent, self).__init__(callback)
        self.playerId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
