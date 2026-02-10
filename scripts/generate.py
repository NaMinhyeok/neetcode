"""NeetCode 150 문제 생성 스크립트.

GitHub의 .problemSiteData.json에서 문제 목록을 가져오고,
LeetCode GraphQL API에서 상세 정보를 조회하여
README.md + solution.py를 생성한다.
"""

import json
import re
import time
from pathlib import Path

import jinja2
import requests
from markdownify import markdownify

# ── 경로 설정 ──────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
CACHE_DIR = ROOT / ".cache"
TEMPLATES_DIR = ROOT / "templates"

# ── API URL ────────────────────────────────────────────────
NEETCODE_DATA_URL = (
    "https://raw.githubusercontent.com/neetcode-gh/leetcode"
    "/main/.problemSiteData.json"
)
LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

PROBLEM_QUERY = """
query selectProblem($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        content
        isPaidOnly
        difficulty
        hints
        topicTags { name slug }
        codeSnippets { lang langSlug code }
        exampleTestcases
    }
}
"""

# ── 카테고리 → 폴더명 매핑 (표시 순서 유지) ────────────────
CATEGORY_SLUG = {
    "Arrays & Hashing": "arrays-and-hashing",
    "Two Pointers": "two-pointers",
    "Sliding Window": "sliding-window",
    "Stack": "stack",
    "Binary Search": "binary-search",
    "Linked List": "linked-list",
    "Trees": "trees",
    "Tries": "tries",
    "Heap / Priority Queue": "heap-priority-queue",
    "Backtracking": "backtracking",
    "Graphs": "graphs",
    "Advanced Graphs": "advanced-graphs",
    "1-D Dynamic Programming": "1d-dynamic-programming",
    "2-D Dynamic Programming": "2d-dynamic-programming",
    "Greedy": "greedy",
    "Intervals": "intervals",
    "Math & Geometry": "math-and-geometry",
    "Bit Manipulation": "bit-manipulation",
}

# ── HTTP 세션 ──────────────────────────────────────────────
session = requests.Session()
session.headers.update({
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
})


# ── 캐싱 유틸 ─────────────────────────────────────────────
def _cache_path(slug: str) -> Path:
    return CACHE_DIR / f"{slug}.json"


def _load_cache(slug: str) -> dict | None:
    path = _cache_path(slug)
    if path.exists():
        return json.loads(path.read_text())
    return None


def _save_cache(slug: str, data: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    _cache_path(slug).write_text(json.dumps(data, ensure_ascii=False, indent=2))


# ── 1) NeetCode 150 문제 목록 가져오기 ───────────────────
def fetch_neetcode150() -> list[dict]:
    """GitHub에서 .problemSiteData.json을 가져와 NeetCode 150만 필터링."""
    cache = _load_cache("_problemSiteData")
    if cache:
        data = cache
    else:
        resp = session.get(NEETCODE_DATA_URL, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        _save_cache("_problemSiteData", data)

    return [p for p in data if p.get("neetcode150")]


# ── 2) LeetCode 문제 상세 조회 (GraphQL) ─────────────────
def fetch_problem_detail(slug: str, retries: int = 3) -> dict | None:
    """LeetCode GraphQL API에서 문제 상세 정보를 조회. 캐싱 + 재시도."""
    cached = _load_cache(slug)
    if cached:
        return cached

    for attempt in range(retries):
        try:
            resp = session.post(
                LEETCODE_GRAPHQL_URL,
                json={
                    "query": PROBLEM_QUERY,
                    "variables": {"titleSlug": slug},
                },
                timeout=30,
            )
            if resp.status_code == 429:
                wait = 2 ** (attempt + 2)
                print(f"  ⏳ Rate limited, waiting {wait}s...", flush=True)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            data = resp.json().get("data", {}).get("question")
            if data:
                _save_cache(slug, data)
                return data
        except (requests.RequestException, json.JSONDecodeError) as e:
            wait = 2 ** (attempt + 1)
            print(f"  ⚠️  Attempt {attempt + 1}/{retries} failed: {e}", flush=True)
            if attempt < retries - 1:
                time.sleep(wait)

    print(f"  ❌ Failed to fetch: {slug}", flush=True)
    return None


# ── 3) HTML → Markdown 변환 ───────────────────────────────
def html_to_markdown(html: str) -> str:
    """LeetCode HTML을 깔끔한 Markdown으로 변환."""
    # 빈 단락 제거
    html = re.sub(r"<p>&nbsp;</p>", "", html)
    md = markdownify(html, heading_style="ATX", bullets="-")
    # 연속 빈 줄 정리
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


# ── 4) Python3 함수 시그니처 추출 ─────────────────────────
def extract_python3_snippet(detail: dict) -> str:
    """codeSnippets에서 Python3 코드를 추출."""
    for snippet in detail.get("codeSnippets") or []:
        if snippet.get("langSlug") == "python3":
            return snippet["code"]
    return "# No Python3 snippet available\npass"


# ── 5) NeetCode slug 변환 ─────────────────────────────────
def to_neetcode_slug(link: str) -> str:
    """'contains-duplicate/' → 'contains-duplicate'"""
    return link.strip("/")


def to_leetcode_slug(link: str) -> str:
    """'contains-duplicate/' → 'contains-duplicate'"""
    return link.strip("/")


# ── 6) 문제 번호 추출 ────────────────────────────────────
def extract_number(code: str) -> str:
    """'0217-contains-duplicate' → '217'"""
    match = re.match(r"^0*(\d+)", code)
    return match.group(1) if match else "0"


# ── 메인 생성 로직 ────────────────────────────────────────
def generate_all() -> None:
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_DIR),
        keep_trailing_newline=True,
    )
    problem_tmpl = env.get_template("problem.md.j2")
    solution_tmpl = env.get_template("solution.py.j2")

    problems = fetch_neetcode150()
    print(f"📋 NeetCode 150 문제 {len(problems)}개 로드", flush=True)

    created = 0
    skipped = 0
    failed = 0

    for i, prob in enumerate(problems, 1):
        category = prob["pattern"]
        cat_slug = CATEGORY_SLUG.get(category, category.lower().replace(" ", "-"))
        code = prob["code"]  # e.g. "0217-contains-duplicate"
        number = extract_number(code)
        leetcode_slug = to_leetcode_slug(prob["link"])
        neetcode_slug = to_neetcode_slug(prob["link"])

        problem_dir = PROBLEMS_DIR / cat_slug / code
        readme_path = problem_dir / "README.md"
        solution_path = problem_dir / "solution.py"

        # 이미 존재하면 스킵
        if readme_path.exists() and solution_path.exists():
            skipped += 1
            continue

        print(f"[{i}/{len(problems)}] {prob['problem']} ({category})", flush=True)

        # API 호출
        detail = fetch_problem_detail(leetcode_slug)
        if not detail:
            failed += 1
            continue

        # isPaidOnly 체크
        is_premium = detail.get("isPaidOnly", False)
        if is_premium:
            description = (
                f"*이 문제는 LeetCode Premium 문제입니다.*\n\n"
                f"[LeetCode에서 보기](https://leetcode.com/problems/{leetcode_slug}/)"
            )
        else:
            raw_html = detail.get("content") or ""
            description = html_to_markdown(raw_html) if raw_html else "문제 설명을 가져올 수 없습니다."

        # 힌트
        hints = detail.get("hints") or []

        # 토픽 태그
        topic_tags = detail.get("topicTags") or []
        topics = [t["name"] for t in topic_tags if isinstance(t, dict)]

        # YouTube URL
        video_id = prob.get("video", "")
        youtube_url = f"https://www.youtube.com/watch?v={video_id}" if video_id else ""

        # 함수 시그니처
        code_snippet = extract_python3_snippet(detail)

        # 템플릿 컨텍스트
        ctx = {
            "number": number,
            "title": prob["problem"],
            "difficulty": prob["difficulty"],
            "category": category,
            "neetcode_slug": neetcode_slug,
            "leetcode_slug": leetcode_slug,
            "youtube_url": youtube_url,
            "topics": topics,
            "description": description,
            "hints": hints,
            "code_snippet": code_snippet,
        }

        # 파일 생성
        problem_dir.mkdir(parents=True, exist_ok=True)

        if not readme_path.exists():
            readme_path.write_text(problem_tmpl.render(ctx))

        if not solution_path.exists():
            solution_path.write_text(solution_tmpl.render(ctx))

        created += 1

        # API rate limit 배려
        time.sleep(1)

    print(f"\n✅ 완료: 생성 {created}, 스킵 {skipped}, 실패 {failed}", flush=True)


if __name__ == "__main__":
    generate_all()
