# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerInventoryOpenScriptServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerInventoryOpenScriptServerEvent, self).__init__(callback)
        self.playerId = None
        self.isCreative = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.isCreative = args.get("isCreative")
