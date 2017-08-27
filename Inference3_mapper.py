#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 12:
		DRGdef, id, name, address, city, state, zip, ref, discharge, avgCoveredCharge, avgTotalPayment, avgMediPayments = data
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(state, DRGdef, discharge,avgCoveredCharge, avgTotalPayment, avgMediPayments)