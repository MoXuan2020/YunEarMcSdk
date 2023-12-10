# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityDieLoottableServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityDieLoottableServerEvent, self).__init__(callback)
        self.dieEntityId = None
        self.attacker = None
        self.itemList = None
        self.dirty = None

    def CreateFromArgs(self, args):
        self.dieEntityId = args.get("dieEntityId")
        self.attacker = args.get("attacker")
        self.itemList = args.get("itemList")
        self.dirty = args.get("dirty")
