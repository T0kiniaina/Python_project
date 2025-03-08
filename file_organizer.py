import os
import shutil
from pathlib import Path

video = [
    ".mp4", ".mkv", ".webm", ".flv", ".vob", ".ogv", ".ogg", ".drc", ".gif", ".gifv", ".mng", ".avi", ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".asf", ".amv", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mpg", ".mpeg", ".m2v", ".m4v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b"
]

audio = [
    ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff", ".alac", ".opus", ".amr", ".mid", ".midi", ".pcm", ".aif", ".au", ".ra", ".rm", ".caf", ".ac3", ".dts", ".mpa", ".weba"
]

images = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".heif", ".heic", ".raw", ".ico", ".jfif", ".ppm", ".pgm", ".pbm", ".pnm", ".hdr", ".exr", ".ai", ".eps", ".indd", ".psd"
]

documents = [
    ".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt", ".tex", ".wpd", ".md", ".xls", ".xlsx", ".csv", ".tsv", ".ods", ".ppt", ".pptx", ".odp", ".pages", ".key", ".numbers", ".epub", ".mobi", ".azw", ".azw3", ".log", ".xml", ".json", ".yaml", ".yml"
]

archives = [
    ".zip", ".rar", ".7z", ".tar", ".tar.gz", ".tgz", ".tar.xz", ".txz", 
    ".tar.bz2", ".tbz2", ".gz", ".xz", ".bz2", ".iso", ".img", 
    ".cab", ".arj", ".lzh", ".ace", ".z", ".apk", ".deb", ".rpm", 
    ".cpio", ".jar", ".war", ".ear"
]


path = input("Entrez le chemin du dossier : ")
path = Path(path)
if not path.exists():
    print("Le dossier n'existe pas")
    exit()
video_path = path / "Video"
audio_path = path / "Audio"
images_path = path / "Images"
documents_path = path / "Documents"
archives_path = path / "Archives"

dir_path = [video_path, audio_path, images_path, documents_path, archives_path]

for i in dir_path:
    i.mkdir(exist_ok=True)

files = os.listdir(path)

for file in files:
    path_file = path / file
    if path_file.suffix in video :
        shutil.move(path_file, video_path)
    elif path_file.suffix in audio:
        shutil.move(path_file, audio_path)
    elif path_file.suffix in documents:
        shutil.move(path_file, documents_path)
    elif path_file.suffix in images:
        shutil.move(path_file, images_path)
    elif path_file.suffix in archives:
        shutil.move(path_file, archives_path)

print("Opération terminé")