import numpy as np
allans = np.load('./data/allans.npy')
import network
settings = network.Settings()
num_classes = settings.num_classes - 1
print(int(len(allans)/num_classes))
#运行比较慢，看来是加载network文件比较慢!