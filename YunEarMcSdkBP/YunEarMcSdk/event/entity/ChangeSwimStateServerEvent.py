# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChangeSwimStateServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChangeSwimStateServerEvent, self).__init__(callback)
        self.entityId_ = None
        self.formState_ = None
        self.toState_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args["entityId"]
        self.formState_ = args["formState"]
        self.toState_ = args["toState"]
