import re

filepath = 'C:\\Git\\my-endurance-ai\\.github\\workflows\\auto-sync.yml'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the README update section and add git pull before the if statement
old_text = '''SYNC_TIME=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
          
          if [ -f README.md ]; then'''

new_text = '''SYNC_TIME=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
          git pull --rebase --autostash origin main
          
          if [ -f README.md ]; then'''

if old_text in content:
    content = content.replace(old_text, new_text)
    print('Found and replaced with exact match!')
else:
    print('Exact match not found, trying alternative...')
    # Try without the extra spaces
    old_text2 = 'SYNC_TIME=$(date -u +"%Y-%m-%d %H:%M:%S UTC")'
    idx = content.find(old_text2)
    if idx != -1:
        end_idx = content.find('if [ -f README.md ]', idx)
        if end_idx != -1:
            # Find the line with SYNC_TIME and insert after it
            lines_before = content[:idx + len(old_text2)]
            lines_after = content[idx + len(old_text2):]
            content = lines_before + '\n          git pull --rebase --autostash origin main' + lines_after
            print('Replaced using insert method!')
        else:
            print('Could not find README.md check after SYNC_TIME')
    else:
        print('Could not find SYNC_TIME line')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('File updated successfully!')
