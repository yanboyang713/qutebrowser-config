import os
from os.path import join, dirname, expanduser
from dotenv import load_dotenv
from time import localtime, strftime
from libs.utility import to_bool

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)


class Variable:
    leader = ""
    ss_dir = ""
    dl_dir = ""
    terminal = ""
    editor = ""
    username = ""
    homepage = ""
    timestamp = ""
    canvas = False
    webgl = False
    font_size = ""
    font_family = ""
    font = ""
    darkmode = False

    # initial constructor to set the values
    def __init__(self):
        # Fallbacks ensure config runs even without a .env
        self.leader = os.environ.get("LEADER_KEY", " ")

        # Directories (ensure sensible defaults and trailing slash where used via string concat)
        default_dl = os.environ.get("DOWNLOAD_DIR", expanduser("~/Downloads/"))
        if not default_dl.endswith("/"):
            default_dl += "/"

        self.dl_dir = os.environ.get("DOWNLOAD_DIR", default_dl)

        default_ss = os.environ.get("SCREENSHORT_DIR", self.dl_dir)
        if not default_ss.endswith("/"):
            default_ss += "/"
        self.ss_dir = default_ss

        # Apps and identity
        self.terminal = os.environ.get("TERMINAL", "xterm")
        self.editor = os.environ.get("EDITOR", "nvim")
        self.username = os.environ.get("GITHUB_USERNAME", "user")
        self.homepage = os.environ.get("HOMEPAGE", "https://duckduckgo.com/")
        self.timestamp = strftime("%Y-%m-%d-%H-%M-%S", localtime())

        # Booleans with robust parsing and safe default False
        self.canvas = to_bool(os.environ.get("CANVAS"), default=False)
        self.webgl = to_bool(os.environ.get("WEBGL"), default=False)

        # Fonts
        size = os.environ.get("FONT_SIZE", "11")
        self.font_size = f"{size}pt"
        self.font_family = os.environ.get("FONT_FAMILY", "monospace")
        self.font = self.font_size + " " + self.font_family
        self.darkmode = to_bool(os.environ.get("DARKMODE"), default=False)
