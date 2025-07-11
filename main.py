import os
import sys

# 🧠 Auto-install dependencies using importlib and ensurepip
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        import ensurepip
        ensurepip.bootstrap()
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

# Install needed modules
for pkg in ["pandas", "requests", "tqdm"]:
    install_and_import(pkg)

import pandas as pd
import requests
from tqdm import tqdm

# ✅ YouTube Shorts checker
def is_youtube_short(video_id):
    url = f"https://www.youtube.com/shorts/{video_id}"
    try:
        response = requests.get(url, allow_redirects=False, timeout=10)
        return 'short' if response.status_code == 200 else 'long'
    except Exception as e:
        print(f"⚠️ Error checking {video_id}: {e}")
        return 'error'

# ✅ Process batches
def process_videos(csv_path, batch_size):
    df = pd.read_csv(csv_path)
    total_videos = len(df)
    print(f"\n🔢 Total videos to process: {total_videos}")
    
    os.makedirs("exports", exist_ok=True)

    for start in range(0, total_videos, batch_size):
        end = min(start + batch_size, total_videos)
        batch_df = df.iloc[start:end].copy()
        print(f"\n🚀 Processing batch {start // batch_size + 1}: {start + 1} to {end}")
        
        batch_df["video_type"] = [
            is_youtube_short(vid) for vid in tqdm(batch_df["video_id"], desc="🔍 Analyzing")
        ]
        
        export_path = f"exports/export_{start // batch_size + 1}.csv"
        batch_df.to_csv(export_path, index=False)
        print(f"✅ Saved: {export_path}")

# ✅ Entry point
if __name__ == "__main__":
    print("📦 YouTube Shorts Type Checker")
    csv_path = input("📁 Enter path to your CSV file: ").strip()
    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        sys.exit(1)
    batch_size = int(input("🔢 Enter batch size: "))
    process_videos(csv_path, batch_size)
