#coding=gbk

import numpy as np
import matplotlib.pyplot as plt

N = 20
D = 2
K = 5

X = np.zeros((N * K, D))

y = np.zeros(N * K, dtype='uint8')

for j in range(K):
    ix = range(N * j, N * (j + 1))
    r = np.linspace(0.0, 1, N)
    t = np.linspace(j * 4, (j + 1) * 4, N) + np.random.randn(N) * 0.2
    X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
    y[ix] = j
    
# ��ʼ��Ȩ�غ�ƫ��
W = 0.01 * np.random.randn(D, K)
b = np.zeros((1, K))
step_size = 1e-0
reg = 1e-3 # regularization strength

# ��ȡѵ����������
num_examples = X.shape[0]
for i in range(200):
    # �������÷�
    scores = np.dot(X, W) + b
    # ���� softmax�÷�
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    # ʹ�ý�������ʧ
    correct_log_probs = -np.log(probs[range(num_examples), y])
    # ����ѵ������data loss���ܵ���ʧ������������
    data_loss = np.sum(correct_log_probs) / num_examples
    # ������������ʧreg loss��ʹ��L2����
    # reg����lambda
    reg_loss = 0.5 * reg * np.sum(W * W)
    # �����ܵ���ʧ����
    loss = data_loss + reg_loss
    if i%10 == 0:
        print("iteration %4d loss: %f" % (i, loss))
    # �����ݶȣ����򴫲�
    dscores = probs
    dscores[range(num_examples), y] -= 1
    dscores /= num_examples
    dW = np.dot(X.T, dscores)
    db = np.sum(dscores, axis=0, keepdims=True)
    dW += reg * W # ��������ݶȣ�dW���ǵ�һ�γ��֣������ۼ�
    # ���²���
    W += -step_size * dW
    b += -step_size * db

# ѵ������������׼ȷ��
scores = np.dot(X, W) + b

# �ڵڶ���ά�ȣ����ά�ȣ�ȡ��������ߵķ���
predicted_class = np.argmax(scores, axis=1)

print("Training accuracy: %.2f" % (np.mean(predicted_class == y)))