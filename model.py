import re

class MOMLModel:
    def parse_text1(self, text):
        # สร้างรูปแบบ regex เพื่อตรวจจับ tag และข้อความที่ไม่ได้แท็ก
        pattern = r'<([^>]+)>(.*?)</\1>|<([^>]+)\/>|([^<]+)'
        # ค้นหาคำที่ตรงกับรูปแบบ regex
        #findall อ่านทั้งหมด
        matches = re.findall(pattern, text)
        # สร้างรายการผลลัพธ์
        results = []
        for match in matches:
            if match[0]:
                # หากมี tag และข้อความรอบตัวมัน
                tag = match[0]
                content = match[1]
                results.append(f'[TAG= "{tag}"]{{{content}}}')
            elif match[2]:
                tag = match[2]
                content = match[3]
                results.append(f'[TAG= "{tag}"]{{{content}}}')
            elif match[3]:
                # หากไม่มี tag
                content = match[3].strip()
                if content:
                    results.append(f'[UNTAGGED]{{{content}}}')
        
        textString = "\n".join(results)
        return textString


    def parse_text2(self, text):
        # สร้างรูปแบบ regex เพื่อตรวจจับ tag และข้อความที่ไม่ได้แท็ก
        pattern = r'<([^>]+)>(.*?)</\1>|<([^>]+)\/>|([^<]+)'
        # ค้นหาคำที่ตรงกับรูปแบบ regex
        #finditer อ่านทีละบรรทัด
        matches = re.finditer(pattern, text)
        # สร้างรายการผลลัพธ์
        results = []
        for match in matches:
            if match.group(1):
                # หากมี tag และข้อความรอบตัวมัน
                tag = match.group(1)
                content = match.group(2)
                results.append(f'[TAG= "{tag}"]{{{content}}}')
            elif match.group(3):
                tag = match.group(3)
                content = ""
                results.append(f'[TAG= "{tag}"]{{{content}}}')
            elif match.group(4):
                # หากไม่มี tag
                content = match.group(4).strip()
                if content:
                    results.append(f'[UNTAGGED]{{{content}}}')
        
        textString = "\n".join(results)
        return textString
