import torch
from d2l import torch as d2l
from IPython import display


batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

# 将展平每个图像,将它视为长度为784的向量.
# 因为我们的数据集有10个类别,所以网络输出维度为10
num_inputs = 784
num_outputs = 10

w = torch.normal(0, 0.01, size=(num_inputs, num_outputs), requires_grad=True)
b = torch.zeros(num_outputs, requires_grad=True)

# # 给定一个矩阵X, 可以对所有的元素求和.
# X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
# X.sum(0, keepdim=True), X.sum(1, keepdim=True)


def softmax(X):
    X_exp = torch.exp(X)
    partition = X_exp.sum(1, keepdim=True)
    return X_exp / partition  # 这里应用了广播机制


def net(X):
    return softmax(torch.matmul(X.reshape(-1, w.shape[0]), w) + b)


# 实现交叉熵损失函数.
def cross_entroy(y_hat, y):
    return -torch.log(y_hat[range(len(y_hat)), y])


# 将预测类别与真实y元素进行比较
def accuracy(y_hat, y):
    """计算预测正确的数量"""
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())


accuracy(y_hat, y) / len(y)


# 可以评估在任意模型net的准确率
def evaluate_accuracy(net, data_iter):
    """计算在指定数据集上模型的精度."""
    if isinstance(net, torch.nn.Module):
        net.eval()  # 将模型设置为评估模式
    metric = Accumulator(2)  # 正确预测数,预测总数
    for X, y in data_iter:
        metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]


class Accumulator:
    """在'n'个变量上累加"""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


evaluate_accuracy(net, test_iter)


# 没写完,不想写了


