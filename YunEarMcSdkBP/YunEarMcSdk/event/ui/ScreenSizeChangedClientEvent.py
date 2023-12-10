# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ScreenSizeChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ScreenSizeChangedClientEvent, self).__init__(callback)
        self.beforeX = None
        self.beforeY = None
        self.afterX = None
        self.afterY = None

    def CreateFromArgs(self, args):
        self.beforeX = args.get("beforeX")
        self.beforeY = args.get("beforeY")
        self.afterX = args.get("afterX")
        self.afterY = args.get("afterY")
