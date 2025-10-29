# Qutebrowser Custom Configuration

qutebrowser (pronounced "cute browser") is a QTwebengine web browser for Linux, Windows, and macOS operating systems with Vim-style key bindings and a minimal GUI. It is keyboard driven and takes inspiration from similar software such as Vimperator and dwb. Use DuckDuckGo as your default search engine. qutebrowser is included in the native repositories of Linux distributions such as Fedora and Arch Linux. qutebrowser was developed by Florian Bruhin and in 2016 he won the CH Open Source Award.

## Setup Config

Clone this repo direct to user config `~/.config/qutebrowser`:

```bash
git clone --depth 1 https://github.com/asapdotid/qutebrowser-config.git ~/.config/qutebrowser
```

OR

Clone to your `project/lab` directory:

```bash
git clone --depth 1 https://github.com/asapdotid/qutebrowser-config.git
```

Link project to user config `~/.config/qutebrowser`:

```bash
ln -s $PWD/qutebrowser-config ~/.config/qutebrowser
```

Instruction configuration:

-   cd to Qutebrowser project
-   Setup environment: `make ini` and update or using default value on `.env`
-   Copy env example: `cp ~/.config/qutebrowser/.env.example ~/.config/qutebrowser/.env`
-   Reload config: `<space> + r`
-   Reload window: `<space> + R`
-   If config not reload properly, please restart Qutebrowser `(close and open)` app

## Support

-   Environment variables
-   Themes
-   Adblock Brave
-   Youtube Adblock

## Extras

### Adblock (Brave engine)

Install the adblock dependency and update lists:

```bash
# Arch Linux
sudo pacman -S python-adblock

# In qutebrowser (command mode)
:adblock-update
```

### Spellcheck dictionary (en-US)

Install the English (US) dictionary:

```bash
/usr/share/qutebrowser/scripts/dictcli.py install en-US
```

Then restart qutebrowser (e.g., `:restart`).

For Bitwarden integration (rbw), see the "Userscripts: qute-rbw (Bitwarden)" section below.

## Authenticator App (TOTP)

Use an authenticator app (TOTP) with Bitwarden and rbw.

- Enable in Bitwarden Web Vault: Settings → Security → Two-step Login → Authenticator App (TOTP).
- Ensure rbw is configured for the US cloud:
  - `rbw config set base_url https://vault.bitwarden.com`
  - `rbw config set email <your-email>`
- Log in with TOTP:
  - `rbw login` (enter master password via pinentry when prompted)
  - When asked for 2FA, enter the 6‑digit TOTP from your authenticator.
- Retrieve TOTP codes stored in your vault items (Bitwarden Premium):
  - `rbw get --totp "<item name>"`
  - Example copy to clipboard (Linux): `rbw get --totp "GitHub" | xclip -selection clipboard`
- Common issues:
  - HTTP 400 on login: verify server URL, email, and update rbw (`rbw --version`).
  - SSO or non‑TOTP 2FA isn’t supported by rbw; use TOTP or email 2FA.
  - Config file: `~/.config/rbw/config.json`.

## Userscripts: qute-rbw (Bitwarden)

Use the qute-rbw userscript to fill usernames and copy passwords from Bitwarden (rbw) in qutebrowser — no download needed if the userscript already exists on your system.

- Link userscripts directory (so qutebrowser finds your scripts):
  - `mkdir -p ~/.config/qutebrowser/userscripts`
  - `ln -s ~/.config/qutebrowser/userscripts ~/.local/share/qutebrowser/userscripts`
- Keybindings (add in `~/.config/qutebrowser/config.py`):
  - Run userscript: `config.bind(",bw", "spawn --userscript qute-rbw")`
  - Autofill username + copy password: `config.bind("ea", "spawn --userscript qute-rbw --autofill")`
- Usage flow:
  - Click the username field on the page.
  - Press `ea` (or run `:spawn --userscript qute-rbw --autofill`).
  - The userscript pastes the username and copies the password to the clipboard for you to paste.
- Requirements:
  - `rbw` installed and unlocked (`rbw login`, then `rbw unlock`)
  - A picker: `fuzzel` (recommended) or `rofi` / `dmenu` / `fzf`
  - Clipboard tool: Wayland `wl-clipboard` (wl-copy/wl-paste) or X11 `xclip`/`xsel`

## References

-   Qutebrowser Official Help [Documentation](https://qutebrowser.org/doc/help/)
-   Qutebrowser Arch WIki [Documentation](https://wiki.archlinux.org/title/qutebrowser)

## License

MIT / BSD

## Author Information

This Code was created in 2024 by [Asapdotid](https://github.com/asapdotid).
