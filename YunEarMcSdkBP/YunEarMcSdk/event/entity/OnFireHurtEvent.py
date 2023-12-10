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
        self.victim_ = args["victim"]
        self.src_ = args["src"]
        self.fireTime_ = args["fireTime"]
        self.cancel_ = args["cancel"]
        self.cancelIgnite_ = args["cancelIgnite"]
