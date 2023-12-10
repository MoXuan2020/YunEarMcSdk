# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class DelServerPlayerEvent(ServerEvent):

    def __init__(self, callback):
        super(DelServerPlayerEvent, self).__init__(callback)
        self.id_ = None
        self.isTransfer_ = None
        self.uid_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]
        self.isTransfer_ = args["isTransfer"]
        self.uid_ = args["uid"]
