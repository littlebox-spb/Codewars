def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 4:
        return signature[:n]
    else:
        for i in range(3, n):
            signature.append(sum(signature[-3:]))
        return signature


assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print("OK")

"""
# Чужое решение
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
"""
