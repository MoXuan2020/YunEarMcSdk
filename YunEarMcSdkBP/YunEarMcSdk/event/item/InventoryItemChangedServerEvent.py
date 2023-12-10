# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class InventoryItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(InventoryItemChangedServerEvent, self).__init__(callback)
        self.playerId = None
        self.slot = None
        self.oldItemDict = None
        self.newItemDict = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.slot = args.get("slot")
        self.oldItemDict = args.get("oldItemDict")
        self.newItemDict = args.get("newItemDict")
