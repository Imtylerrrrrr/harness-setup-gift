# 실습 03 — 🔌 MCP 하나 붙여보기 (여유 있을 때)

> 목표: 내 프로젝트에 맞는 MCP를 **딱 하나만** 연결한다.

## 왜

MCP는 AI를 바깥 도구와 연결하는 표준 규격입니다.
예를 들어 문서 MCP를 붙이면, AI가 학습 시점 이후에 바뀐 라이브러리 문법도
최신 문서를 찾아보고 씁니다.

⚠️ 시작 전에 — 황금률을 기억하세요. **부족함을 느낀 다음에 하나씩.**
"있으면 좋을 것 같은" MCP를 수집하는 실습이 아닙니다.

## 0. 하나만 고르기

| 내 프로젝트 | 추천 | 하는 일 |
|---|---|---|
| 웹앱 / 파이썬 / AI | **context7** | 라이브러리 최신 문서를 AI가 검색 |
| 게임 (Unity) | **Unity MCP** | AI가 Unity 에디터의 씬·에셋·스크립트를 직접 조작 |

## 따라 하기 — context7 (웹/파이썬/AI)

프로젝트 폴더 맨 위에 `.mcp.json` 파일을 만들면 끝입니다.
`examples/2-project/.mcp.json` 에 실물이 있으니, AI에게 이렇게 시킵니다.

```
내 프로젝트 루트에 .mcp.json 만들어줘. context7 MCP 하나만 연결.
```

또는 직접 만들어도 됩니다:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

> 참고: context7은 Node.js가 설치되어 있어야 돌아갑니다. 없다면 AI에게 "Node.js 설치 도와줘"부터.

## 따라 하기 — Unity MCP (게임)

Unity는 에디터 쪽에서 설정하는 방식이 표준입니다. 두 가지 중 하나:

1. **Unity 공식 MCP 서버** — Unity 에디터의 MCP 설정 페이지 → Integrations → 내 클라이언트(Claude Code 등) 선택 → Configure. ([unity.com/blog/unity-ai-mcp-how-to-get-started](https://unity.com/blog/unity-ai-mcp-how-to-get-started))
2. **커뮤니티판 (CoplayDev/unity-mcp)** — Package Manager → Add from git URL 로 설치 후, Window → MCP for Unity → Configure All Detected Clients. ([github.com/CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp))

연결되면 "씬에 큐브 하나 만들어줘" 같은 요청이 에디터에서 실제로 일어납니다.

## 확인하기

1. 프로젝트 폴더에서 Claude Code를 **다시 시작**합니다.
2. `/mcp` 를 입력해 연결 상태가 뜨는지 확인합니다.
3. 실제로 써봅니다.
   - context7: "context7으로 (내가 쓰는 라이브러리) 최신 사용법 찾아서 알려줘"
   - Unity: "씬에 큐브 하나 추가해줘"

## 잘 안 되면

- `/mcp` 에 안 뜨면 → `.mcp.json`이 프로젝트 **맨 위 폴더**에 있는지, JSON에 오타(쉼표!)가 없는지 확인.
- 처음 연결 시 "이 MCP를 신뢰하냐"고 물어보면 내용 확인 후 승인.
- 느리거나 자주 끊기면 → 외부 도구라 원래 그럴 수 있습니다. 그 MCP가 꼭 필요한지부터 다시 생각해보세요.
