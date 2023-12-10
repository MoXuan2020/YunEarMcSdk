# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerDoInteractServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerDoInteractServerEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None
        self.interactEntityId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
        self.interactEntityId = args.get("interactEntityId")
