# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlayerTryDestroyBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlayerTryDestroyBlockClientEvent, self).__init__(callback)
        self.x = None
        self.y = None
        self.z = None
        self.face = None
        self.blockName = None
        self.auxData = None
        self.playerId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.face = args.get("face")
        self.blockName = args.get("blockName")
        self.auxData = args.get("auxData")
        self.playerId = args.get("playerId")
        self.cancel = args.get("cancel")
