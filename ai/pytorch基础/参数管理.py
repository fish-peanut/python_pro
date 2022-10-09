import torch
from torch import nn

net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 1))
X = torch.rand(size=(2, 4))

# print(net(X))

# print(net[2].state_dict())
#
# print(type(net[2].bias))
# print(net[2].bias)
# print(net[2].bias.data)

# print(net[2].weight.grad is None)

# print(*[(name, param.shape) for name, param in net[0].named_parameters()])
# print(*[(name, param.shape) for name, param in net.named_parameters()])
#
# print(net.state_dict()['2.bias'].data)


def block1():
    return nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 4), nn.ReLU())


def block2():
    net = nn.Sequential()
    for i in range(4):
        net.add_module(f'block {i}', block1())
    return net


# rgnet = nn.Sequential(block2(), nn.Linear(4, 1))
# rgnet(X)
# print(rgnet)


def init_normal(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, mean=0, std=0.01)
        # nn.init.constant_(m.weight, 1)
        """不能将 weight 都置为 1 """
        # nn.init.xavier_uniform_(m.weight)
        # 利用 xavier_uniform_ 函数初始化参数
        nn.init.zeros_(m.bias)


net.apply(init_normal)
print(net[0].weight.data[0], net[0].bias.data[0])




