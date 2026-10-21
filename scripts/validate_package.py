#!/usr/bin/env python3
"""Offline, stdlib-only structural linter for the AI Development Team marketplace.
Use `claude plugin validate` separately for native Claude Code validation.
"""
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'plugins'/'ai-development-team'
EXPECTED={'coordinator','architect','security','data','business-logic','frontend',
          'admin-console','platform-ops','integration-release','qa-testing'}
NEEDED_SKILLS={'core-standards','start-project','implement-change','release-check',
              'incident-triage','agent-status'}
errors=[]
def chk(c,msg):
    if not c: errors.append(msg)
def j(path):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{path}: {e}'); return {}
market=j(ROOT/'.claude-plugin'/'marketplace.json')
manifest=j(P/'.claude-plugin'/'plugin.json')
chk(market.get('name')=='ai-team-marketplace','marketplace name mismatch')
chk(manifest.get('name')=='ai-development-team','plugin name mismatch')
chk(('version' not in manifest) or bool(re.fullmatch(r'\d+\.\d+\.\d+',str(manifest['version']))), 'invalid optional manifest version')
plugins=market.get('plugins',[])
chk(len(plugins)==1 and plugins[0].get('source')=='./plugins/ai-development-team','bad plugin path')
files=list((P/'agents').glob('*.md'))
chk({f.stem for f in files}==EXPECTED,'agent filename roster mismatch')
for f in files:
    t=f.read_text(encoding='utf-8')
    m=re.match(r'^---\n(.+?)\n---\n(.+)$',t,re.S)
    chk(bool(m),f'{f.name}: missing YAML frontmatter and body')
    if not m: continue
    fm=m.group(1)
    for field in ('name','description','tools','model'):
        chk(re.search(rf'(?m)^{field}: .+',fm) is not None,f'{f.name}: missing {field}')
    chk(re.search(rf'(?m)^name: {re.escape(f.stem)}$',fm)!=None,f'{f.name}: name differs from filename')
    chk('skills:\n  - ai-development-team:core-standards' in fm,f'{f.name}: core standards not preloaded')
    tools_match=re.search(r'(?m)^tools: "([^"]+)"$',fm)
    toks=[x.strip() for x in tools_match.group(1).split(',')] if tools_match else []
    chk('Skill' in toks,f'{f.name}: Skill tool missing')
    chk(('Agent' in toks)==(f.stem=='coordinator'),f'{f.name}: incorrect Agent tool allocation')
    for forbidden in ('permissionMode:','mcpServers:','hooks:'):
        chk(forbidden not in fm,f'{f.name}: unsupported plugin-agent frontmatter: {forbidden}')
    for s in ('documentation','production','company','handoff'):
        chk(s in t.lower(),f'{f.name}: missing safety/handoff token {s}')
for name in NEEDED_SKILLS:
    f=P/'skills'/name/'SKILL.md'
    chk(f.is_file(),f'missing skill: {name}')
    if f.exists():
        t=f.read_text(encoding='utf-8')
        chk(t.startswith('---\n') and f'name: {name}\n' in t,f'bad skill frontmatter: {name}')
for name in ('CONSTITUTION.md','DATA-SAFETY.md','SECURITY-AND-TENANCY.md','DOCUMENTATION.md','ENGINEERING.md','CHANGE-CONTROL.md','QUALITY-GATES.md','APPLICATION-PROFILES.md'):
    chk((P/'standards'/name).is_file(),f'missing standard {name}')
chk(j(P/'hooks'/'hooks.json').get('hooks')=={},'unsafe hooks unexpectedly enabled')
chk((ROOT/'.github'/'workflows'/'plugin-validation.yml').is_file(),'missing CI validator workflow')
chk((P/'docs'/'PREPUBLICATION-REVIEW.md').is_file(),'missing audit findings')
if errors:
    for e in errors: print('FAIL',e)
    sys.exit(1)
print(f'PASS: marketplace, manifest, {len(files)} agents, {len(NEEDED_SKILLS)} skills, standards, templates and hooks structure')
print('NOTE: static checks only; run `claude plugin validate` in Claude Code locally.')
