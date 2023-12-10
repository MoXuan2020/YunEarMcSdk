# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityPickupItemServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityPickupItemServerEvent, self).__init__(callback)
        self.entityId = None
        self.itemDict = None
        self.secondaryActor = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.itemDict = args.get("itemDict")
        self.secondaryActor = args.get("secondaryActor")
