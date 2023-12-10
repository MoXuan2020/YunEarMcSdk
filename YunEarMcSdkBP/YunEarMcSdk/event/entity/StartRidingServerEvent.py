# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class StartRidingServerEvent(ServerEvent):

    def __init__(self, callback):
        super(StartRidingServerEvent, self).__init__(callback)
        self.cancel_ = None
        self.actorId_ = None
        self.victimId_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args.get("cancel")
        self.actorId_ = args.get("actorId")
        self.victimId_ = args.get("victimId")
