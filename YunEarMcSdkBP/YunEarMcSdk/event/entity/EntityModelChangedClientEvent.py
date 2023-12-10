# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class EntityModelChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(EntityModelChangedClientEvent, self).__init__(callback)
        self.entityId = None
        self.newModel = None
        self.oldModel = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.newModel = args.get("newModel")
        self.oldModel = args.get("oldModel")
