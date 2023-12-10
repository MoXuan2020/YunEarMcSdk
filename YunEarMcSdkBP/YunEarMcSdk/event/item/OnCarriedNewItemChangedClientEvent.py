# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnCarriedNewItemChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnCarriedNewItemChangedClientEvent, self).__init__(callback)
        self.itemDict_ = None

    def CreateFromArgs(self, args):
        self.itemDict_ = args.get("itemDict")
