# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StartRidingClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StartRidingClientEvent, self).__init__(callback)
        self.actorId = None
        self.victimId = None

    def CreateFromArgs(self, args):
        self.actorId = args.get("actorId")
        self.victimId = args.get("victimId")
