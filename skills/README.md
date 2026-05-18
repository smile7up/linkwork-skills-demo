# Skills 目录

本目录下每个子目录是一个 Skill。Skill 名 = 子目录名。

新增 Skill 流程（自动由后端通过 GitHub API 执行）：
1. 用户在 UI Skills 工厂点「创建」
2. 后端调 `upsertFile("<name>", "SKILL.md", content, "init skill")`
3. GitHub API `PUT /repos/.../contents/skills/<name>/SKILL.md` 产生一次 commit

修改 / 删除 / 历史查询同理。
