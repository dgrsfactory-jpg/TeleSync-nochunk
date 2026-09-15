import os

from config import *
from tqdm import tqdm
from termcolor import colored
from telethon import TelegramClient

VERBOSE = get_verbose()
PHONE = get_phone()
CHANNEL = get_channel()

if VERBOSE:
    import logging
    logging.basicConfig(level=logging.DEBUG)


class Telegram:
    def __init__(self):
        self._api_id = get_telegram_api_id()
        self._api_hash = get_telegram_api_hash()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        session_path = os.path.join(script_dir, "anon.session")
        if VERBOSE:
            print(colored("[INFO] Initializing Telegram Client...", "magenta"))
        self._client = TelegramClient(session=session_path, api_id=self._api_id, api_hash=self._api_hash)
        if VERBOSE:
            print(colored(f"[INFO] Connecting to Telegram via \"{PHONE}\"", "magenta"))
            print(colored(f"[INFO] Uploading to channel \"{CHANNEL}\"", "magenta"))
        self._client.start(phone=PHONE)

    @property
    def client(self):
        return self._client

    def upload_file(self, current_dir: str, file_path: str, file_name: str):
        print(colored(f"[*] Uploading {file_name} to {CHANNEL}...", "magenta"))
        absolute_path = os.path.abspath(os.path.join(current_dir, file_path))
        file_size = os.path.getsize(absolute_path)

        with tqdm(
            total=file_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            desc=file_name,
            colour="green",
        ) as progress:
            last_sent = [0]

            def _progress(sent, total):
                progress.total = total
                progress.update(sent - last_sent[0])
                last_sent[0] = sent

            self.client.send_file(CHANNEL, absolute_path, progress_callback=_progress)

        print(colored(f"[+] Uploaded \"{file_name}\" to {CHANNEL}.", "green"))

    def upload_directory(self, current_dir: str, dir_path: str, dir_name: str):
        print(colored(f"[*] Uploading directory \"{dir_name}\" to {CHANNEL}...", "magenta"))
        absolute_path = os.path.abspath(os.path.join(current_dir, dir_path))

        all_files = [
            f for f in os.listdir(absolute_path)
            if os.path.isfile(os.path.join(absolute_path, f))
        ]
        total_files = len(all_files)

        with self.client.start() as client:
            for idx, file in enumerate(all_files, start=1):
                file_abs_path = os.path.join(absolute_path, file)
                file_size = os.path.getsize(file_abs_path)

                print(colored(f"\n[{idx}/{total_files}] Uploading {file}...", "magenta"))

                with tqdm(
                    total=file_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    desc=file,
                    colour="green",
                ) as progress:
                    last_sent = [0]

                    def _progress(sent, total, _p=progress, _l=last_sent):
                        _p.total = total
                        _p.update(sent - _l[0])
                        _l[0] = sent

                    client.send_file(CHANNEL, file_abs_path, progress_callback=_progress)

        print(colored(f"\n[+] Uploaded \"{dir_name}\" to {CHANNEL}.", "green"))
