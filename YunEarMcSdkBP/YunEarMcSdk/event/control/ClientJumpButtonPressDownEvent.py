# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientJumpButtonPressDownEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientJumpButtonPressDownEvent, self).__init__(callback)
        self.continueJump = None

    def CreateFromArgs(self, args):
        self.continueJump = args.get("continueJump")
