# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PopScreenEvent(ClientEvent):

    def __init__(self, callback):
        super(PopScreenEvent, self).__init__(callback)
        self.screenName = None

    def CreateFromArgs(self, args):
        self.screenName = args.get("screenName")
