# -*- coding: utf-8 -*-


class Event(object):

    def __init__(self, callback):
        self.callback = callback
        self.mod = None

    def BindMod(self, mod):
        self.mod = mod

    def __call__(self, args):
        self.callback(self.mod, args)
