# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class TapBeforeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(TapBeforeClientEvent, self).__init__(callback)
        self.cancel = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
