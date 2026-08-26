from pathlib import Path 
import argparse
import os 
import shutil

def path_folder(_path):
    folder_path = Path(_path)

    documents = [
    ".pdf", ".txt", ".docx", ".doc", ".docm", ".dotx", ".rtf", ".odt", 
    ".ott", ".wpd", ".pages", ".tex", ".md", ".rst", ".epub", ".mobi",
    ".xlsx", ".xls", ".xlsm", ".xltx", ".xlsb", ".csv", ".tsv", ".ods", ".ots",
    ".numbers",".pptx", ".ppt", ".pptm", ".potx", ".ppsx", ".odp", ".otp", ".key",
    ".html", ".htm", ".xml", ".json", ".yaml", ".yml", ".xhtml", ".xps", 
    ".oxps"
    ]





    videos = [
    ".mp4",".mpg",".mpeg",".avi",".wmv",".mov",".rm",
    ".ram",".swf",".flv",".ogg",".webm",".mkv",".m4v",".3gp",".3g2",".asf",".vob",".mts",".m2ts",
    ".ts",".ogv",".qt",".divx",".xvid",".f4v",".f4p",".f4a",".f4b",".m2v",".m4p",".amv",".viv",
    ".svi",".roq",".nsv",".mxf",".yuv",".rmvb",".asx",".dvr-ms",".wtv",".ogm",".ogx",".gvi"
    ]




    system_files = [
    ".iso", ".exe", ".msi", ".bat", ".cmd", ".sh", ".bin", ".dmg", ".app",
    ".jar", ".vmdk", ".vhd", ".vhdx", ".img", ".cue", ".mdf", ".toast", ".deb", ".rpm",
    ".com", ".gadget", ".wsf", ".vbs", ".ps1", ".ink", ".sys", ".dll", ".drv", ".cpl",
    ".cab", ".msu", ".inf", ".reg", ".ini", ".cfg", ".log", ".bak", ".tmp", ".crdownload",
    ".tar", ".gz", ".zip", ".rar", ".7z", ".pkg", ".apk", ".ipa", ".run", ".elf"
]




    musics = [
    ".mp3", ".wav", ".aac", ".flac", ".m4a", ".wma", ".ogg", ".oga", ".opus", ".alac",
    ".aif", ".aiff", ".aifc", ".ape", ".wv", ".mpc", ".m4b", ".m4p", ".m4r", ".mp2",
    ".amr", ".awb", ".gsm", ".dct", ".dss", ".msv", ".dvf", ".vox", ".mmf", ".iklax",
    ".mid", ".midi", ".rmi", ".kar", ".mod", ".s3m", ".xm", ".it", ".mtm", ".uax",
    ".pcm", ".dsd", ".dff", ".dsf", ".sacd", ".cda", ".w64", ".caf", ".rf64", ".mka"
    ]





    photos = [
    ".jpg", ".jpeg", ".png", ".jpe", ".gif", ".svg", ".svgz", ".eps", ".webp", ".tiff",
    ".tif", ".bmp", ".ico", ".raw", ".cr2", ".nef", ".arw", ".dng", ".heic", ".heif",
    ".avif", ".psd", ".ai", ".indd", ".jfif", ".pjpeg", ".pnm", ".ppm", ".pgm",
    ".pbm", ".tga", ".dds", ".hdr", ".exr", ".pic", ".pct", ".pict", ".mac", ".pcx",
    ".ani", ".cur", ".icns", ".wbmp", ".wmf", ".emf", ".svgz", ".cgm", ".gbr", ".pat"
    ]




    # # Creating Folders
    system_files_dir = folder_path / "System_Files"
    system_files_dir.mkdir(exist_ok=True)

    documents_dir = folder_path / "Documents"
    documents_dir.mkdir(exist_ok=True)

    musics_dir = folder_path / "Musics"
    musics_dir.mkdir(exist_ok=True)

    photos_dir = folder_path / "Photos"
    photos_dir.mkdir(exist_ok=True)

    videos_dir = folder_path / "Videos"
    videos_dir.mkdir(exist_ok=True)

    unknown_dir = folder_path / "Unknown"
    unknown_dir.mkdir(exist_ok=True)


    
    for item in folder_path.rglob('*'):
        if item.is_file():

            if item.suffix.lower() in musics:
                shutil.move(str(item), musics_dir)

            elif item.suffix.lower() in system_files:
                shutil.move(str(item), system_files_dir)

            elif item.suffix.lower() in videos:
                shutil.move(str(item), videos_dir)

            elif item.suffix.lower() in photos:
                shutil.move(str(item), photos_dir)

            elif item.suffix.lower() in documents:
                shutil.move(str(item), documents_dir)

            else:
                shutil.move(str(item), unknown_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean a target folder.")
    parser.add_argument(
        "--path", required=True, help="The full path to the folder to clean"
    )

    args = parser.parse_args()

    path_folder(args.path)