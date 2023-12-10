# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ItemUseAfterServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ItemUseAfterServerEvent, self).__init__(callback)
        self.entityId = None
        self.itemDict = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.itemDict = args.get("itemDict")
