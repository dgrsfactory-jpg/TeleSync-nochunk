#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Installing TeleSync for Termux..."

# Update and install system dependencies
echo "[*] Updating Termux packages..."
pkg update -y && pkg upgrade -y

echo "[*] Installing Python and Git..."
pkg install -y python git

# Install pip dependencies
echo "[*] Installing Python dependencies..."
pip install -r requirements.txt

# Copy example config if config.json doesn't exist yet
if [ ! -f config.json ]; then
    cp example.config.json config.json
    echo "[*] Created config.json from example — fill in your details:"
    echo ""
    echo "    nano config.json"
    echo ""
else
    echo "[*] config.json already exists, skipping..."
fi

# Make run.sh executable
chmod +x run.sh

# Add TeleSync to PATH via ~/.bashrc
TELESYNC_DIR="$(pwd)"
BASHRC="$HOME/.bashrc"

if ! grep -q "TeleSync" "$BASHRC" 2>/dev/null; then
    echo "" >> "$BASHRC"
    echo "# TeleSync" >> "$BASHRC"
    echo "export PATH=\"\$PATH:$TELESYNC_DIR\"" >> "$BASHRC"
    echo "[+] Added TeleSync to PATH in ~/.bashrc"
    echo "[*] Run 'source ~/.bashrc' or restart Termux to apply."
else
    echo "[*] TeleSync already in PATH, skipping..."
fi

echo ""
echo "[+] Installation complete!"
echo ""
echo "    Usage:"
echo "      ./run.sh upload <file_or_dir>"
echo "      ./run.sh upload <file_or_dir> --delete"
echo ""
echo "    After sourcing ~/.bashrc you can run from anywhere:"
echo "      run.sh upload <file_or_dir>"
