# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ScreenSizeChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ScreenSizeChangedClientEvent, self).__init__(callback)
        self.beforeX_ = None
        self.beforeY_ = None
        self.afterX_ = None
        self.afterY_ = None

    def CreateFromArgs(self, args):
        self.beforeX_ = args["beforeX"]
        self.beforeY_ = args["beforeY"]
        self.afterX_ = args["afterX"]
        self.afterY_ = args["afterY"]
