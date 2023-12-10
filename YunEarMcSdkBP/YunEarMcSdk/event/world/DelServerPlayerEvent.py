# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class DelServerPlayerEvent(ServerEvent):

    def __init__(self, callback):
        super(DelServerPlayerEvent, self).__init__(callback)
        self.id = None
        self.isTransfer = None
        self.uid = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.isTransfer = args.get("isTransfer")
        self.uid = args.get("uid")
