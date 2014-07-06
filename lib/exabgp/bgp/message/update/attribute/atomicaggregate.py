# encoding: utf-8
"""
atomicaggregate.py

Created by Thomas Mangin on 2012-07-14.
Copyright (c) 2009-2013 Exa Networks. All rights reserved.
"""

from exabgp.bgp.message.update.attribute.attribute import Attribute
from exabgp.bgp.message.update.attribute.flag import Flag
from exabgp.bgp.message.update.attribute.id import AttributeID
from exabgp.bgp.message.notification import Notify


# =================================================================== AtomicAggregate (6)

class AtomicAggregate (Attribute):
	ID = AttributeID.ATOMIC_AGGREGATE
	FLAG = Flag.TRANSITIVE
	MULTIPLE = False
	CACHING = True

	__slots__ = []

	def pack (self,asn4=None):
		return self._attribute('')

	def __len__ (self):
		return 0

	def __str__ (self):
		return ''

	def __cmp__ (self,other):
		if not isinstance(other,self.__class__):
			return -1
		return 0

	def __hash__ (self):
		return 0

	@classmethod
	def unpack (cls,data,negotiated):
		if data:
			raise Notify(3,2,'invalid ATOMIC_AGGREGATE %s' % [hex(ord(_)) for _ in data])
		return cls()

	@classmethod
	def setCache (cls):
		# There can only be one, build it now :)
		cls.cache[AttributeID.ATOMIC_AGGREGATE][''] = cls()

AtomicAggregate.register_attribute()
AtomicAggregate.setCache()
