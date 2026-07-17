import os

# ضع رابط خادمك هنا (مثلاً رابط الـ Codespace أو ريندر إذا قررت استخدامه مستقبلاً)
# تأكد أن الرابط بنفس طول الرابط القديم أو أقل (ونقوم بملء الفراغات بـ أصفار)
NEW_URL = "https://your-revival-url.app.github.dev" 

def patch_file(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # الروابط التي نريد استبدالها داخل التطبيق
    targets = [
        b"https://www.roblox.com",
        b"https://api.roblox.com",
        b"http://www.roblox.com",
        b"http://api.roblox.com"
    ]
    
    modified = False
    for target in targets:
        if target in content:
            padded_url = NEW_URL.encode('utf-8').ljust(len(target), b'\x00')
            content = content.replace(target, padded_url)
            modified = True
            print(f"✅ تم تعديل الرابط في: {file_path}")
            
    if modified:
        with open(file_path, 'wb') as f:
            f.write(content)

# البحث في ملفات التطبيق بعد فكه
for root, dirs, files in os.walk("./extracted_apk"):
    for file in files:
        if file.endswith(".so") or file.endswith(".dex") or file.endswith(".xml"):
            patch_file(os.path.join(root, file))
