# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class GridComponentSizeChangedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(GridComponentSizeChangedClientEvent, self).__init__(callback)
        self.path_ = None

    def CreateFromArgs(self, args):
        self.path_ = args.get("path")
