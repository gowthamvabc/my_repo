try:
    x = int("abc")
except ValueError:
    print("Error")
finally:
    print("True")
