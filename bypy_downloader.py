from bypy import ByPy
import sys


bp = ByPy(
    configdir="./bypy_config",
    downloader="aria2",
    retry=10,
)
print("=============== files under /app/ ===============")
bp.list()
print("=============== start downloading ===============")


bp.download(
    remotepath=sys.argv[1],
    localpath=sys.argv[2],
)