# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnMouseMiddleDownClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnMouseMiddleDownClientEvent, self).__init__(callback)
        self.isDown = None
        self.mousePositionX = None
        self.mousePositionY = None

    def CreateFromArgs(self, args):
        self.isDown = args.get("isDown")
        self.mousePositionX = args.get("mousePositionX")
        self.mousePositionY = args.get("mousePositionY")
