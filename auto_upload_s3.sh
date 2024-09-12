#!/bin/bash

# Thư mục cần theo dõi
WATCH_DIR="/mnt/pve/hddex/dump"  # Đường dẫn tới thư mục bạn muốn theo dõi

# Bucket S3
S3_BUCKET="s3://s9-csvm-backup"

# Sử dụng inotify để theo dõi các tệp mới hoặc được di chuyển vào
inotifywait -m -e close_write -e moved_to --format "%w%f" "$WATCH_DIR" | while read NEW_FILE
do
    # Kiểm tra xem tệp có phải là tệp thông thường không (loại trừ thư mục)
    if [ -f "$NEW_FILE" ]; then
        echo "New file detected or moved: $NEW_FILE"

        # Tải lên S3 trong nền (background)
        (
            aws s3 cp "$NEW_FILE" "$S3_BUCKET"
            if [ $? -eq 0 ]; then
                echo "Uploaded $NEW_FILE to $S3_BUCKET successfully."
            else
                echo "Failed to upload $NEW_FILE to $S3_BUCKET."
            fi
        ) &
    fi
done
