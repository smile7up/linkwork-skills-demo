# linkwork-skills-demo

演示用 Skill 仓库，供 AI 机器人平台 (general-agent) 的 GitHub Skill Provider 读写。

## 目录结构

```
skills/
├── README.md
├── python-data-analysis/    # 数据分析 Skill
│   ├── SKILL.md
│   └── analyze.py
└── document-generation/     # 文档生成 Skill
    ├── SKILL.md
    └── template.md
```

每个 Skill 是 `skills/` 下的一个目录，含一份 `SKILL.md`（描述、调用方式）和若干随附资源。

## 与平台后端的交互

- `listSkills()` → `GET /repos/smile7up/linkwork-skills-demo/contents/skills`
- `getTree(skillName)` → `GET /repos/.../git/trees/main?recursive=1`
- `upsertFile(skillName, path, content, msg)` → `PUT /repos/.../contents/skills/{skillName}/{path}`
- `deleteFile(skillName, path, msg)` → `DELETE /repos/.../contents/skills/{skillName}/{path}`
- `listCommits(skillName, page, size)` → `GET /repos/.../commits?path=skills/{skillName}`

所有写操作走 main 分支，commit 作者默认是 PAT 所有者。
