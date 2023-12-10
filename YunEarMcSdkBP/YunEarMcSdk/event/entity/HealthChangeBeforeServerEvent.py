# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HealthChangeBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HealthChangeBeforeServerEvent, self).__init__(callback)
        self.entityId = None
        self._from = None
        self.to = None
        self.byScript = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self._from = args.get("from")
        self.to = args.get("to")
        self.byScript = args.get("byScript")
        self.cancel = args.get("cancel")
