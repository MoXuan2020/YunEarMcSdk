# -*- coding: utf-8 -*-

from YunEarMcSdk.entity.Entity import Entity
from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddEntityServerEvent(ServerEvent):

    def __init__(self, callback):
        super(AddEntityServerEvent, self).__init__(callback)
        self.entity = None

    def CreateFromArgs(self, args):
        self.entity = Entity(args.get("id"))
