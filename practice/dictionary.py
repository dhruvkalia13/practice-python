"""
think HashMap<Key, Value>
JAVA
mMap = new HashMap<String, Integer>();
mMap.put("key", 1);
PYTHON3
version 1:
mMap = {}
mMap["key"] = value
"""

def putInMap():
    mMap = {}
    mMap["dhruv"] = 1
    mMap["ishan"] = 2
    mMap["dhru"] = 3
    mMap["ish"] = 4
    mMap["dh"] = 5
    mMap["i"] = 6
    mMap[""] = 7
    print(type(mMap))
    print(type(mMap.items()))
    print(type(mMap.values()))
    return mMap
"""
{
    dhruv : None
    ishan : None
    dhruv : None
    dhruv : 
    dhruv : 1
}

# dict cannot be a key
# mMap[mMapNested] = "dhruv"
# get

"""
def getFromMap(mMap, key):
    return mMap[key]

def printAllMap(mMap):
    # print only keys
    for item in mMap:
        print(item)
    # print only values
    for item in mMap.values():
        print(item)
    # print both together
    for key, value in mMap.items():
        print('key: ', key, ':', 'value: ', value)


def contains(mMap, keyToCheck):
    return keyToCheck in mMap

def remove(mMap, keyToRemove):
    del mMap[keyToRemove]

newMap = putInMap()
print(getFromMap(newMap, "dhruv"))
print(printAllMap(newMap))
print(contains(newMap, 'dhruv'))
remove(newMap, 'dhruv')
print(contains(newMap, 'dhruv'))
