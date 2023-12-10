# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChangeSwimStateServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChangeSwimStateServerEvent, self).__init__(callback)
        self.entityId = None
        self.formState = None
        self.toState = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.formState = args.get("formState")
        self.toState = args.get("toState")
