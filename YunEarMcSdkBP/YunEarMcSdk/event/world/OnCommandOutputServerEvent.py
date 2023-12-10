# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnCommandOutputServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnCommandOutputServerEvent, self).__init__(callback)
        self.command = None
        self.message = None

    def CreateFromArgs(self, args):
        self.command = args.get("command")
        self.message = args.get("message")
