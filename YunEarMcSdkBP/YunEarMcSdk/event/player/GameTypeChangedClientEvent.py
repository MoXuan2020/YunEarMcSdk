# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class GameTypeChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(GameTypeChangedClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.oldGameType_ = None
        self.newGameType_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.oldGameType_ = args["oldGameType"]
        self.newGameType_ = args["newGameType"]
