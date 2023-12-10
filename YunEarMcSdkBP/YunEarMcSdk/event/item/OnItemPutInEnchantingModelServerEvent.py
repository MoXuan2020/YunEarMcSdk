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
        self.playerId_ = args.get("playerId")
        self.slotType_ = args.get("slotType")
        self.options_ = args.get("options")
        self.change_ = args.get("change")
