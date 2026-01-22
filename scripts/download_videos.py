"""
Tencent Meeting Video Downloader Helper

This script helps manage the download process for Tencent Meeting recordings.
It waits for downloads to complete and moves files to the target directory.
"""

import os
import sys
import time
import shutil
from pathlib import Path


def wait_for_downloads(downloads_dir=None, timeout=300):
    """
    Wait for all Chrome downloads to complete.

    Args:
        downloads_dir: Path to Downloads folder (defaults to user Downloads)
        timeout: Maximum seconds to wait (default 300)

    Returns:
        List of completed .mp4 file paths
    """
    if downloads_dir is None:
        downloads_dir = Path.home() / "Downloads"
    else:
        downloads_dir = Path(downloads_dir)

    print(f"Monitoring downloads folder: {downloads_dir}")

    start_time = time.time()
    completed_files = []

    while time.time() - start_time < timeout:
        # Check for .crdownload files (Chrome temporary downloads)
        temp_files = list(downloads_dir.glob("*.crdownload"))

        if not temp_files:
            # No active downloads, get recent mp4 files
            mp4_files = list(downloads_dir.glob("*.mp4"))
            if mp4_files:
                # Sort by modification time, get most recent
                mp4_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
                completed_files = mp4_files
                break

        time.sleep(2)

    return completed_files


def move_files(files, target_dir):
    """
    Move files to target directory.

    Args:
        files: List of file paths to move
        target_dir: Target directory path

    Returns:
        List of moved file paths
    """
    target_dir = Path(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    moved = []
    for file in files:
        dest = target_dir / file.name
        shutil.move(str(file), str(dest))
        moved.append(dest)
        print(f"Moved: {file.name} -> {dest}")

    return moved


def main():
    if len(sys.argv) < 2:
        print("Usage: python download_videos.py <target-directory>")
        print("Example: python download_videos.py .")
        sys.exit(1)

    target_dir = sys.argv[1]

    print("Waiting for downloads to complete...")
    completed = wait_for_downloads()

    if completed:
        print(f"Found {len(completed)} completed download(s)")
        moved = move_files(completed, target_dir)
        print(f"Successfully moved {len(moved)} file(s)")
    else:
        print("No completed downloads found within timeout period")


if __name__ == "__main__":
    main()
