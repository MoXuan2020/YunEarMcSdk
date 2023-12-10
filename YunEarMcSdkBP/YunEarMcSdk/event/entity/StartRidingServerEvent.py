# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class StartRidingServerEvent(ServerEvent):

    def __init__(self, callback):
        super(StartRidingServerEvent, self).__init__(callback)
        self.cancel = None
        self.actorId = None
        self.victimId = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
        self.actorId = args.get("actorId")
        self.victimId = args.get("victimId")
