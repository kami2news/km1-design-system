#!/usr/bin/env python3
"""保留・提案・試行の期限切れを見つける / Find overdue holds, proposals and trials (KM1-GOV-002).

governance.md の 2 章（判断の記録）で状態が「提案」「保留」「試行」の項目が、6 章（期限）に載っているか、
次の確認日を過ぎていないかを調べる。FAIL があれば終了コード 1。
Checks that every decision whose state is proposed, on hold or trial appears in chapter 6 with a next review date,
and that the date has not passed. Exits with 1 on any FAIL.

usage: govcheck.py [project dir] [--today YYYY-MM-DD]
"""
import os, re, sys, datetime

args = [a for a in sys.argv[1:] if not a.startswith('--')]
today = datetime.date.today()
if '--today' in sys.argv:
    today = datetime.date.fromisoformat(sys.argv[sys.argv.index('--today') + 1])
    args = [a for a in args if a != sys.argv[sys.argv.index('--today') + 1]]
_H = os.path.dirname(os.path.abspath(__file__))
P = args[0] if args else os.environ.get('KM1_PROJECT') or (
    os.path.join(_H, '..', 'project') if os.path.exists(os.path.join(_H, '..', 'project', 'governance.md')) else os.path.join(_H, '..'))
text = open(os.path.join(P, 'governance.md'), encoding='utf-8').read()

OPEN = ('提案', '保留', '試行')
log, due = {}, {}
section = None
for line in text.splitlines():
    m = re.match(r'^## (\d+)\.', line)
    if m:
        section = int(m.group(1))
        continue
    if not line.startswith('|'):
        continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if not cells or not re.fullmatch(r'D\d+', cells[0]):
        continue
    if section == 2 and len(cells) >= 3:
        log[cells[0]] = cells[2]
    elif section == 6 and len(cells) >= 3:
        due[cells[0]] = cells[2]

bad, warn = [], []
for d, state in sorted(log.items(), key=lambda kv: int(kv[0][1:])):
    if not state.startswith(OPEN):
        continue
    if d not in due:
        bad.append(f'{d}: 状態が「{state}」なのに、6 章に次の確認日がない / open decision without a review date')
        continue
    try:
        when = datetime.date.fromisoformat(due[d])
    except ValueError:
        bad.append(f'{d}: 次の確認日が YYYY-MM-DD でない（{due[d]}） / bad date')
        continue
    if when < today:
        bad.append(f'{d}: 確認日 {when} を過ぎている（{(today - when).days} 日） / overdue')
    elif (when - today).days <= 7:
        warn.append(f'{d}: 確認日 {when} まで {(when - today).days} 日 / due within a week')
for d in sorted(due):
    if d not in log:
        bad.append(f'{d}: 6 章にあるが 2 章に載っていない / listed in ch. 6 but not in the log')
    elif not log[d].startswith(OPEN):
        warn.append(f'{d}: 状態が「{log[d]}」に変わった。6 章から外せる / no longer open; remove from ch. 6')

for w in warn:
    print('WARN', w)
for b in bad:
    print('FAIL', b)
open_n = sum(1 for s in log.values() if s.startswith(OPEN))
print(f'  --- 開いている判断 {open_n} / FAIL {len(bad)} / WARN {len(warn)}  （基準日 {today}）')
sys.exit(1 if bad else 0)
