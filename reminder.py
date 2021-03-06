#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle


class Reminder:
    rmd_list = {}

    def __init__(self):
        try:
            f = open('rmd_list.data', 'rb')
        except:
            f = open('rmd_list.data', 'wb')
            pickle.dump({}, f)
            f.close()
            f = open('rmd_list.data', 'rb')
        self.rmd_list = pickle.load(f)
        f.close()

    def write(self):
        f = open('rmd_list.data', 'wb')
        pickle.dump(self.rmd_list, f)
        f.close()

    def add(self, uid, rmd_time, rmd_times, rmd_msg):
        if uid not in self.rmd_list:
            self.rmd_list[uid] = [[rmd_time, rmd_times, rmd_msg]]
        else:
            self.rmd_list[uid].append([rmd_time, rmd_times, rmd_msg])
        self.write()

    def clear(self, uid):
        if uid in self.rmd_list:
            self.rmd_list.pop(uid)
            self.write()

    def list(self, uid):
        if uid in self.rmd_list:
            return self.rmd_list[uid]
        else:
            return None

    def check(self, current_time):
        return_list = []
        for uid in self.rmd_list:
            for record in self.rmd_list[uid]:
                if record[0] == current_time:
                    return_list.append([uid, record[2]])
                    record[1] = record[1] - 1
                    if record[1] <= 0:
                        self.rmd_list[uid].remove(record)
                    self.write()
        return return_list
