# PZM - 拼字幕
![](https://img.shields.io/pypi/pyversions/Django.svg?maxAge=2592000)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/nosoyyo)


快速拼接电影截图字幕的命令行工具

![PinZimu](https://github.com/nosoyyo/pzm/blob/master/pzm_title_500x200.png)

## Features | 特性

🚀 将纯手动提升为半自动操作，可省去大量重复劳动

🔥 与传统方式相比，效率提升 500%+

💻 自动化程度稳步提升中

🖥 分别为 Mac/Win 用户进行专门优化

## Installation | 安装
    pip install pzm

❕PZM 目前仅在 Python 3.7 测试通过

## Usage | 用法

### Mac Users Workflow | 苹果用户工作流
- 播放需要截取的视频片段
- 按住 ⌘Command 和 ⇧Shift，并在字幕变化的时候按下 `3`
- 将需要生成一张长图的所有截图放入同一个文件夹

```
pulp fiction
├── Screen Shot 2018-08-28 at 3.42.52 PM.png
├── Screen Shot 2018-08-28 at 3.42.54 PM.png
└── Screen Shot 2018-08-28 at 3.43.01 PM.png
```
- 手动测量字幕起始位置&高度
- 在存放截图的路径里运行 

        MacBook-Air:pulp fiction$ pzm [start] [height] [end]

        参数
        [start]   字幕区域相对底边的起始位置
        [height]  字幕区高度
        [end]     字幕区域相对底边的结束位置
- 例如

        pzm --start -200 --end -100
- 若省略 `flag`，仅使用数字参数，则将按照 `start`、`height`、`end` 的顺序解析

        pzm -200 200
        将被解析为
        pzm --start -200 --height 200
- 最后生成长图上的字幕顺序和文件夹里的图片排序相同

### Windows Users Workflow | Windows 用户工作流

- #TODO

### Tips
- 所有图片必须大小相同、图片格式相同（正常情况下连续截全屏就可以）
- 给存放图片的目录起一个简单的英文名字会方便许多
- 目录里可以有其他非图片文件，将自动忽略
- 建议留出 15% 左右的 bleeding

## #TODO

- [x] 写单元测试
- [x] 自适应参数
- [x] 递归处理子目录
- [ ] ~~测试 win 等其他平台~~
- [ ] 为 Mac 优化
- [ ] 为 Windows 优化
- [ ] 制作演示视频
- [ ] 自动检测字幕位置&高度
- [ ] `--autoclean`   #`autoclean` 只在非`Desktop`文件夹里生效
- [ ] `--desktop`       #在`Desktop`也生效，⚠危险️

## License | 开源协议

![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)

## Author | 作者

[nosoyyo](https://www.zhihu.com/people/nosoyyo)