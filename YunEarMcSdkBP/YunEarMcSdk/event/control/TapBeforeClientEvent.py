# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class TapBeforeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(TapBeforeClientEvent, self).__init__(callback)
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.cancel_ = args.get("cancel")
