# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddExpEvent(ServerEvent):

    def __init__(self, callback):
        super(AddExpEvent, self).__init__(callback)
        self.id_ = None
        self.addExp_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]
        self.addExp_ = args["addExp"]
