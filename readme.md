# PZM - 拼字幕
!(pzm_title_500x200.png)

## Features | 特性
- 快速拼接电影截图字幕
- 目前是半自动操作，但仍省去大量重复劳动
- 与传统方式相比，效率提升 500%+
- 正在向全自动迭代

## Installation | 安装
    pip install pzm

- PZM 目前仅在 Python 3.7 测试通过

## Usage | 用法

### Mac Users Workflow | 苹果用户工作流
- 播放需要截取的视频片段
- 左手按着 ⌘Command 和 ⇧Shift，并在字幕变化的时候按下 `3`
- 将需要生成一张长图的所有截图放入同一个子目录

#### 例如

├── Screen Shot 2018-08-28 at 3.42.52 PM.png

└── Screen Shot 2018-08-28 at 3.42.54 PM.png

└── Screen Shot 2018-08-28 at 3.43.01 PM.png

- 手动测量字幕起始位置&高度
- 在存放截图的目录里运行 

        pzm <start> <end>

- `:start:` 字幕区域起始位置

- `:end:` 字幕区域结束位置
- 例如

        pzm -200 -100

### Tips
- 所有图片必须大小相同、图片格式相同（正常情况下连续截全屏就可以）
- 目录里可以有其他非图片文件，将自动忽略
- 建议留出 15% 左右的 bleeding

## Contributing | 贡献代码
欢迎。

## #TODO

- [ ] 自适应参数
- [ ] 自动检测字幕位置&高度
- [ ] 递归处理子目录

## License | 开源协议

![http://www.wtfpl.net/]("http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png")

## Author | 作者

[nosoyyo](https://www.zhihu.com/people/paulcarino)