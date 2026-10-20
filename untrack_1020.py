import subprocess

REPO = '/Users/leonliang/maoquanqingbao'
out = subprocess.run(['git', 'ls-files', '.cache1020_1808'], cwd=REPO, capture_output=True, text=True)
files = [f for f in out.stdout.splitlines() if f.strip()]
print('tracked cache files:', len(files))
if files:
    subprocess.run(['git', 'update-index', '--force-remove'] + files, cwd=REPO, check=True)
print('done')
