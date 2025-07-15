import subprocess
import time
import os

SCRIPT_PATH = "DevX Team Lag.py"  # أو المسار الكامل

while True:
    if not os.path.isfile(SCRIPT_PATH):
        print(f"🚫 الملف غير موجود: {SCRIPT_PATH}")
        print("⏳ تأكد من المسار وحاول ثانية بعد 5 ثواني...")
        time.sleep(5)
        continue

    print("🟢 تشغيل البوت...")
    try:
        p = subprocess.Popen(["python3", SCRIPT_PATH])
        p.wait()
    except Exception as e:
        print(f"❌ حدث خطأ أثناء تشغيل البوت: {e}")

    print("🔴 البوت توقف! إعادة تشغيل بعد 5 ثواني...")
    time.sleep(5)