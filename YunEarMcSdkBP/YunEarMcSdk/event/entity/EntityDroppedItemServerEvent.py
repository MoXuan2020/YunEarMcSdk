# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityDroppedItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityDroppedItemServerEvent, self).__init__(callback)
        self.entityId = None
        self.itemDict = None
        self.itemEntityId = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.itemDict = args.get("itemDict")
        self.itemEntityId = args.get("itemEntityId")
