# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnCommandOutputClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnCommandOutputClientEvent, self).__init__(callback)
        self.command = None
        self.message = None

    def CreateFromArgs(self, args):
        self.command = args.get("command")
        self.message = args.get("message")
