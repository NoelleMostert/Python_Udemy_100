import ephem

jupiter = ephem.Jupiter()
jupiter.compute('1230/01/01')
print('%s %s %s' % (jupiter.ra, jupiter.dec, jupiter.mag))