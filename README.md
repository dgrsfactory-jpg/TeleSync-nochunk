# TeleSync-nochunk

An application to store your selected files on Telegram. Upload Only and nothing else
a files must ≤ 2GB

## Features

- Infinite storage (No limit)
- Easy to use
- Fast and secure (encrypt ur own files manually or using your own script)
- Free & Open Source

## Prerequisites

You need a Telegram API ID and API Hash.
You can create a new App [here](https://my.telegram.org/apps).

## Installation

```bash
git clone https://github.com/dgrsfactory-jpg/TeleSync-nochunk.git
cd TeleSync-nochunk
```

> ⚠️: In order to install the dependencies flawlessly, please follow the instructions step-by-step.

## Linux

```bash 
python -m venv venv
source venv/bin/activate
```

## Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

Then, continue with the installation:

```bash 
pip install -r requirements.txt
# Copy the example.config.json to config.json
cp example.config.json config.json # Edit the config.json file with your own settings
```

Next, give the `run.sh` Shell-Script executable permissions:

```bash
chmod +x run.sh
```

## Configuration

| Option         | Description                                                                 |
| -------------- | ----------------------------------------------------------------------------|
| `api_id`       | Your Telegram API ID.                                                       |
| `api_hash`     | Your Telegram API Hash.                                                     |
| `phone_number` | Your phone number, which you use for Telegram.                              |
| `channel`      | "me" your own Saved Messages or "@channelname" a public channel username    |
| `verbose`      | If `true`, the application will print more information. (Default: `false`)  |


### Commands

| Command                 | Description                            |
| ----------------------- | -------------------------------------- |
| `upload [FILE_QUERY]`   | Upload a file to Telegram              |


`FILE_QUERY` can be the file name, file path, the ID of the file, or a part of the file name.

## Adding Script to PATH

### Linux

To add the script to the PATH in Linux, you can modify the `~/.bashrc` file:

```bash
export PATH="$PATH:/path/to/TeleSync"
```
### Windows

To add the script to the PATH in Windows, you can follow these steps:

1. Search for "Environment Variables" in the Start menu.
2. Click on "Edit the system environment variables".
3. In the System Properties window, click on the "Environment Variables..." button.
4. In the Environment Variables window, under System variables, find the Path variable and select it.
5. Click on the "Edit..." button.
6. Click on the "New" button and add the path to the TeleSync directory.
7. Click "OK" on all windows to apply the changes.


## Running

### Linux

To run TeleSync on Linux, navigate to the TeleSync directory in your terminal and execute the following command:

```bash
./run.sh [COMMAND] [ARGUMENTS]
```

### Windows

To run TeleSync on Windows, open Command Prompt, navigate to the TeleSync directory, and execute the following command:

```bash
.\run.bat [COMMAND] [ARGUMENTS]
```

> ⚡: If you added `TeleSync` to your `PATH`, you may run the script from anywhere.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Issues

If you find a **bug**, please to open an [issue](https://github.com/FujiwaraChoki/TeleSync/issues). Issues that are not related to bugs will be closed.

## Contributing

Only **Pull Request**s with **fixes** or/and **improvements** will be accepted.
