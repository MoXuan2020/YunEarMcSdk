# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ExtinguishFireServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ExtinguishFireServerEvent, self).__init__(callback)
        self.pos_ = None
        self.playerId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.pos_ = args["pos"]
        self.playerId_ = args["playerId"]
        self.cancel_ = args["cancel"]
