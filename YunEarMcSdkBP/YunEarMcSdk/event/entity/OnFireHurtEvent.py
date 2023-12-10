# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnFireHurtEvent(ServerEvent):

    def __init__(self, callback):
        super(OnFireHurtEvent, self).__init__(callback)
        self.victim = None
        self.src = None
        self.fireTime = None
        self.cancel = None
        self.cancelIgnite = None

    def CreateFromArgs(self, args):
        self.victim = args.get("victim")
        self.src = args.get("src")
        self.fireTime = args.get("fireTime")
        self.cancel = args.get("cancel")
        self.cancelIgnite = args.get("cancelIgnite")
