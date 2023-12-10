# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityTickServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityTickServerEvent, self).__init__(callback)
        self.entityId = None
        self.identifier = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.identifier = args.get("identifier")
