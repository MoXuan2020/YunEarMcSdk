# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class InventoryItemChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(InventoryItemChangedClientEvent, self).__init__(callback)
        self.playerId = None
        self.slot = None
        self.oldItemDict = None
        self.newItemDict = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.slot = args.get("slot")
        self.oldItemDict = args.get("oldItemDict")
        self.newItemDict = args.get("newItemDict")
