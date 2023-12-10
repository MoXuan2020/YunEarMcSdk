# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HealthChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HealthChangeServerEvent, self).__init__(callback)
        self.entityId = None
        self._from = None
        self.to = None
        self.byScript = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self._from = args.get("from")
        self.to = args.get("to")
        self.byScript = args.get("byScript")
