# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddExpEvent(ServerEvent):

    def __init__(self, callback):
        super(AddExpEvent, self).__init__(callback)
        self.id = None
        self.addExp = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.addExp = args.get("addExp")
