# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PopScreenAfterClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PopScreenAfterClientEvent, self).__init__(callback)
        self.screenName = None

    def CreateFromArgs(self, args):
        self.screenName = args.get("screenName")
