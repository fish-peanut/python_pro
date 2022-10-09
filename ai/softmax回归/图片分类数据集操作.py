# ％　matplotlib inline
import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l
# fashion minst


d2l.use_svg_display()


# 通过ToTensor实例将图像数据从pil类型变成32位浮点数格式。
# 并除以255使得所有像素的数值均在0到1之间
trans = transforms.ToTensor()
mnist_train = torchvision.datasets.FashionMNIST(root="../data", train=True, transform=trans, download=True)
mnist_test = torchvision.datasets.FashionMNIST(root="../data", train=False, transform=trans, download=True)
#
# print(len(mnist_train))
# print(len(mnist_test))


# print(mnist_train[0][0].shape)


def get_fashion_mnist_labels(labels):
    """返回Fashion-MNIST数据集的文本标签。"""
    text_labels = [
        't-shirt', 'trouser', 'pullover', 'dress', 'coat',
        'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot'
    ]
    return [text_labels[int(i)] for i in labels]


def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):
    """Plot a list of images."""
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            """图片张量。"""
            ax.imshow(img.numpy())
        else:
            """plt 图片。"""
            ax.imshow(img)
        # d2l.plt.show(img)


X, y = next(iter(data.DataLoader(mnist_train, batch_size=18)))
show_images(X.reshape(18, 28, 28), 2, 9, titles=get_fashion_mnist_labels(y))


batch_size = 256


def get_dataloader_wordkers():
    """使用四个进程来读取数据。"""
    return 4


train_iter = data.DataLoader(mnist_train, batch_size, shuffle=True, num_workers=get_dataloader_wordkers())

timer = d2l.Timer()
for X, y in train_iter:
    continue
print(f'{timer.stop():2f} sec')


def load_data_fashion_mnist(batch_size,resize=None):
    """下载Fashion-MNIST数据集, 然后将其加载到内存中。"""
    trans = [transforms.ToTensor]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(root='../data', train=True, transform=trans, download=True)
    mnist_test = torchvision.datasets.FashionMNIST(root='../data', train=False, transform=trans, download=True)
    return (data.DataLoader(mnist_train, batch_size, shuffle=True, num_workers=get_dataloader_wordkers()),
            data.DataLoader(mnist_train, batch_size, shuffle=True, num_workers=get_dataloader_wordkers()))


