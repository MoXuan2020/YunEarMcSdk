# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class NewOnEntityAreaEvent(ServerEvent):

    def __init__(self, callback):
        super(NewOnEntityAreaEvent, self).__init__(callback)
        self.name_ = None
        self.enteredEntities_ = None
        self.leftEntities_ = None

    def CreateFromArgs(self, args):
        self.name_ = args["name"]
        self.enteredEntities_ = args["enteredEntities"]
        self.leftEntities_ = args["leftEntities"]
