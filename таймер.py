import time
sec = int(input())
for sec in reversed(range(sec)):
    time.sleep(1)
    print(sec)
print("Бум! Бах! Бдыщ!")