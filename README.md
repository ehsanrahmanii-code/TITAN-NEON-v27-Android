# TITAN NEON v2.7 PRISM + GEMINI — Android APK

داشبورد کامل تحلیل کریپتو (Flask + Python) با تم نئون Prism Glass، موتور ۲۴ مولفه‌ای، پیش‌بینی، صرافی کاغذی و Gemini AI — به صورت **APK مستقل اندروید**.

## داخل APK
- Python 3.11 + numpy + pandas + flask + waitress + requests (همه داخل APK)
- WebView روی `http://127.0.0.1:8080`
- داده فقط در پوشه **VVV** (حافظه داخلی)
- کلید Gemini اختیاری: در `secret/gemini_api_key.txt` داخل اپ یا مسیر داده

## ساخت APK (یک‌بار)

1. بروید: https://github.com/ehsanrahmanii-code/TITAN-NEON-v27-Android/actions
2. **Build Titan Neon v27 APK** → **Run workflow** → **Run workflow**
3. بعد از ۱۵–۴۵ دقیقه، Artifact به نام `Titan-Neon-v27-APK` را دانلود کنید.
4. یا از Releases آخرین نسخه را بگیرید.

## نصب
- فایل APK را روی گوشی کپی کنید و نصب کنید (Unknown sources).
- در اولین اجرا مجوز **All files access** را تأیید کنید تا پوشه VVV ساخته شود.
- ۳۰–۹۰ ثانیه صبر کنید تا موتور پایتون بالا بیاید.

## نسخه
- **2.7.3-FULL-THEME** — Prism Glass + 20 تم شیشه‌ای + Gemini
- منبع: ZIP اصلی `TITAN_NEON_v27_PRISM_GEMINI`
