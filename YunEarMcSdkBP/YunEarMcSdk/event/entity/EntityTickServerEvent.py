# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityTickServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityTickServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.identifier_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.identifier_ = args.get("identifier")
