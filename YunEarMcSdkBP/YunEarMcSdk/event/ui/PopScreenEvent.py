# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PopScreenEvent(ClientEvent):

    def __init__(self, callback):
        super(PopScreenEvent, self).__init__(callback)
        self.screenName_ = None

    def CreateFromArgs(self, args):
        self.screenName_ = args["screenName"]
