#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

src = [ i + 1 for i in xrange(54)]

def shuffle(src, count=54, person=3):
  assert person > 0
  rs = {}
  conflict_count = 0
  for i in xrange(person):
    rs.setdefault(i + 1, [])
  for i in xrange(count):
    added = randint(1, count)
    while added not in src:
      added = added + 1 if added < 54 else 1
      conflict_count += 1
    rs[i % person + 1].append(added)
    src[src.index(added)] = 0
  print 'conflict count: %d' % conflict_count
  return rs

rs = shuffle(src, person=3)
for v in rs.values():
  print v
