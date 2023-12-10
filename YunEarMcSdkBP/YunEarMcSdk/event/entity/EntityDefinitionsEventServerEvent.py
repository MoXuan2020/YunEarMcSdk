# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityDefinitionsEventServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityDefinitionsEventServerEvent, self).__init__(callback)
        self.entityId = None
        self.eventName = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.eventName = args.get("eventName")
