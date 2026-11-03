#!/usr/bin/env python3
"""One-off site hygiene fixer for the カハール株式会社 (GitHub Pages) site.

Applies, across all HTML files:
  - Replace dead Universal Analytics (analytics.js, placeholder id) with GA4 gtag.js
  - Remove the dead Google Maps JS include (no #map_canvas exists; only leaks the API key)
  - Fix ClaPat template leftovers (logo alt / author meta)
  - Move <meta charset> to be the first thing in <head>

Per real page:
  - Unique <title> and <meta name="description">
  - canonical + Open Graph + Twitter Card tags
  - Organization JSON-LD on the homepage

Demo/template pages get noindex instead of OG tags.
"""
import re
import pathlib

HTML_DIR = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://cahalinc.github.io/"
COMPANY = "カハール株式会社"
GA4_ID = "G-XXXXXXXXXX"  # TODO: replace with the real GA4 Measurement ID

OLD_GA = """	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script>
		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
		(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
		m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
		})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

		ga('create', 'code_here', 'auto');
		ga('send', 'pageview');
	</script>"""

NEW_GA = f"""	<!-- Google tag (gtag.js) -->
	<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag(){{dataLayer.push(arguments);}}
		gtag('js', new Date());
		gtag('config', '{GA4_ID}');
	</script>"""

DEFAULT_DESC = ("カハール株式会社は、ICML 2017 Biology Workshop 以降、biology と AI の研究を継続。"
                "Lab-in-the-loop により治療用抗体設計などの AI for Science 研究を進める研究開発会社です。")

# filename -> (canonical_url, title, description, og_image_relpath)
PAGES = {
    "index.html": (BASE, "カハール株式会社｜Lab-in-the-loop・AI for Science", DEFAULT_DESC, "images/01hero.jpg"),
    "index-showcase-grid.html": (BASE + "index-showcase-grid.html", "研究テーマ｜カハール株式会社",
        "Lab-in-the-loop・生成ML・多タスク性質予測・能動学習・in vitro 実験・構造生物学。カハール株式会社の研究テーマ一覧です。", "images/01hero.jpg"),
    "index-showcase-gallery.html": (BASE + "index-showcase-gallery.html", "研究テーマ（ギャラリー）｜カハール株式会社",
        "Lab-in-the-loop・生成ML・多タスク性質予測・能動学習・in vitro 実験・構造生物学。カハール株式会社の研究テーマをギャラリー形式で紹介します。", "images/01hero.jpg"),
    "about.html": (BASE + "about.html", "会社概要｜カハール株式会社", DEFAULT_DESC, "images/about.jpg"),
    "contact.html": (BASE + "contact.html", "お問い合わせ｜カハール株式会社",
        "共同研究・技術相談・抗体設計への AI 導入のご相談は、カハール株式会社までお気軽にお問い合わせください。", "images/01hero.jpg"),
    "project01.html": (BASE + "project01.html", "Lab-in-the-loop｜カハール株式会社",
        "生成モデル・性質予測・能動学習・in vitro 実験を統合した反復最適化ループ（Lab-in-the-loop）による抗体最適化。", "images/01hero.jpg"),
    "project02.html": (BASE + "project02.html", "Property Predictors（多タスク性質予測）｜カハール株式会社",
        "結合親和性など複数物性を同時に予測する多タスク性質予測モデルで、抗体設計の判断材料を提供します。", "images/02hero.jpg"),
    "project03.html": (BASE + "project03.html", "Generative ML（生成モデルによる抗体設計）｜カハール株式会社",
        "生成機械学習により配列空間の高コストな探索を効率化し、有望な抗体バリアントを設計します。", "images/03hero.jpg"),
    "project04.html": (BASE + "project04.html", "Active Learning（能動学習による選抜）｜カハール株式会社",
        "能動学習によるランキングと選抜で、次に実験すべき設計候補をデータに基づいて選定します。", "images/04hero.jpg"),
    "project05.html": (BASE + "project05.html", "In Vitro Loop（実験とデータ統合）｜カハール株式会社",
        "選抜した設計を in vitro でアッセイし、得られた実験データを最適化ループへ統合します。", "images/05hero.jpg"),
    "project06.html": (BASE + "project06.html", "Structural Biology（構造生物学）｜カハール株式会社",
        "結晶構造解析により、変異が抗体機能に与える影響の機構的洞察を得ます。", "images/06hero.jpg"),
}

DEMO_PAGES = ["typography.html", "multimedia.html", "shortcodes.html"]


def build_seo(canonical, title, desc, img):
    img_abs = BASE + img
    esc = lambda s: s.replace("&", "&amp;").replace('"', "&quot;")
    return f"""    <link rel="canonical" href="{canonical}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{COMPANY}">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{img_abs}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="{img_abs}">
"""

ORG_JSONLD = f"""    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "{COMPANY}",
      "url": "{BASE}",
      "logo": "{BASE}images/logo.png",
      "email": "keiohigh2nd@gmail.com",
      "telephone": "+81-90-7842-9642",
      "description": "{DEFAULT_DESC}",
      "address": {{
        "@type": "PostalAddress",
        "postalCode": "105-0001",
        "addressRegion": "東京都",
        "addressLocality": "港区",
        "streetAddress": "虎ノ門4-1-1 東京ワールドゲート 23F",
        "addressCountry": "JP"
      }}
    }}
    </script>
"""


def process(path: pathlib.Path):
    txt = path.read_text(encoding="utf-8")
    orig = txt
    name = path.name

    # 1. GA: UA -> GA4
    if OLD_GA in txt:
        txt = txt.replace(OLD_GA, NEW_GA)
    else:
        print(f"  ! GA block not found verbatim in {name}")

    # 2. Remove dead Google Maps include (whole line)
    txt = re.sub(r'[ \t]*<script src="https://maps\.googleapis\.com/maps/api/js[^"]*"></script>\n', "", txt)

    # 3. ClaPat leftovers
    txt = txt.replace('alt="ClaPat Logo"', f'alt="{COMPANY}"')
    txt = txt.replace('content="ClaPat Studio"', f'content="{COMPANY}"')

    # 4. charset first in <head>
    txt = re.sub(r'[ \t]*<meta charset="UTF-8" />[ \t]*\n', "", txt, count=1)
    txt = txt.replace("<head>\n", '<head>\n    <meta charset="UTF-8" />\n', 1)

    if name in PAGES:
        canonical, title, desc, img = PAGES[name]
        # unique title (generic ones are literally <title>カハール株式会社</title>)
        txt = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", txt, count=1, flags=re.S)
        # unique description
        txt = re.sub(r'<meta name="description" content=".*?">',
                     f'<meta name="description" content="{desc}">', txt, count=1, flags=re.S)
        # inject SEO block + JSON-LD (index) before </head>
        block = build_seo(canonical, title, desc, img)
        if name == "index.html":
            block += ORG_JSONLD
        txt = txt.replace("</head>", block + "</head>", 1)
    elif name in DEMO_PAGES:
        # keep template demo pages out of the index
        if "noindex" not in txt:
            txt = txt.replace("</head>", '    <meta name="robots" content="noindex, follow">\n</head>', 1)

    if txt != orig:
        path.write_text(txt, encoding="utf-8")
        print(f"  updated {name}")
    else:
        print(f"  no change {name}")


def main():
    for p in sorted(HTML_DIR.glob("*.html")):
        print(p.name)
        process(p)


if __name__ == "__main__":
    main()
