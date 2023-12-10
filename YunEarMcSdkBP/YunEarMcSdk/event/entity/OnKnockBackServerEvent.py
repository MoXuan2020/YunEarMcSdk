# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnKnockBackServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnKnockBackServerEvent, self).__init__(callback)
        self.id_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
