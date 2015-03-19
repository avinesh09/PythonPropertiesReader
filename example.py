__author__ = 'Avinesh_Kumar'

import properties

props = properties.loadproperties('python.properties')

print props

print props.get('fast\\')

print props.get('Truth')