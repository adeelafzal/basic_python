a = 4
b = 0

try:
    result = a/b
    print("Result:", result)
except Exception as e:
    print("Exception occured", e)
finally:
    print("Execute every time")

print("End of execution")