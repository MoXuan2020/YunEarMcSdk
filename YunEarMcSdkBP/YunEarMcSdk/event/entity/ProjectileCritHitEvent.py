# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ProjectileCritHitEvent(ServerEvent):

    def __init__(self, callback):
        super(ProjectileCritHitEvent, self).__init__(callback)
        self.id_ = None
        self.targetId_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]
        self.targetId_ = args["targetId"]
