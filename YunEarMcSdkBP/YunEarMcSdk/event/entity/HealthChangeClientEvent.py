# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class HealthChangeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(HealthChangeClientEvent, self).__init__(callback)
        self.entityId = None
        self._from = None
        self.to = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self._from = args.get("from")
        self.to = args.get("to")
