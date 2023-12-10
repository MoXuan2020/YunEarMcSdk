# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnPlayerHitBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnPlayerHitBlockClientEvent, self).__init__(callback)
        self.playerId = None
        self.posX = None
        self.posY = None
        self.posZ = None
        self.blockId = None
        self.auxValue = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.posX = args.get("posX")
        self.posY = args.get("posY")
        self.posZ = args.get("posZ")
        self.blockId = args.get("blockId")
        self.auxValue = args.get("auxValue")
