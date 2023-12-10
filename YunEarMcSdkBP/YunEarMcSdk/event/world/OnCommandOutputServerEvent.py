# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnCommandOutputServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnCommandOutputServerEvent, self).__init__(callback)
        self.command_ = None
        self.message_ = None

    def CreateFromArgs(self, args):
        self.command_ = args.get("command")
        self.message_ = args.get("message")
