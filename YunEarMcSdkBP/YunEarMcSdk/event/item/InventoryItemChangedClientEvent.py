# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class InventoryItemChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(InventoryItemChangedClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.slot_ = None
        self.oldItemDict_ = None
        self.newItemDict_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.slot_ = args["slot"]
        self.oldItemDict_ = args["oldItemDict"]
        self.newItemDict_ = args["newItemDict"]
