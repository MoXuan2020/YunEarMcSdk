# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ProjectileCritHitEvent(ServerEvent):

    def __init__(self, callback):
        super(ProjectileCritHitEvent, self).__init__(callback)
        self.id = None
        self.targetId = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.targetId = args.get("targetId")
