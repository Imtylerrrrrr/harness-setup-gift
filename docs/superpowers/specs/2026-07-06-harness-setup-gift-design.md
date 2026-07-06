# harness-setup-gift 설계 스펙

날짜: 2026-07-06
상태: 승인 대기

## 1. 목적과 대상

고등학교 소프트웨어반 학생들에게 주는 "AI 코딩 세팅" 입문 자료.
학생들은 AI를 이미 많이 쓰지만 스킬·플러그인·MCP 세팅 없이 날것으로 쓴다.
이 자료의 목표는 **코딩 워크플로우(메커니즘)를 한 단계 끌어올리는 것**.

- 핵심 메시지: AI는 이미 잘 쓰고 있다 → 세팅을 하면 한 단계 더 올라간다.
- 학생 특성: 터미널에 익숙하지 않음 → 슬래시 명령(`/plugin` 등) 위주로 진입장벽 최소화.
- 프로젝트 성향: 웹앱, 파이썬, 게임, AI 등 다양 → 범용 뼈대 + 도메인별 카드 방식.
- 분량 정책: "입시생이니까 줄이기" 없음. 개발자 꿈나무 기준 적당량을 제대로 담는다.
- 배포: GitHub 공개 레포. 학생은 링크로 HTML을 읽거나 clone해서 예제를 본다.

## 2. 말투와 톤

- 서술체: `~입니다 / ~다`. 개인적 관계(형·선생님 등)는 담지 않는다.
- 레퍼런스 문서(`2026-06-09-claude-code-architecture.html`, AICONLAB)의 화법을 따른다:
  비유 중심, "쉬운 말" 주석(`easy` 박스), 섹션당 한 화면, 한 줄 요약 카드.
- 2인칭 후킹("너는 이미 ~") 금지. 담담한 궁금증 유발형 헤드라인.

## 3. 중심 컨셉

**줌 렌즈 비유** — 세팅은 렌즈를 갈아끼우는 것.

| 렌즈 | 층 | 위치 | 색 |
|---|---|---|---|
| 🔭 광각 | 글로벌 | `~/.claude/` | 파스텔 하늘 |
| 🎯 표준 | 프로젝트 | `프로젝트/.claude/` | 파스텔 민트 |
| 🔬 매크로 | 폴더 | 프로젝트 안 하위 폴더 | 파스텔 라벤더 |

내려갈수록 좁고 깊게. 더 구체적인 층이 우선한다.

## 4. 레포 구조

```
harness-setup-gift/
├── index.html                       설명 문서 (10섹션)
├── README.md                        소개 + 3줄 시작법
├── docs/superpowers/specs/          설계 문서 (이 파일)
├── examples/
│   ├── 1-global/                    🔭 ~/.claude 에 넣을 예시
│   │   ├── CLAUDE.md                Karpathy 4원칙 스타일 범용 규칙
│   │   └── skills/make-doc/SKILL.md 범용 '문서 만들기' 스킬
│   └── 2-project/                   🎯 작은 파이썬 미니 프로젝트: "단어장 퀴즈"
│       ├── main.py                  퀴즈 실행 (50줄 내외)
│       ├── words.py                 단어 데이터
│       ├── .claude/
│       │   ├── CLAUDE.md            프로젝트 전용 규칙
│       │   └── skills/add-quiz-set/SKILL.md  "새 단어 세트 추가" 절차 스킬
│       ├── .mcp.json                MCP 연결 예시 (주석으로 친절히)
│       └── 3-folder/                🔬 공들이는 폴더 집중 세팅
│           └── CLAUDE.md            이 폴더만의 더 좁은 규칙
└── exercises/
    ├── 01-글로벌-깔기.md            Karpathy 플러그인 /plugin 설치
    ├── 02-내-스킬-만들기.md         SKILL.md 직접 작성
    └── 03-MCP-붙여보기.md           .mcp.json 로 MCP 연결
```

- 도메인 카드(웹/게임/AI)는 별도 파일이 아니라 index.html 5번 섹션 안의 시각 카드.

## 5. index.html — 10섹션 목차

| # | 섹션 | 내용 |
|---|---|---|
| 0 | 표지 | 담담한 헤드라인 + "AI 세팅이란 게 있다" 한 줄 |
| 1 | 하네스가 뭔지 | AI에 손발 다는 것 = 하네스. 짧은 개념 소개 |
| 2 | 세팅 = 렌즈 갈아끼우기 | 줌 렌즈 비유 도입, 중심 SVG 다이어그램 |
| 3 | 재료 4개 | Skills·Plugins·MCP·Hooks 각 한 줄 (지식이냐 행동이냐) |
| 4 | 🔭 광각 = 글로벌 | `~/.claude`. Karpathy skills 플러그인 설치 시연 (`/plugin marketplace add forrestchang/andrej-karpathy-skills` → `/plugin install`) — 중요 예시 |
| 5 | 🎯 표준 = 프로젝트 | `프로젝트/.claude` + 공식 마켓플레이스(`/plugin` Discover 탭) + MCP. 도메인 카드: 웹/파이썬/게임(Unity MCP는 가벼운 예시)/AI |
| 6 | 🔬 매크로 = 폴더 | 공들이는 부분만 집중 세팅. 가벼운 톤 |
| 7 | 딱 3가지만 조심 | 함정 + 황금률("가장 단순한 것부터") |
| 8 | 오늘 이것부터 | 마무리 한 문장 + exercises/ 연결 |
| 9 | 더 궁금하면 | 심화 포인터: **loop 엔지니어링**(Boris Cherny "이제 프롬프트 대신 루프를 쓴다", Addy Osmani 명명, 2026.6) 등 |

## 6. 디자인

- 밝은 파스텔톤: 크림/화이트 배경 + 민트·라벤더·하늘·버터옐로·살구핑크 포인트.
- 폰트: 제목 Gaegu, 본문 Gowun Dodum + Pretendard (레퍼런스와 동일 계열).
- 레이아웃: 좌측 고정 TOC 사이드바 + 섹션 스크롤 (레퍼런스와 동일 골격).
- SVG 다이어그램: 최소 2개 (줌 렌즈 3층, 3층 우선순위/오버라이드).
- 모바일 대응: 860px 이하에서 사이드바 숨김.

## 7. 콘텐츠 소스 (2026-07-06 리서치 확정)

- **Karpathy plugin**: `multica-ai/andrej-karpathy-skills` (Forrest Chang 작성, Karpathy 2026-01-26 X 포스트 기반).
  4원칙: Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution.
  설치: `/plugin marketplace add forrestchang/andrej-karpathy-skills` → `/plugin install andrej-karpathy-skills@karpathy-skills`.
  주의 표기: Karpathy 본인이 만든 것 아님(영감만).
- **공식 마켓플레이스**: `claude-plugins-official`은 Claude Code에 기본 내장. `/plugin` → Discover 탭.
- **Unity MCP**: Unity 공식 MCP 서버(에디터 내 Integrations 자동 설정) 또는 CoplayDev/unity-mcp. `.mcp.json` 예시로만 가볍게.
- **Loop 엔지니어링**: 2026-06 등장. Boris Cherny(WorkOS Acquired Unplugged, 2026-06-02) "루프가 Claude에 프롬프트한다, 내 일은 루프를 쓰는 것". Addy Osmani가 "loop engineering" 명명(6요소: automations·worktrees·skills·connectors·sub-agents·memory).

## 8. 실습 (exercises/) 설계

각 실습은 "왜 → 따라 하기 → 확인하기" 3부 구조. 터미널 최소화, 슬래시 명령 우선.

1. **01-글로벌-깔기**: Karpathy 플러그인 설치 + `~/.claude/CLAUDE.md`에 한 줄 추가해보기. 확인: 아무 프로젝트에서 Claude가 규칙을 따르는지.
2. **02-내-스킬-만들기**: examples의 SKILL.md를 복사해 자기 반복작업 하나를 스킬로. 확인: 해당 작업 시 스킬이 발동하는지.
3. **03-MCP-붙여보기**: `.mcp.json`으로 MCP 하나 연결(도메인별 선택지 제공: 웹→context7 등 문서 MCP, 게임→Unity MCP, 파이썬/AI→적절한 예). 확인: `/mcp`로 연결 상태.

## 9. 성공 기준

- [ ] 학생이 HTML만 읽고 3층 구조("어디에 뭘 두는지")를 설명할 수 있다.
- [ ] exercises 01을 따라 하면 실제로 Karpathy 플러그인이 글로벌에 깔린다.
- [ ] examples를 clone하면 3층 세팅의 실제 파일 모양을 그대로 볼 수 있다.
- [ ] 모든 명령이 2026-07 기준 실제로 동작한다 (설치 명령·경로 검증).
- [ ] 개인적 관계 표현 0건, `~입니다/~다` 서술체 일관.

## 10. 범위 밖 (안 하는 것)

- 해커톤 관련 내용 (별도 전달 예정)
- Hooks 심화, 서브에이전트 심화 (9번 섹션 포인터로만)
- 게임엔진 MCP 심화 (Unity MCP는 예시 카드 1장)
- 배포 자동화, CI 등
