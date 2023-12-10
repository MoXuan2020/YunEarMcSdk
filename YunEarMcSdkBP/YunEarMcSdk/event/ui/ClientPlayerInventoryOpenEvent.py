# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientPlayerInventoryOpenEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientPlayerInventoryOpenEvent, self).__init__(callback)
        self.isCreative_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.isCreative_ = args.get("isCreative")
        self.cancel_ = args.get("cancel")
