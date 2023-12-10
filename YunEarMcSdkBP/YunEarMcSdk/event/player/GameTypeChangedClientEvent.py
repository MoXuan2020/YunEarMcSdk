# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class GameTypeChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(GameTypeChangedClientEvent, self).__init__(callback)
        self.playerId = None
        self.oldGameType = None
        self.newGameType = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.oldGameType = args.get("oldGameType")
        self.newGameType = args.get("newGameType")
