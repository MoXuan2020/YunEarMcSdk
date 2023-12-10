# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class HoldBeforeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(HoldBeforeClientEvent, self).__init__(callback)
        self.cancel = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
