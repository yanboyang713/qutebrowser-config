# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

import os
from os.path import join, dirname
from time import localtime, strftime
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Reassign to avoid lsp(ruff_lsp) errors
config = config  # noqa: F821
c = c  # noqa: F821

config.load_autoconfig()

# Variables
leader = os.environ.get("LEADER_KEY")
ss_dir = os.environ.get("SCREENSHORT_DIR")
dl_dir = os.environ.get("DOWNLOAD_DIR")
terminal = os.environ.get("TERMINAL")
editor = os.environ.get("EDITOR")
username = os.environ.get("GITHUB_USERNAME")
homepage = os.environ.get("HOMEPAGE")
timestamp = strftime("%Y-%m-%d-%H-%M-%S", localtime())  # updates on every config-source

# General
c.editor.command = [terminal, "-e", editor, "{}"]
c.downloads.location.directory = dl_dir
c.zoom.default = "100%"
c.tabs.show = "switching"
c.statusbar.show = "in-mode"
c.auto_save.session = True
c.url.auto_search = "naive"
c.completion.height = "33%"
c.downloads.position = "bottom"
c.input.insert_mode.auto_load = True
c.spellcheck.languages = ["en-US"]
c.confirm_quit = ["always"]

# Tabs
c.tabs.favicons.scale = 1.0
c.tabs.background = True

# User agent
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3 Firefox/121",
    "*",
)

# Dark mode
config.set("colors.webpage.darkmode.enabled", False)
config.set("colors.webpage.preferred_color_scheme", "auto")

# File handling
config.set("fileselect.handler", "external")
config.set(
    "fileselect.single_file.command", [terminal, "-e", "ranger", "--choosefile", "{}"]
)
config.set(
    "fileselect.multiple_files.command",
    [terminal, "-e", "ranger", "--choosefiles", "{}"],
)

# Enable Brave browser adblocker
# Install the python-adblock package and enable the adblocker within qutebrowser
config.set("content.blocking.method", "both")

# Theme
config.source("themes/manjaro-dark.py")

# Font
font_size = "11pt"
font_family = "FiraCode Nerd Font"
font = font_size + " " + font_family
# Set fonts
c.fonts.default_size = font_size
c.fonts.default_family = font_family
c.fonts.completion.entry = font
c.fonts.hints = font
c.fonts.debug_console = font
c.fonts.prompts = font
c.fonts.statusbar = font

# Content
c.content.pdfjs = True
c.content.autoplay = False

# Home page
c.url.open_base_url = True
c.url.start_pages = homepage
c.url.default_page = homepage

# Search engines
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "am": "https://amazon.com/s?k={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "bn": "https://bing.com/search?q={}",
    "dd": "https://duckduckgo.com/?q={}",
    "gh": "https://github.com/search?q={}",
    "gg": "https://google.com/search?q={}",
    "gho": "https://github.com/{}",
    "ghr": "https://github.com/" + username + "/{}",
    "jr": "https://springhealth.atlassian.net/browse/{}",
    "mp": "https://google.com/maps?q={}",
    "rd": "https://reddit.com/search/?q={}",
    "rds": "https://reddit.com/r/{}",
    "rt": "https://rottentomatoes.com/search?search={}",
    "so": "https://stackoverflow.com/search?q={}",
    "sp": "https://open.spotify.com/search/{}",
    "tw": "https://twitter.com/search?q={}",
    "ud": "https://urbandictionary.com/define.php?term={}",
    "wk": "https://en.wikipedia.org/wiki/{}",
    "yt": "https://youtube.com/results?search_query={}",
    "ytm": "https://music.youtube.com/search?q={}",
}

# Aliases
c.aliases = {
    "o": "open",
    "q": "quit",
    "Q": "close",
    "w": "session-save",
    "x": "quit --save",
}

# Keybindings
config.bind("t", "cmd-set-text -s :open -t")
config.bind("O", "cmd-set-text -s :open -w")
config.bind("P", "cmd-set-text -s :open -p")
config.bind("W", "tab-clone -w")
config.bind("a", "mode-enter insert")

config.bind("K", "back")
config.bind("J", "forward")
config.bind("H", "tab-prev")
config.bind("L", "tab-next")
config.bind("Q", "tab-close")

config.bind("<Ctrl-=>", "zoom-in")
config.bind("<Ctrl-->", "zoom-out")

config.bind(leader + "b", "config-cycle statusbar.show always in-mode")
config.bind(leader + "B", "config-cycle tabs.show multiple switching")
config.bind(leader + "c", "config-edit")
config.bind(leader + "C", "cmd-set-text -s :set -t")
config.bind(leader + "d", "devtools")
config.bind(leader + "D", "devtools-focus")
config.bind(leader + "e", "edit-text")
config.bind(leader + "E", "cmd-edit")
config.bind(leader + "i", "hint inputs")
config.bind(leader + "I", "open -t https://github.com/2kabhishek/qute2k")
config.bind(leader + "h", "history")
config.bind(leader + "H", "help")
config.bind(leader + "m", "bookmark-list")
config.bind(leader + "M", "bookmark-add")
config.bind(leader + "n", "tab-clone")
config.bind(leader + "N", "tab-clone -w")
config.bind(leader + "o", "hint links window")
config.bind(leader + "O", "hint links run :open -p {hint-url}")
config.bind(leader + "p", "tab-pin")
config.bind(leader + "P", "cmd-set-text -s :tab-move")
config.bind(leader + "q", "tab-close")
config.bind(leader + "Q", "close")
config.bind(leader + "r", "config-source")
config.bind(leader + "R", "restart")
config.bind(leader + "s", "screenshot " + ss_dir + "qute-" + timestamp + ".png")
config.bind(leader + "S", "view-source --edit")
config.bind(leader + "t", "cmd-set-text -s :tab-select")
config.bind(leader + "T", "tab-only")
config.bind(leader + "u", "undo")
config.bind(leader + "v", "hint links spawn mpv {hint-url}")
config.bind(leader + "V", "hint links spawn " + terminal + "-e youtube-dl {hint-url}")
config.bind(leader + "w", "cmd-set-text -s :tab-take")
config.bind(leader + "W", "tab-give")
config.bind(leader + "y", "hint links yank")
config.bind(leader + "x", "quit --save")
config.bind(leader + "X", "window-only")

config.bind("p", "tab-pin")
config.bind(";w", "hint link spawn --detach mpv --force-window yes {hint-url}")
config.bind(";W", "spawn --detach mpv --force-window yes {url}")
config.bind(
    ";I",
    "hint images spawn --output-message wget -P " + dl_dir + "images/ -c {hint-url}",
)

# Password management
config.bind("ee", "spawn --userscript qute-pass")
config.bind("eu", "spawn --userscript qute-pass --username-only")
config.bind("ep", "spawn --userscript qute-pass --password-only")
config.bind("eo", "spawn --userscript qute-pass --otp-only")
