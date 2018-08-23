# NetEasePhotoBak
> 网易相册批量下载工具

## 如何使用

1、下载网易相册 APP 抓包获得你的 `token`

2、修改 `ApiService.py` 文件中的 `headers` 中的 `token` 和 api 接口中的用户名

3、运行 `__init__.py`

## 说明
1、文件如果相册中存在失效图片下载该图片会提示，并会打印出该图片地址

2、脚本采用单线程，保证下载及时发现下载失败的文件，有能力可自行修改成多线程

3、文件默认保持在 F://网易相册，如报错请自行新建文件夹

4、下载过程中如果发现目录已经存在不会下载该目录中的文件，会直接跳过，如果下载未完成由于中途报错请删除该文件夹重新运行脚本

## License

```
Copyright 2018 Loofer, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
