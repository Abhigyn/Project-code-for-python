import os

def createfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        try:
            os.replace(file, f"{foldername}/{file}")
        except Exception as e:
            print(f"Could not move {file}: {e}")

# List all files
files = os.listdir()

# Create folders
# createfolder("a")
# createfolder("games")
createfolder("movies")
createfolder("images")
createfolder("docs")
createfolder("audio")
createfolder("Pograms")
# createfolder("compressed")
# createfolder("executables")
# createfolder("webfiles")
# createfolder("system")

# Extensions
imgExit = [".png",".webm",".jpg",".jpeg",".ico",".gif",".svg",".webp",".bmp"]
docExit = [".txt",".doc",".docx",".pptx",".pdf",".xls",".xlsx"]
mediaExit = [".mp4",".mkv",".mov",".avi",".webm"]
audioExit = [".mp3",".m4a",".wav",".ogg",".flac"]
compressExit = [".rar",".7z",".zip"]
executableExit = [".exe",".apk",".msi"]
webfileExit = [".html",".css",".cpp",".cs",".py",".json",".js"]
PogramsExit = [".html",".css",".cpp",".cs",".py",".json",".js"]
systemExit = [".sys",".log",".dll"]

# Categorize
images = [f for f in files if os.path.splitext(f)[1].lower() in imgExit]
docs = [f for f in files if os.path.splitext(f)[1].lower() in docExit]
media = [f for f in files if os.path.splitext(f)[1].lower() in mediaExit]
audio = [f for f in files if os.path.splitext(f)[1].lower() in audioExit]
compressed = [f for f in files if os.path.splitext(f)[1].lower() in compressExit]
executables = [f for f in files if os.path.splitext(f)[1].lower() in executableExit]
webfiles = [f for f in files if os.path.splitext(f)[1].lower() in webfileExit]
Pograms = [f for f in files if os.path.splitext(f)[1].lower() in PogramsExit]
system = [f for f in files if os.path.splitext(f)[1].lower() in systemExit]

# Move them
move("images", images)
move("docs", docs)
move("movies", media)
move("audio", audio)
move("compressed", compressed)
move("executables", executables)
move("webfiles", webfiles)
move("system", system)

print("✅ Sorting complete!")
if __name__ == '__main__':
    pass
    