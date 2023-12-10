# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnItemPutInEnchantingModelServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnItemPutInEnchantingModelServerEvent, self).__init__(callback)
        self.playerId = None
        self.slotType = None
        self.options = None
        self.change = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.slotType = args.get("slotType")
        self.options = args.get("options")
        self.change = args.get("change")
