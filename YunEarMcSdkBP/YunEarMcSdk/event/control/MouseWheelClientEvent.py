# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class MouseWheelClientEvent(ClientEvent):

    def __init__(self, callback):
        super(MouseWheelClientEvent, self).__init__(callback)
        self.direction_ = None

    def CreateFromArgs(self, args):
        self.direction_ = args.get("direction")
