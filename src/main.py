"""
By using `TeleSync`, you agree to the following terms and conditions:
- No warranty is provided. Use at your own risk.
- You will not use this tool for any illegal activities.
- You will not use this tool to upload or download any illegal content.

If you do not agree to these terms, do not use this tool.

This tool is provided as is, and is not affiliated with Telegram in any way.

Author: @FujiwaraChoki
Date: 08.02.2024
Version: 1.0.4
GitHub: https://github.com/FujiwaraChoki/TeleSync

Licensed under the GNU General Public License v3.0.
See the LICENSE file for more information.
"""

import os
import sys
import shutil

from telegram import Telegram
from termcolor import colored


def main():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

    # Check if `config.json` exists
    config_file = os.path.join(ROOT_DIR, "config.json")
    if not os.path.exists(config_file):
        print(colored("[-] Couldn't find your config file.", "red"))
        sys.exit(1)

    args = sys.argv[1:]

    if len(args) == 0:
        print(colored("[-] No arguments provided. Usage: tls upload <file_or_dir> [--delete]", "red"))
        sys.exit(1)

    command = args[0]

    if command == "upload":
        if len(args) < 2:
            print(colored("[-] Not enough arguments provided. Usage: tls upload <file_or_dir> [--delete]", "red"))
            sys.exit(1)

        current_dir = os.getcwd()
        file_path = args[1]
        file_name = os.path.basename(file_path)
        delete_after = "--delete" in args

        if not os.path.exists(file_path):
            print(colored(f"[-] \"{file_path}\" does not exist.", "red"))
            sys.exit(1)

        telegram = Telegram()

        if os.path.isdir(file_path):
            telegram.upload_directory(current_dir, file_path, file_name)
        else:
            telegram.upload_file(current_dir, file_path, file_name)

        if delete_after:
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(colored(f"[+] Deleted directory \"{file_name}\".", "yellow"))
            else:
                os.remove(file_path)
                print(colored(f"[+] Deleted \"{file_name}\".", "yellow"))

        sys.exit(0)

    print(colored(f"[-] Unknown command \"{command}\". Available command: upload", "red"))
    sys.exit(1)


if __name__ == "__main__":
    main()
