# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnCommandOutputClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnCommandOutputClientEvent, self).__init__(callback)
        self.command_ = None
        self.message_ = None

    def CreateFromArgs(self, args):
        self.command_ = args.get("command")
        self.message_ = args.get("message")
