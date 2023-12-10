# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class GrindStoneRemovedEnchantClientEvent(ClientEvent):

    def __init__(self, callback):
        super(GrindStoneRemovedEnchantClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.oldItemDict_ = None
        self.additionalItemDict_ = None
        self.newItemDict_ = None
        self.exp_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.oldItemDict_ = args.get("oldItemDict")
        self.additionalItemDict_ = args.get("additionalItemDict")
        self.newItemDict_ = args.get("newItemDict")
        self.exp_ = args.get("exp")
