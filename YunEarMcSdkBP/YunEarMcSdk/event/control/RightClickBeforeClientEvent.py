# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class RightClickBeforeClientEvent(ClientEvent):

    def __init__(self, callback):
        super(RightClickBeforeClientEvent, self).__init__(callback)
        self.cancel = None

    def CreateFromArgs(self, args):
        self.cancel = args.get("cancel")
