import os
import pandas as pd
import requests
from tqdm import tqdm
from pathlib import Path

# ✅ File upload for Replit
def upload_csv():
    from replit import file
    print("📁 Upload your CSV file (with columns: id, user_id, video_id)...")
    uploaded = file.upload()
    csv_path = list(uploaded.keys())[0]
    print(f"✅ Uploaded: {csv_path}")
    return csv_path

# ✅ Check if video is a Short (no redirect = short)
def is_youtube_short(video_id):
    url = f"https://www.youtube.com/shorts/{video_id_
