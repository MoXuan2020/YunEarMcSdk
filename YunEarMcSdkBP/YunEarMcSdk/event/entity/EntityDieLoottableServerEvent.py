# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityDieLoottableServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityDieLoottableServerEvent, self).__init__(callback)
        self.dieEntityId_ = None
        self.attacker_ = None
        self.itemList_ = None
        self.dirty_ = None

    def CreateFromArgs(self, args):
        self.dieEntityId_ = args.get("dieEntityId")
        self.attacker_ = args.get("attacker")
        self.itemList_ = args.get("itemList")
        self.dirty_ = args.get("dirty")
