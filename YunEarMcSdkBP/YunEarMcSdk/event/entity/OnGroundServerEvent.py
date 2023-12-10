# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnGroundServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnGroundServerEvent, self).__init__(callback)
        self.id_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
