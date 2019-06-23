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

def randomFunction(res):
    err = [.1, 2]
    log_func = math.log(res)+ random.uniform(err[0], err[1])
    return log_func
print(randomFunction(.9))    



