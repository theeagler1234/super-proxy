<p align="center">
	<img src="https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png" alt="Ubuntu Linux" width="160">
</p>

# Browser-accessible Ubuntu desktop

This project runs an Ubuntu XFCE desktop through the browser using the LinuxServer Webtop image.

## Start

From the repository directory, run:

```sh
./reopen-os.sh
```

The script starts the desktop and waits until the container is healthy.

In VS Code, open the **Ports** panel and open port `3000` (`Ubuntu desktop (HTTP)`). Port `3001` is also forwarded for HTTPS redirects.

## Login

Use these credentials:

| Field | Value |
| --- | --- |
| Username | `ubuntu` |
| Password | `change-this-password` |

Change `PASSWORD` in `docker-compose.yml` before sharing or using this desktop for anything sensitive.

## Stop

```sh
./close-os.sh
```

Desktop files persist in `ubuntu-desktop-config/`.

## First-time Codespaces setup

If ports `3000` and `3001` do not appear in the Ports panel, run **Codespaces: Rebuild Container** from the VS Code Command Palette, then run `./reopen-os.sh` again. The ports are configured in `.devcontainer/devcontainer.json`.