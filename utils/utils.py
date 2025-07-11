__all__ = ['set_seed', 'makedirs']
import os
import random

import numpy as np
import torch

def set_seed(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    print('seed 고정 완료!')


def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
    print('폴더 확인 완료!!')