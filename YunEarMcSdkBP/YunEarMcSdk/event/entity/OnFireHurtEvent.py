# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnFireHurtEvent(ServerEvent):

    def __init__(self, callback):
        super(OnFireHurtEvent, self).__init__(callback)
        self.victim_ = None
        self.src_ = None
        self.fireTime_ = None
        self.cancel_ = None
        self.cancelIgnite_ = None

    def CreateFromArgs(self, args):
        self.victim_ = args.get("victim")
        self.src_ = args.get("src")
        self.fireTime_ = args.get("fireTime")
        self.cancel_ = args.get("cancel")
        self.cancelIgnite_ = args.get("cancelIgnite")
