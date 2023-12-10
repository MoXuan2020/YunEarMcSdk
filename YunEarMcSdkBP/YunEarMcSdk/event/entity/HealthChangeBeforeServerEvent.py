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
        self.entityId_ = args["entityId"]
        self.from_ = args["from"]
        self.to_ = args["to"]
        self.byScript_ = args["byScript"]
        self.cancel_ = args["cancel"]
