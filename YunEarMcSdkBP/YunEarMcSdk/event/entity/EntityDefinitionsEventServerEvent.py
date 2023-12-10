# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityDefinitionsEventServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityDefinitionsEventServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.eventName_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.eventName_ = args.get("eventName")
