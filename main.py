import random

result = random.randint(0,37)

if result == 0:
  print('Pay 0.')
elif result == 37:
  print('Pay 00.')
else:
  print(f'Pay {result}.')
  if result % 2:
    print('Pay odd.')
  else:
    print('Pay even.')
  if result in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
    print('Pay red.')
  else:
    print('Pay black.')
  if result <= 18:
    print('Pay 1 to 18.')
  else:
    print('Pay 19 to 36.')
