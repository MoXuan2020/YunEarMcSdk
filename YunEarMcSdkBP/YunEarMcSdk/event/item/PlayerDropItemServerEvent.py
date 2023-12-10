# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerDropItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerDropItemServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemEntityId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.itemEntityId_ = args.get("itemEntityId")
