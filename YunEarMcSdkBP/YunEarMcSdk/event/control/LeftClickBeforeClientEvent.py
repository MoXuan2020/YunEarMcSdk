# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class LeftClickBeforeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(LeftClickBeforeClientEvent, self).__init__(callback)
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args["cancel"]
