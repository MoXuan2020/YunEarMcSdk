# -*- coding: utf-8 -*-

from YunEarMcSdk.entity.Entity import Entity
from YunEarMcSdk.event.ClientEvent import ClientEvent


class AddEntityClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AddEntityClientEvent, self).__init__(callback)
        self.entity = None

    def CreateFromArgs(self, args):
        self.entity = Entity(self, args.get("id"))
