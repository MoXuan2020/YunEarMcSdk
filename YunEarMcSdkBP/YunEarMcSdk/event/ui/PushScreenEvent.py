# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PushScreenEvent(ClientEvent):

    def __init__(self, callback):
        super(PushScreenEvent, self).__init__(callback)
        self.screenName = None

    def CreateFromArgs(self, args):
        self.screenName = args.get("screenName")
