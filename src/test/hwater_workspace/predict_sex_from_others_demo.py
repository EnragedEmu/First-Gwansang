from celeba_download_demo import Curdir_loader

list_attr_celeba_filename = 'list_attr_celeba.txt'
cl = Curdir_loader()
import torch
import torch.nn as nn
import torch.optim as optim

df = cl.load_file_asDF(list_attr_celeba_filename).replace(to_replace=-1, value=0)
num_data = 202599

X = df.drop(labels=0, axis=0).drop(['Male'], axis=1).drop(['Name'], axis=1)
y = df['Male']

train_size = 180000
test_size = num_data - train_size - 1
X_train = X.iloc[:train_size]
y_train = y.iloc[:train_size]
X_test = X.iloc[train_size:]
y_test = y.iloc[train_size:]

input_size = X_train.shape[1]
output_size = 2

X_train = torch.FloatTensor(X_train.values)
y_train = nn.functional.one_hot(torch.tensor(y_train.values), num_classes=2).type(torch.FloatTensor)
X_test = torch.FloatTensor(X_test.values)
y_test = nn.functional.one_hot(torch.tensor(y_test.values), num_classes=2).type(torch.FloatTensor)

layers = nn.Sequential(nn.Linear(input_size, 20), 
                       nn.GELU(), 
                       nn.Linear(20, output_size))
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(layers.parameters())

epoch_num = 10
batch_iter = 100
batch_size = int(train_size / batch_iter)
X_train_batch = X_train.split(batch_size, dim=0)
y_train_batch = y_train.split(batch_size, dim=0)

accurate = 0
for i in range(test_size):
    if torch.argmax(layers(X_test[i])) == torch.argmax(y_test[i]):
        accurate += 1

print('Primary test acc: ', accurate / test_size)

for epoch in range(epoch_num):
    for i in range(batch_iter):
        hypo = layers(X_train_batch[i])
        loss = loss_fn(hypo, y_train_batch[i])
        loss.backward()
        optimizer.step()

    print('Epoch: {:2d} | loss: {}'.format(epoch + 1, loss.item()))

accurate = 0
for i in range(test_size):
    if torch.argmax(layers(X_test[i])) == torch.argmax(y_test[i]):
        accurate += 1

print('Final test acc: ', accurate / test_size)
