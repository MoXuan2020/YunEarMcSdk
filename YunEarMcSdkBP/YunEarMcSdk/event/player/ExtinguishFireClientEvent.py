# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ExtinguishFireClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ExtinguishFireClientEvent, self).__init__(callback)
        self.pos_ = None
        self.playerId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.pos_ = args["pos"]
        self.playerId_ = args["playerId"]
        self.cancel_ = args["cancel"]
