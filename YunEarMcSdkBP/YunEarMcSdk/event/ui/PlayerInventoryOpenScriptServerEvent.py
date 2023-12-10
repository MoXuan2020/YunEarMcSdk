# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerInventoryOpenScriptServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerInventoryOpenScriptServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.isCreative_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.isCreative_ = args["isCreative"]
