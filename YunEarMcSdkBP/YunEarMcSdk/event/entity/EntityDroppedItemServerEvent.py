# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityDroppedItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityDroppedItemServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.itemDict_ = None
        self.itemEntityId_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.itemDict_ = args["itemDict"]
        self.itemEntityId_ = args["itemEntityId"]
