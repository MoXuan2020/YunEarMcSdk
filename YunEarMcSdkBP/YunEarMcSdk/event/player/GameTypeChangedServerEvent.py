# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class GameTypeChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(GameTypeChangedServerEvent, self).__init__(callback)
        self.playerId = None
        self.oldGameType = None
        self.newGameType = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.oldGameType = args.get("oldGameType")
        self.newGameType = args.get("newGameType")
