# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityRemoveEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityRemoveEvent, self).__init__(callback)
        self.id_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]
