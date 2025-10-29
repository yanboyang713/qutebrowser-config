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

## To Do

-   Update cutsom config
-   Update Youtube adblock
-   Update themes

## References

-   Qutebrowser Official Help [Documentation](https://qutebrowser.org/doc/help/)
-   Qutebrowser Arch WIki [Documentation](https://wiki.archlinux.org/title/qutebrowser)

## License

MIT / BSD

## Author Information

This Code was created in 2024 by [Asapdotid](https://github.com/asapdotid).
