# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class HealthChangeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(HealthChangeClientEvent, self).__init__(callback)
        self.entityId_ = None
        self.from_ = None
        self.to_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.from_ = args.get("from")
        self.to_ = args.get("to")
