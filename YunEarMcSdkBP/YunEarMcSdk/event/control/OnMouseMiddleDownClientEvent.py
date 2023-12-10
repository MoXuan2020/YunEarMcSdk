# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnMouseMiddleDownClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnMouseMiddleDownClientEvent, self).__init__(callback)
        self.isDown_ = None
        self.mousePositionX_ = None
        self.mousePositionY_ = None

    def CreateFromArgs(self, args):
        self.isDown_ = args["isDown"]
        self.mousePositionX_ = args["mousePositionX"]
        self.mousePositionY_ = args["mousePositionY"]
