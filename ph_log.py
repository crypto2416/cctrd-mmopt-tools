#!/usr/bin/python
import glob, os
import copy
import csv
import functools

class DeltaRow:
    def __init__(self):
        self.timestamp = ''
        self.key = ''
        self.delta = 0.0
        self.accout_delta = {}

    def get_dict_row(self):
        d = {'timestamp': self.timestamp, 'portolio_key': self.key, 'delta': self.delta} 
        for k, v in self.accout_delta.items():
            d[k] = v
        return d

    def __str__(self):
        head = '|{}|{}|{}|'.format('timestamp', 'key', 'delta')            
        value = '|{}|{}|{}|'.format(self.timestamp, self.key, self.delta)
        for k, v in self.accout_delta.items():
            head += '{}|'.format(k)
            value += '{}|'.format(v)
        return head + '\r\n' + value
            

files = glob.glob("./3_13_9_3_14/**/*.log", recursive=True)

files.sort()

print(files)

lines = []

for file in files:
    with open(file) as f:
        lines += f.readlines()

rows = []
state =  0
row = DeltaRow()
for l in lines:
    if 'Account,Delta' in l:
        row = DeltaRow()
        state = 1
    elif state == 1: # check accounts
        if l.strip():
            account, delta = l.split(',')
            row.accout_delta[account.strip()] = delta.strip()
            # row.headers.add(account)
        else:
            state = 2
    elif 'INF' in l and state == 2:
        x = l.split(' ')
        row.timestamp = x[0]
    elif 'Portfolio Key' in l and state == 2:
        x = l.split(' ')
        row.key = x[-1].strip()
    elif 'portfolio $ delta' in l and state == 2:
        x = l.split(' ')
        row.delta = x[-1].strip()
        rows.append(copy.deepcopy(row))
        state = 0


with open('ph.csv', 'w', newline='') as csvfile:
    headers = set()
    
    for r in rows:
        headers.update(r.accout_delta.keys())
    
    headers = list(headers)
    print(headers)

    def symbol_first(x, y):
        xs = x.split('_')[-1]
        ys = y.split('_')[-1]
        return 1 if xs > ys else -1 if xs < ys else 0
        # return x.split('_')[-1] < y.split('_')[-1]
    headers = sorted(headers, key = functools.cmp_to_key(symbol_first))
    print(headers)

    headers = ['timestamp', 'portolio_key', 'delta'] + headers

    
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for r in rows:
        print(r)
        writer.writerow(r.get_dict_row())
