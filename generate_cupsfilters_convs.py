#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import shutil

def copy_file(dir)
    src_name = '/cupsfilters.convs.in'
    dest_name = '/cupsfilters.convs'
    src_file = dir + src_name
    dest_file = dir + dest_name
    print(f'copy from %s to %s', src_file, dest_file)
    shutil.copy2(src_file, dest_file)

def main():
    args = sys.argv[1:]
    print(f'args: {args}')
    copy_file(args[0])
    return 0

if __name__ == '__main__':
    sys.exit(main())