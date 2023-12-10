# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ExtinguishFireServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ExtinguishFireServerEvent, self).__init__(callback)
        self.pos = None
        self.playerId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.pos = args.get("pos")
        self.playerId = args.get("playerId")
        self.cancel = args.get("cancel")
