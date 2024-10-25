# BJMF-SignIn

## 克隆

将项目克隆到本地或者下载 zip 压缩包

## 填写信息

### 获取 URL 和 个人 cookie

1. 打开 [Fiddler](https://www.telerik.com/download/fiddler-everywhere)和班级魔方找到 `/student/punchs` 开头的链接点开

   ![image](https://github.com/MRYUHUI/BJMF-SignIn/blob/main/assets/README/image-20241025212245071.png)

2. 在右侧的 `raw` 里找到 url 和 cookie

   ![image](https://github.com/MRYUHUI/BJMF-SignIn/blob/main/assets/README/image-20241025214215403.png)

## 获取需要的坐标

使用 [腾讯位置服务](https://lbs.qq.com/getPoint/) 获取自己的 GPS 定位

## 修改代码里的信息

1. 打开 `BJMF-SignIn.py` 
2. 将自己的 名字（非必要）和 cookie 填入 `userCookieDicts`， 填入一次即可
3. 填入 url （每天都更新）
4. 运行程序
