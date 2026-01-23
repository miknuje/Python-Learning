metros = float(input('Quantos metros andaste? '))

print('Os {:.1f}m que andaste corresponde a: \n{:.1f}mm\n{:.1f}cm\n{:.1f}dam\n{:.2f}hm\n{:.3f}km'.format(metros, metros*1000, metros*100, metros/10, metros/100, metros/1000))
