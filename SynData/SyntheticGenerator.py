"""
Copyright (c) 2019 P.S Narayanan
ALL RIGHTS RESERVED.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
PS Narayanan, thepsnarayanan@gmail.com
"""
import math
import random
import pandas as pd


def randomFunction(res):
    err = [5,10]
    a = 650000
    log_func = a * math.log(1 + res)
    return log_func

def main():
    print(math.log(2))    
    n = int(input("Total no of rows to generate:"))
    data = []
    for i in range(n):
        randCPU = random.uniform(0.0,1.0)
        data +=[[randCPU, randomFunction(randCPU)]] 
    df = pd.DataFrame(data, columns=['CPU','throughput'])
    df.to_csv("data/GeneratedData.csv", sep=',')

main()


