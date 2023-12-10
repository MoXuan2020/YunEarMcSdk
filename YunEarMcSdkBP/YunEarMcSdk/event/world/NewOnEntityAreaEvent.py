# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class NewOnEntityAreaEvent(ServerEvent):

    def __init__(self, callback):
        super(NewOnEntityAreaEvent, self).__init__(callback)
        self.name = None
        self.enteredEntities = None
        self.leftEntities = None

    def CreateFromArgs(self, args):
        self.name = args.get("name")
        self.enteredEntities = args.get("enteredEntities")
        self.leftEntities = args.get("leftEntities")
