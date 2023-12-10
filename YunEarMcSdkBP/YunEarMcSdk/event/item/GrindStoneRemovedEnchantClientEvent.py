# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class GrindStoneRemovedEnchantClientEvent(ClientEvent):

    def __init__(self, callback):
        super(GrindStoneRemovedEnchantClientEvent, self).__init__(callback)
        self.playerId = None
        self.oldItemDict = None
        self.additionalItemDict = None
        self.newItemDict = None
        self.exp = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.oldItemDict = args.get("oldItemDict")
        self.additionalItemDict = args.get("additionalItemDict")
        self.newItemDict = args.get("newItemDict")
        self.exp = args.get("exp")
