import os

# Get file system statistics for the root directory
stat = os.statvfs('/')

# Calculate free space in bytes
# stat[0] is the block size, stat[3] is the number of free blocks
free_bytes = stat[0] * stat[3]

print("Free storage:", free_bytes, "bytes")
print("Free storage:", free_bytes / 1024, "KB")