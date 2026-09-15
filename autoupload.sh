#!/data/data/com.termux/files/usr/bin/bash

PHOTO_DIR="$HOME/storage/shared/DCIM/Camera"
LOG_FILE="$(dirname "$0")/log.txt"
RUN_SH="$(dirname "$0")/run.sh"

# Create log file if it doesn't exist
touch "$LOG_FILE"

echo "[*] Scanning $PHOTO_DIR..."

# Count how many files will be uploaded
total=0
skipped=0
uploaded=0
failed=0

# Only Select .png files
for file in "$PHOTO_DIR"/*.png; do
    [ -f "$file" ] || continue
    total=$((total + 1))
done

echo "[*] Found $total file(s) in $PHOTO_DIR."
echo ""

for file in "$PHOTO_DIR"/*; do
    [ -f "$file" ] || continue

    filename=$(basename "$file")

    # Skip if already uploaded
    if grep -qF "$filename" "$LOG_FILE"; then
        echo "[~] Skipping \"$filename\" (already uploaded)."
        skipped=$((skipped + 1))
        continue
    fi

    echo "[*] Uploading \"$filename\"..."
    bash "$RUN_SH" upload "$file"

    if [ $? -eq 0 ]; then
        echo "$filename" >> "$LOG_FILE"
        echo "[+] Logged \"$filename\"."
        rm "$file"
        echo "[+] Deleted local file \"$filename\"."
        uploaded=$((uploaded + 1))
    else
        echo "[-] Failed to upload \"$filename\", skipping log."
        failed=$((failed + 1))
    fi

    echo ""
done

echo "================================"
echo "[+] Done."
echo "    Total   : $total"
echo "    Uploaded: $uploaded"
echo "    Skipped : $skipped"
echo "    Failed  : $failed"
echo "================================"
