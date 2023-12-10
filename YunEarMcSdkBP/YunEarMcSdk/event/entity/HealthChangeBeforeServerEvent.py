# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class HealthChangeBeforeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(HealthChangeBeforeServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.from_ = None
        self.to_ = None
        self.byScript_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.from_ = args.get("from")
        self.to_ = args.get("to")
        self.byScript_ = args.get("byScript")
        self.cancel_ = args.get("cancel")
