# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class GameTypeChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(GameTypeChangedServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.oldGameType_ = None
        self.newGameType_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.oldGameType_ = args.get("oldGameType")
        self.newGameType_ = args.get("newGameType")
