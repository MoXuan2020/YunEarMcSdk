# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnItemPutInEnchantingModelServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnItemPutInEnchantingModelServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.slotType_ = None
        self.options_ = None
        self.change_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.slotType_ = args["slotType"]
        self.options_ = args["options"]
        self.change_ = args["change"]
