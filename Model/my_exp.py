import torch
import torch.nn as nn
from torch.autograd import Variable as V
from torch.autograd import Function
import torch.nn.functional as F


class M_Exp(nn.Module):
    def __init__(self):
        super(M_Exp, self).__init__()

    def forward(self, input1):
        '''
        n=input1.shape[0]
        dim=input1.shape[1]

        one=torch.ones(input1.shape).cuda()
        e=torch.eye(dim).cuda()

        output=torch.exp(input1)
        output=output-one+e
        #print('exp output',output)

        #print('M_Exp finish')
        '''

        n = input1.shape[0]
        dim = input1.shape[1]

        eighty = ((torch.eye(dim).cuda()) * 10).repeat(n, 1, 1)
        res = input1 - eighty
        res = F.relu(res)
        input2 = input1 - res  # input2是将input1大于eighty的元素置为eighty，其他的不变

        one = torch.ones(input2.shape).cuda()
        e = torch.eye(dim).cuda()

        output = torch.exp(input2)
        output = output - one + e

        return output