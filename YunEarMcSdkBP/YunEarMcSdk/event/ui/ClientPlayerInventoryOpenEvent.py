# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientPlayerInventoryOpenEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientPlayerInventoryOpenEvent, self).__init__(callback)
        self.isCreative = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.isCreative = args.get("isCreative")
        self.cancel = args.get("cancel")
