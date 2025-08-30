import PyPDF2

reader = PyPDF2.PdfReader('The Ultimate Python Handbook.pdf')
text_content = ""

for i in range(min(10, len(reader.pages))):
    page = reader.pages[i]             
    text_content += page.extract_text()
      
with open("Text.txt", "w", encoding="utf-8") as f:
    f.write(text_content)
