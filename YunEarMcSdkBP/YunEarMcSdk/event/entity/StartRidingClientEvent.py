# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StartRidingClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StartRidingClientEvent, self).__init__(callback)
        self.actorId_ = None
        self.victimId_ = None

    def CreateFromArgs(self, args):
        self.actorId_ = args["actorId"]
        self.victimId_ = args["victimId"]
