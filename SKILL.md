---
name: tencent-meeting-download
description: Download video recordings from Tencent Meeting (meeting.tencent.com) web pages. Automatically detects all available video sources (speaker view and screen share view), displays video information (resolution, type), allows user to select which videos to download, and moves completed downloads to the current working directory. Works on Windows environment with Chrome DevTools. Use when user asks to: (1) Download Tencent Meeting recordings, (2) Extract videos from meeting.tencent.com/cw/ URLs, (3) Save Tencent Meeting recording files
---

# Tencent Meeting Recording Downloader

## Overview

This skill downloads video recordings from Tencent Meeting (meeting.tencent.com) pages. Recordings typically contain two video sources:
- **Speaker view** (`*_speaker.mp4`) - Camera footage (1920x1080)
- **Screen share view** (`*_screen.mp4`) - PPT/desktop sharing (2560x1440)

## Workflow

### 1. Navigate to the recording page

Use Chrome DevTools to navigate to the Tencent Meeting URL:

```javascript
mcp__chrome-devtools__navigate_page({ type: "url", url: "<meeting-url>" })
```

### 2. Detect all video sources

Get all video elements and their information:

```javascript
mcp__chrome-devtools__evaluate_script({
  function: () => {
    const videos = document.querySelectorAll('video');
    return Array.from(videos).map((v, i) => ({
      index: i,
      src: v.src,
      currentSrc: v.currentSrc,
      videoWidth: v.videoWidth,
      videoHeight: v.videoHeight,
      duration: v.duration
    }));
  }
})
```

### 3. Present video options to user

Display the detected videos with their details:
- Resolution (width x height)
- Type (speaker/screen based on filename)
- Duration
- File size estimate

Ask user which video(s) to download.

### 4. Trigger download via browser

Create a download link and click it:

```javascript
mcp__chrome-devtools__evaluate_script({
  function: async (videoUrl, filename) => {
    const link = document.createElement('a');
    link.href = videoUrl;
    link.download = filename;
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    return { success: true };
  },
  args: [{ uid: "element" }] // videoUrl and filename
})
```

### 5. Wait for download completion

Monitor Downloads folder for `.crdownload` temporary files:

```bash
# PowerShell - wait for download to finish
powershell -Command "while (Test-Path '$env:USERPROFILE\Downloads\*.crdownload') { Start-Sleep -Seconds 5 }"
```

### 6. Move to current directory

Move downloaded file from Downloads to working directory:

```bash
powershell -Command "Move-Item -Path '$env:USERPROFILE\Downloads\<filename>' -Destination '<current-dir>\<filename>' -Force"
```

## Video URL Pattern

Tencent Meeting recording URLs follow this pattern:
```
https://ylz.cos.meeting.tencent.com/cos/<path>/<timestamp>-<meeting-id>-recording-1_<type>.mp4?token=<token>
```

Types:
- `speaker` - Camera/speaker view
- `screen` - Screen share view

## Notes

- Token in URLs expires after some time - always extract fresh URLs from the page
- Downloads go to Chrome's default Downloads folder first
- File sizes can be 200-400 MB depending on recording length
- The browser must have cookies/session active for download to work (403 Forbidden if token expires)
