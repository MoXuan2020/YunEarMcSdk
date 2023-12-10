# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerDropItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerDropItemServerEvent, self).__init__(callback)
        self.playerId = None
        self.itemEntityId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemEntityId = args.get("itemEntityId")
