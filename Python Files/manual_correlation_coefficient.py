#!/usr/bin/env python
# coding: utf-8

# Code snippet to explain the math behind calculating a correlation coefficient
# As published on the AlgoTrading101 blog

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0,10,size=(5, 2)), columns=list('xy'))
print(df)
print(df.x.mean())

df['step1'] = df.x - df.x.mean()
print('step 1')
print(df)

df['step2'] = df.y - df.y.mean()
print('step 2')
print(df)

df['step3'] = df.step1 * df.step2
print('step 3')
print(df)

step4 = df.step3.sum()
print('step 4')
print(step4)

df['step5'] = df.step1 ** 2
df['step6'] = df.step2 ** 2
print('steps 5 & 6')
print(df)

step7 = df.step5.sum() * df.step6.sum()
step8 = np.sqrt(step7)
r = step4/step8

print('final results')
print(r) # manually calculated pearson correlation coefficient
print(df.x.corr(df.y))  #comparison with the Pandas calculation