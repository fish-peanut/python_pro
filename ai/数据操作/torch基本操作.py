import torch
import numpy

# x = torch.arange(12)
# print(x)
#
# print(x.shape)
#
# print(x.numel())
#
# x = x.reshape(3, 4)
# print(x)

# print(torch.zeros(2, 3, 4))
#
# print(torch.ones(2, 3, 4))

# x = torch.tensor([[[2, 3, 4, 5], [8, 9, 7, 5], [11, 12, 33, 1]]]).shape
# print(x)

x = torch.tensor([1.0, 2, 3, 4])
y = torch.tensor([2, 2, 2, 2])

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
# print(torch.exp(x))

# x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
# y = torch.tensor([[2.0, 3, 4, 5], [8, 9, 6, 7], [11, 12, 33, 1]])
# # print(torch.cat((x, y), dim=0))
# # print(torch.cat((x, y), dim=1))
# print(x.sum())

# x = torch.arange(3).reshape(3, 1)
# y = torch.arange(2).reshape(1, 2)
# print(x)
# print(y)
# print(x+y)

# x = torch.arange(12).reshape(3, 4)
# y = torch.arange(12).reshape(3, 4)
# # print(x)
# # print(x[-1])
# # print(x[1, 3])
# # print(x[1:2])
# # x[1, 2] = 999
# # x[0:2, :] = 999
# before = id(y)
# y += x
# # y = y + x
# print(id(y) == before)

# x = torch.arange(12).reshape(3, 4)
# A = x.numpy()
# B = torch.tensor(A)
# print(type(A))
# print(type(B))

# a = torch.tensor(3.55)
# print(a)
# print(a.item())
# print(float(a))
# print(int(a))

# x = torch.arange(12).reshape(3, 4)
# print(x)
# print(x[::2, ::3])
