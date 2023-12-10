# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class InventoryItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(InventoryItemChangedServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.slot_ = None
        self.oldItemDict_ = None
        self.newItemDict_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.slot_ = args.get("slot")
        self.oldItemDict_ = args.get("oldItemDict")
        self.newItemDict_ = args.get("newItemDict")
