# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ItemUseAfterServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ItemUseAfterServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.itemDict_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.itemDict_ = args.get("itemDict")
