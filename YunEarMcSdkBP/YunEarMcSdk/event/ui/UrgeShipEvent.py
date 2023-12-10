# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class UrgeShipEvent(ServerEvent):

    def __init__(self, callback):
        super(UrgeShipEvent, self).__init__(callback)
        self.playerId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
