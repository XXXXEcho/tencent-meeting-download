# Tencent Meeting Recording Downloader

[中文文档](README.zh-CN.md) | English

A Claude Code skill for downloading video recordings from Tencent Meeting (meeting.tencent.com) web pages.

## Features

- Automatically detects all available video sources (speaker view and screen share view)
- Displays video information including resolution, type, and duration
- Downloads videos through browser with proper authentication
- Automatically moves downloaded files to the current working directory
- Works on Windows with Chrome DevTools

## Video Types

Tencent Meeting recordings typically contain two video sources:

| Type | Filename | Resolution | Description |
|------|----------|------------|-------------|
| **Screen** | `*_screen.mp4` | 2560x1440 | Screen share/PPT display |
| **Speaker** | `*_speaker.mp4` | 1920x1080 | Camera/speaker view |

## How It Works

1. Navigate to the Tencent Meeting recording URL
2. Extract video URLs from the page's video elements
3. Present available video options to the user
4. Trigger browser download for selected videos
5. Wait for download completion
6. Move files from Downloads folder to working directory

## Usage

### Installing the Skill

1. Copy the `.skill` file to your Claude Code skills directory:
   ```
   Windows: %USERPROFILE%\.claude\skills\
   ```

2. Or clone this repository to your skills directory:
   ```bash
   git clone https://github.com/XXXXEcho/tencent-meeting-download.git %USERPROFILE%\.claude\skills\tencent-meeting-download
   ```

### Using the Skill

Simply ask Claude to download a Tencent Meeting recording:

```
"Download the video from https://meeting.tencent.com/cw/XXXXXX"
"Help me download this Tencent Meeting recording"
```

Claude will automatically:
- Open the meeting page
- Detect available videos
- Ask which video(s) to download
- Download and save to the current directory

## Requirements

- **OS**: Windows
- **Browser**: Chrome/Edge with DevTools support
- **Claude Code**: With MCP Chrome DevTools integration

## Technical Details

### Video URL Pattern

```
https://ylz.cos.meeting.tencent.com/cos/<path>/<timestamp>-<meeting-id>-recording-1_<type>.mp4?token=<token>
```

### Token Authentication

Video URLs include authentication tokens that expire over time. Always extract fresh URLs from the page rather than reusing old links.

### File Sizes

Typical file sizes for 3-hour recordings:
- Screen video: ~400 MB
- Speaker video: ~200 MB

## Troubleshooting

### 403 Forbidden Error

If download fails with 403 error, the token may have expired. Refresh the page and try again.

### Download Stuck

Check Chrome's Downloads page (Ctrl+J) to see download progress.

### File Not Found

Ensure the Downloads folder path is correct:
```
C:\Users\<Username>\Downloads\
```

## Project Structure

```
tencent-meeting-download/
├── SKILL.md              # Skill definition for Claude Code
├── scripts/
│   └── download_videos.py # Python helper script
├── references/           # (optional) Additional documentation
└── README.md             # This file
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Created for Claude Code users who need to download Tencent Meeting recordings efficiently.
