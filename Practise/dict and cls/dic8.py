Dict = {'tim': 18, 'charli': 22, 'jack': 25, 'rose': 26, 'jilu': 22}
Boys = {'tim': 18, 'charli': 22, 'jack': 25}
Girls = {'rose': 26, 'jilu': 22}
Dict.update({"sarah":9})
Girls.update({"sarah": 9})
del Dict['tim']
studentx = Boys.copy()
studenty = Girls.copy()
print(studentx)
print(studenty)
print(Dict)
print("student name: %s" % list(Dict.items()))
print("student name: %s" % list(Dict.keys()))
print("student age: %s" % list(Dict.values()))