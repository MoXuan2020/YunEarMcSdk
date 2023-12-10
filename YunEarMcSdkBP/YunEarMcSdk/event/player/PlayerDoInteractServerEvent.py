# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerDoInteractServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerDoInteractServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None
        self.interactEntityId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.itemDict_ = args["itemDict"]
        self.interactEntityId_ = args["interactEntityId"]
