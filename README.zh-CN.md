# 腾讯会议录屏下载器

用于从腾讯会议 (meeting.tencent.com) 网页下载录制视频的 Claude Code 技能。

## 功能特性

- 自动检测所有可用的视频源（发言人视角和屏幕共享视角）
- 显示视频信息，包括分辨率、类型和时长
- 通过浏览器下载视频，带有正确的身份验证
- 自动将下载的文件移动到当前工作目录
- 在 Windows 环境下使用 Chrome DevTools 工作

## 视频类型

腾讯会议录制通常包含两个视频源：

| 类型 | 文件名 | 分辨率 | 描述 |
|------|--------|--------|------|
| **屏幕共享** | `*_screen.mp4` | 2560x1440 | 屏幕共享/PPT 展示 |
| **发言人** | `*_speaker.mp4` | 1920x1080 | 摄像头/发言人画面 |

## 工作原理

1. 导航到腾讯会议录制 URL
2. 从页面的视频元素中提取视频 URL
3. 向用户展示可用的视频选项
4. 为选定的视频触发浏览器下载
5. 等待下载完成
6. 将文件从 Downloads 文件夹移动到工作目录

## 使用方法

### 安装技能

1. 将 `.skill` 文件复制到你的 Claude Code 技能目录：
   ```
   Windows: %USERPROFILE%\.claude\skills\
   ```

2. 或克隆此仓库到你的技能目录：
   ```bash
   git clone https://github.com/XXXXEcho/tencent-meeting-download.git %USERPROFILE%\.claude\skills\tencent-meeting-download
   ```

### 使用技能

只需告诉 Claude 下载腾讯会议录制：

```
"下载 https://meeting.tencent.com/cw/XXXXXX 的视频"
"帮我下载这个腾讯会议录屏"
```

Claude 将自动：
- 打开会议页面
- 检测可用的视频
- 询问要下载哪个视频
- 下载并保存到当前目录

## 系统要求

- **操作系统**: Windows
- **浏览器**: 支持 DevTools 的 Chrome/Edge
- **Claude Code**: 需要集成 MCP Chrome DevTools

## 技术细节

### 视频 URL 格式

```
https://ylz.cos.meeting.tencent.com/cos/<路径>/<时间戳>-<会议ID>-recording-1_<类型>.mp4?token=<令牌>
```

### 令牌验证

视频 URL 包含会过期的身份验证令牌。请始终从页面提取新的 URL，而不是重用旧链接。

### 文件大小

3 小时录制的典型文件大小：
- 屏幕视频：约 400 MB
- 发言人视频：约 200 MB

## 常见问题

### 403 Forbidden 错误

如果下载失败并显示 403 错误，令牌可能已过期。刷新页面后重试。

### 下载卡住

检查 Chrome 的下载页面（Ctrl+J）查看下载进度。

### 找不到文件

确保 Downloads 文件夹路径正确：
```
C:\Users\<用户名>\Downloads\
```

## 项目结构

```
tencent-meeting-download/
├── SKILL.md              # Claude Code 的技能定义
├── scripts/
│   └── download_videos.py # Python 辅助脚本
├── references/           # （可选）额外文档
├── README.md             # 英文文档
└── README.zh-CN.md       # 中文文档（本文件）
```

## 许可证

本项目是开源的，采用 MIT 许可证。

## 贡献

欢迎贡献！随时提交问题或拉取请求。

## 作者

为需要高效下载腾讯会议录制的 Claude Code 用户创建。
