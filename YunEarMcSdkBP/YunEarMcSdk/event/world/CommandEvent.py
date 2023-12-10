# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class CommandEvent(ServerEvent):

    def __init__(self, callback):
        super(CommandEvent, self).__init__(callback)
        self.entityId_ = None
        self.command_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.command_ = args["command"]
        self.cancel_ = args["cancel"]
