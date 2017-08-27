#!/usr/bin/python
import sys
dischargeTotal = 0
coveredChargeTotal = 0
totalPaymentTotal = 0
mediPaymentsTotal = 0
oldKey = None
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 6:
	# Something has gone wrong. Skip this line.
	continue
	thisKey, DRG, discharges, coveredCharge, totalPayment, mediPayments = data_mapped
	if oldKey and oldKey != thisKey:
		print oldKey, "\t", dischargeTotal, "\t", coveredChargeTotal, "\t", totalPaymentTotal, "\t",
	mediPaymentsTotal
	oldKey = thisKey;
	dischargeTotal = 0