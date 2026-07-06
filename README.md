# 🔭 AI 코딩 세팅 가이드 — 줌 렌즈 3층

AI 코딩 에이전트(Claude Code, Codex 등)를 **세팅 없이 날것으로** 쓰고 있다면, 이 저장소가 선물입니다.

하네스는 이미 완성품입니다. 세팅이란 거기에 "나"를 가르치는 일 —
그리고 그 세팅은 **딱 3층**이면 됩니다.

| 렌즈 | 층 | 위치 | 두는 것 |
|---|---|---|---|
| 🔭 광각 | 글로벌 | `~/.claude/` | 모든 프로젝트에 통하는 규칙·범용 스킬 |
| 🎯 표준 | 프로젝트 | `프로젝트/.claude/` | 이 프로젝트의 규칙·맞춤 스킬·MCP |
| 🔬 매크로 | 폴더 | 폴더 안 `CLAUDE.md` | 공들이는 폴더에만 얹는 집중 규칙 |

## 시작하기 (3단계)

1. **읽기** — 가이드 본문: **[imtylerrrrrr.github.io/harness-setup-gift](https://imtylerrrrrr.github.io/harness-setup-gift/)** (클릭하면 끝)
2. **구경** — [`examples/`](examples/)에서 3층 세팅의 실제 파일 모양을 봅니다.
3. **따라 하기** — [`exercises/01-글로벌-깔기.md`](exercises/01-글로벌-깔기.md)부터. 첫 층은 5분이면 깔립니다.

## 무엇이 들어있나

```
index.html      가이드 본문 (10개 섹션, 브라우저로 열기)
examples/       3층 세팅 스캐폴드 — 열어보는 실물 예시
  1-global/       🔭 ~/.claude 에 넣을 것
  2-project/      🎯 작은 파이썬 프로젝트 + .claude + .mcp.json
    3-folder/     🔬 폴더 전용 규칙
exercises/      따라 하기 3편 (글로벌 → 스킬 → MCP)
```

## 이 저장소의 한 문장

> 가장 좋은 초기 세팅은, 최소한의 세팅입니다.
> CLAUDE.md 한 장에서 시작해서, 부족함을 느낀 다음에 하나씩 얹으세요.

## 참고 자료

- [Claude Code 공식 문서](https://code.claude.com/docs)
- [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — 가이드 4번 섹션의 그 플러그인
- [Unity MCP 시작하기](https://unity.com/blog/unity-ai-mcp-how-to-get-started) — 게임 프로젝트용
