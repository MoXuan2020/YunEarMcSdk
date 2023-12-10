# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class RemoveEntityClientEvent(ClientEvent):

    def __init__(self, callback):
        super(RemoveEntityClientEvent, self).__init__(callback)
        self.id_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
