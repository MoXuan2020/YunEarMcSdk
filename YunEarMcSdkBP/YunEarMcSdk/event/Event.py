# -*- coding: utf-8 -*-


class Event(object):

    def __init__(self, callback):
        self.callback = callback
        self.mod = None

    def __call__(self, args):
        self.CreateFromArgs(args)
        self.callback(self.mod, self)

    def BindMod(self, mod):
        self.mod = mod

    def CreateFromArgs(self, args):
        pass
