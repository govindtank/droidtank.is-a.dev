import json
import os

def build():
    with open('/Users/govind/workspace/droidtank.is-a.dev/data_packages.json', 'r') as f:
        packages = json.load(f)

    with open('/Users/govind/workspace/droidtank.is-a.dev/data_blogs.json', 'r') as f:
        blogs = json.load(f)

    # Ensure all Kotlin CMP packages have the exact verified JitPack links
    for p in packages:
        if p['type'] == 'kotlin':
            p['pubUrl'] = f"https://jitpack.io/#govindtank/{p['name']}"

    packages_json = json.dumps(packages)
    blogs_json = json.dumps(blogs)

    core_css = """
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
      --bg: #000000;
      --card-bg: #050505;
      --border: #262626;
      --border-lit: #404040;
      --text: #ffffff;
      --text-muted: #888888;
      --text-dim: #555555;
      --green: #00ff66;
      --green-glow: rgba(0, 255, 102, 0.15);
      --red: #ef4444;
      --cyan: #38bdf8;
      --purple: #c084fc;
      --mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
      --sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      border-radius: 0px !important;
      box-shadow: none !important;
      min-width: 0;
    }

    html {
      background: #000000;
      color: #ffffff;
      scroll-behavior: smooth;
    }

    body {
      font-family: var(--sans);
      background: #000000;
      color: #ffffff;
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* Minimal Grid Background */
    .bg-grid {
      position: fixed;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 40px 40px;
      z-index: -1;
      pointer-events: none;
    }

    /* Staggered Cascade Animations */
    .reveal {
      animation: fadeUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    .delay-1 { animation-delay: 0.1s; }
    .delay-2 { animation-delay: 0.2s; }
    .delay-3 { animation-delay: 0.3s; }
    .delay-4 { animation-delay: 0.4s; }

    @keyframes fadeUp {
      0% { opacity: 0; transform: translateY(16px); }
      100% { opacity: 1; transform: translateY(0); }
    }

    .wrapper {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Headings */
    h1, h2, h3, h4 {
      font-family: var(--mono);
      font-weight: 700;
      letter-spacing: -0.5px;
      color: var(--text);
      text-transform: lowercase;
      word-break: break-word;
    }
    .display-title {
      font-size: clamp(2.4rem, 5.5vw, 4.2rem);
      line-height: 1.05;
      margin-bottom: 20px;
      letter-spacing: -1.5px;
    }
    .section-title {
      font-size: clamp(1.6rem, 3.5vw, 2.4rem);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .section-title::before {
      content: '$';
      color: var(--green);
    }

    .cursor-blink {
      display: inline-block;
      width: 12px;
      height: 1em;
      background-color: var(--green);
      vertical-align: middle;
      animation: blink 1s step-end infinite;
      margin-left: 4px;
    }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

    /* CLI Prompt Tag */
    .cli-tag {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-dim);
      margin-bottom: 14px;
      letter-spacing: 0.08em;
    }
    .cli-tag span { color: var(--green); }

    /* Neo-Brutalist Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      height: 34px;
      padding: 0 16px;
      font-family: var(--mono);
      font-size: 11.5px;
      font-weight: 600;
      text-transform: lowercase;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--text);
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
      user-select: none;
    }
    .btn:hover {
      background: var(--text);
      color: var(--bg);
      border-color: var(--text);
    }
    .btn-primary {
      background: #ffffff;
      color: #000000;
      border-color: #ffffff;
    }
    .btn-primary:hover {
      background: #e5e5e5;
    }
    .btn-green {
      background: rgba(0, 255, 102, 0.08);
      color: var(--green);
      border-color: rgba(0, 255, 102, 0.35);
    }
    .btn-green:hover {
      background: var(--green);
      color: #000000;
      border-color: var(--green);
    }
    .btn-muted {
      border-color: var(--border);
      color: var(--text-muted);
    }
    .btn-muted:hover {
      border-color: var(--border-lit);
      color: var(--text);
      background: #111111;
    }

    /* Telemetry Badge */
    .telemetry-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #000000;
      border: 1px solid var(--border);
      padding: 4px 10px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-muted);
      text-decoration: none;
    }
    .pulse-dot {
      width: 6px; height: 6px;
      border-radius: 50% !important;
      background: var(--green);
      box-shadow: 0 0 6px var(--green);
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 0.6; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    /* Nav */
    nav.site-nav {
      position: fixed;
      top: 0; left: 0; right: 0;
      background: rgba(0, 0, 0, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
      z-index: 1000;
    }
    .nav-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 24px;
      max-width: 1200px;
      margin: 0 auto;
      gap: 16px;
    }
    .nav-brand {
      font-family: var(--mono);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--text);
      text-decoration: none;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 18px;
      list-style: none;
    }
    .nav-link {
      font-family: var(--mono);
      font-size: 11.5px;
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.15s;
      letter-spacing: 0.05em;
    }
    .nav-link:hover, .nav-link.active {
      color: var(--text);
    }

    /* Sections */
    section {
      padding: 90px 0;
      border-bottom: 1px solid var(--border);
    }

    /* Package Cards */
    .pkg-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 20px;
    }
    .pkg-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .pkg-card:hover {
      border-color: var(--border-lit);
      background: #09090b;
      transform: translateY(-2px);
    }
    .pkg-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
      gap: 10px;
    }
    .pkg-name {
      font-family: var(--mono);
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text);
      text-decoration: none;
      word-break: break-word;
    }
    .pkg-name:hover { color: var(--green); }
    .badge-pill {
      font-family: var(--mono);
      font-size: 10px;
      padding: 2px 6px;
      border: 1px solid var(--border);
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      white-space: nowrap;
    }
    .badge-green {
      color: var(--green);
      border-color: rgba(0, 255, 102, 0.35);
    }
    .badge-cyan {
      color: var(--cyan);
      border-color: rgba(56, 189, 248, 0.35);
    }
    .badge-purple {
      color: var(--purple);
      border-color: rgba(192, 132, 252, 0.35);
    }

    .pkg-tagline {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--green);
      margin-bottom: 8px;
    }
    .pkg-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 16px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .pkg-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-bottom: 16px;
    }
    .chip {
      font-family: var(--mono);
      font-size: 10px;
      padding: 2px 6px;
      background: #000000;
      border: 1px solid var(--border);
      color: var(--text-dim);
    }

    .cmd-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #000000;
      border: 1px solid var(--border);
      padding: 7px 12px;
      margin-bottom: 14px;
      font-family: var(--mono);
      font-size: 11px;
    }
    .cmd-text {
      color: var(--text);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin-right: 8px;
      flex: 1;
    }
    .cmd-copy {
      background: #18181b;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 2px 8px;
      font-size: 10px;
      font-family: var(--mono);
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }
    .cmd-copy:hover {
      background: var(--text);
      color: var(--bg);
    }

    .pkg-actions {
      display: flex;
      gap: 6px;
      padding-top: 12px;
      border-top: 1px solid var(--border);
    }

    /* Article Rows */
    .art-row {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 20px;
      padding: 20px 24px;
      background: var(--card-bg);
      border: 1px solid var(--border);
      text-decoration: none;
      color: inherit;
      margin-bottom: 12px;
      transition: all 0.15s;
    }
    .art-row:hover {
      border-color: var(--border-lit);
      background: #09090b;
      transform: translateX(4px);
    }
    .art-tag-line {
      font-family: var(--mono);
      font-size: 10.5px;
      color: var(--purple);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }
    .art-title {
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--text);
      margin-bottom: 6px;
      line-height: 1.35;
    }
    .art-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.55;
      max-width: 780px;
    }
    .art-meta {
      font-family: var(--mono);
      font-size: 11.5px;
      color: var(--text-dim);
      text-align: right;
      white-space: nowrap;
    }
    .art-views-badge {
      display: inline-block;
      color: var(--green);
      font-weight: 600;
      margin-top: 4px;
    }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #000000;
      border: 1px solid var(--green);
      color: var(--green);
      padding: 8px 16px;
      font-family: var(--mono);
      font-size: 11.5px;
      z-index: 5000;
      transform: translateY(80px);
      opacity: 0;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .toast.show {
      transform: translateY(0);
      opacity: 1;
    }

    /* Footer */
    footer {
      padding: 50px 0 30px;
      background: #000000;
      font-family: var(--mono);
      font-size: 11.5px;
      color: var(--text-dim);
    }

    @media (max-width: 768px) {
      .nav-links { display: none; }
      .art-row { grid-template-columns: 1fr; }
      .art-meta { text-align: left; }
      .pkg-grid { grid-template-columns: 1fr; }
    }
    """

    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Govind Tank | Open Source Mobile Architect &amp; Systems</title>
  <meta name="description" content="Open source mobile architecture, Flutter &amp; Dart packages (140/140 score), and Kotlin Compose Multiplatform libraries by Govind Tank.">
  <meta name="google-site-verification" content="XgM7pPr1XAMYxTg37pXPzcTeW9-m0x96HRA65XtPBjM">
  <link rel="canonical" href="https://droidtank.is-a.dev/">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
  
  <!-- GoatCounter Telemetry -->
  <script data-goatcounter="https://govindtank.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>

  <style>
    __CORE_CSS__
    
    .hero {
      min-height: 88vh;
      display: flex;
      align-items: center;
      padding-top: 100px;
      padding-bottom: 50px;
    }
    .hero-layout {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 40px;
      align-items: center;
      width: 100%;
    }
    .hero-sub {
      font-size: 1.1rem;
      color: var(--text-muted);
      line-height: 1.65;
      margin-bottom: 28px;
      max-width: 580px;
    }
    .hero-sub strong {
      color: #ffffff;
      font-weight: 600;
    }

    /* Metrics Grid */
    .metrics-row {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      border: 1px solid var(--border);
      margin-top: 40px;
      background: var(--card-bg);
    }
    .metric-cell {
      padding: 18px 16px;
      border-right: 1px solid var(--border);
    }
    .metric-cell:last-child {
      border-right: none;
    }
    .metric-val {
      font-family: var(--mono);
      font-size: 1.6rem;
      font-weight: 700;
      color: #ffffff;
      line-height: 1;
      margin-bottom: 4px;
    }
    .metric-lbl {
      font-family: var(--mono);
      font-size: 10.5px;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    @media (max-width: 992px) {
      .hero-layout { grid-template-columns: 1fr; }
      .metrics-row { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 600px) {
      .metrics-row { grid-template-columns: repeat(2, 1fr); }
    }
  </style>
</head>
<body>
  <div class="bg-grid"></div>

  <!-- Top Navigation -->
  <nav class="site-nav">
    <div class="nav-inner">
      <a href="./" class="nav-brand">
        govindtank<span style="color:var(--text-dim)">/droidtank</span>
      </a>

      <ul class="nav-links">
        <li><a href="#packages" class="nav-link">packages</a></li>
        <li><a href="#author" class="nav-link">architect</a></li>
        <li><a href="#blog" class="nav-link">articles (120)</a></li>
        <li><a href="https://pub.dev/publishers/govindtank.is-a.dev/packages" target="_blank" rel="noopener" class="nav-link">publisher ↗</a></li>
        <li><a href="https://github.com/govindtank" target="_blank" rel="noopener" class="nav-link">github ↗</a></li>
      </ul>

      <!-- Real Working Live Visitor Counter -->
      <div class="telemetry-badge" title="Live Verified Visits">
        <span class="pulse-dot"></span>
        <span>VISITS: <strong id="nav-visitor-count" style="color:#fff;">--</strong></span>
      </div>
    </div>
  </nav>

  <main>
    <!-- HERO SECTION -->
    <section class="hero">
      <div class="wrapper">
        <div class="hero-layout">
          <div>
            <div class="cli-tag reveal"><span>$</span> droidtank init --publisher="govindtank.is-a.dev"</div>
            <h1 class="display-title reveal delay-1">
              the mobile &amp;<br>ai ecosystem.<span class="cursor-blink"></span>
            </h1>

            <p class="hero-sub reveal delay-2">
              <strong>one architect. every platform.</strong> 20 published open-source libraries across Flutter, Dart, Android NDK, and Kotlin Compose Multiplatform. Built for 60 FPS performance, offline AI agents, and 140/140 pub target points.
            </p>

            <div class="cmd-bar reveal delay-2" style="max-width: 440px;">
              <span class="cmd-text">$ <span id="quick-install-cmd">flutter pub add spatial_card</span></span>
              <button class="cmd-copy" onclick="copySnippet(document.getElementById('quick-install-cmd').textContent, this)">copy</button>
            </div>

            <div style="display:flex; gap:10px; flex-wrap:wrap;" class="reveal delay-3">
              <a href="#packages" class="btn btn-primary">explore 20 packages</a>
              <a href="#packages" onclick="setFilter('demos')" class="btn btn-green">view 6 live demos ↗</a>
              <a href="blog/" class="btn btn-muted">read 120 articles →</a>
              <a href="https://github.com/govindtank" target="_blank" rel="noopener" class="btn btn-muted">github profile ↗</a>
            </div>
          </div>

          <!-- ASCII System Schematic -->
          <div class="reveal delay-3">
            <div style="background:var(--card-bg); border:1px solid var(--border); padding:20px; font-family:var(--mono); font-size:11px; line-height:1.4;">
              <div style="color:var(--text-dim); border-bottom:1px solid var(--border); padding-bottom:8px; margin-bottom:12px; display:flex; justify-content:space-between;">
                <span>TOPOLOGY: DROIDTANK-CORE</span>
                <span style="color:var(--green);">✓ 200 OK</span>
              </div>
              <pre style="color:var(--text); font-size:11px; white-space:pre;">
            user touch / sensors / audio
                         │
                         ▼
                ┌─────────────────┐
                │ droidtank engine│
                └────────┬────────┘
            ┌────────────┴────────────┐
            ▼                         ▼
    ┌───────────────┐         ┌───────────────┐
    │  flutter/dart │         │ compose multi │
    │  impeller gpu │         │  kotlin 2.x   │
    └───────┬───────┘         └───────┬───────┘
            │                         │
        ┌───┴───┐                 ┌───┴───┐
        ▼       ▼                 ▼       ▼
    ┌──────┐┌──────┐          ┌──────┐┌──────┐
    │3d tilt││voice │          │bioauth││haptic│
    └──────┘└──────┘          └──────┘└──────┘
      ✓ 200   ✓ 200             ✓ 200   ✓ 200</pre>
            </div>
          </div>
        </div>

        <!-- Ecosystem Metrics Bar with Real Raw Visit Count -->
        <div class="metrics-row reveal delay-4">
          <div class="metric-cell">
            <div class="metric-val">20</div>
            <div class="metric-lbl">libraries</div>
          </div>
          <div class="metric-cell">
            <div class="metric-val" style="color:var(--cyan);">13</div>
            <div class="metric-lbl">pub.dev pkgs</div>
          </div>
          <div class="metric-cell">
            <div class="metric-val" style="color:var(--purple);">7</div>
            <div class="metric-lbl">kotlin cmp</div>
          </div>
          <div class="metric-cell">
            <div class="metric-val" style="color:var(--green);">140/140</div>
            <div class="metric-lbl">pub target</div>
          </div>
          <div class="metric-cell">
            <div class="metric-val">6</div>
            <div class="metric-lbl">live demos</div>
          </div>
          <div class="metric-cell">
            <div class="metric-val" id="hero-visitor-count" style="color:#ffffff;">--</div>
            <div class="metric-lbl">site visits</div>
          </div>
        </div>
      </div>
    </section>

    <!-- PUBLISHED PACKAGES SHOWCASE -->
    <section id="packages">
      <div class="wrapper">
        <div class="cli-tag reveal"><span>$</span> droidtank packages --inventory</div>
        <h2 class="section-title reveal delay-1">published open source libraries</h2>
        <p style="font-size:14px; color:var(--text-muted); margin-bottom:32px; max-width:680px;" class="reveal delay-1">
          20 production-grade libraries across Flutter, Dart, and Kotlin Compose Multiplatform. 100% null-safe and verified cross-platform.
        </p>

        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px; margin-bottom:24px;" class="reveal delay-2">
          <div style="background:#000; border:1px solid var(--border); padding:6px 12px; flex:1; max-width:360px; display:flex; align-items:center;">
            <span style="color:var(--text-dim); margin-right:8px; font-family:var(--mono); font-size:12px;">&gt;</span>
            <input type="text" id="pkg-search" style="background:transparent; border:none; outline:none; color:#fff; font-family:var(--mono); font-size:12px; width:100%;" placeholder="filter by name or platform..." oninput="filterPkgs()">
          </div>

          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            <button class="btn btn-muted" onclick="setFilter('all')">all (20)</button>
            <button class="btn btn-green" onclick="setFilter('demos')">⚡ live demos (6)</button>
            <button class="btn btn-muted" onclick="setFilter('flutter')">flutter (13)</button>
            <button class="btn btn-muted" onclick="setFilter('kotlin')">kotlin cmp (7)</button>
            <button class="btn btn-muted" onclick="setFilter('ai')">ai (3)</button>
            <button class="btn btn-muted" onclick="setFilter('ui')">ui (6)</button>
          </div>
        </div>

        <div class="pkg-grid reveal delay-3" id="pkg-grid">
          <!-- Injected via JS -->
        </div>
      </div>
    </section>

    <!-- ARCHITECT PROFILE / METHODOLOGY -->
    <section id="author">
      <div class="wrapper">
        <div class="cli-tag reveal"><span>$</span> man govindtank</div>
        <h2 class="section-title reveal delay-1">architect profile &amp; constraints</h2>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-top:32px;" class="reveal delay-2">
          <div style="background:var(--card-bg); border:1px solid var(--border); padding:28px;">
            <h3 style="font-size:1.25rem; font-weight:700; color:#fff; margin-bottom:10px;">Govind Tank</h3>
            <p style="font-size:13.5px; color:var(--text-muted); line-height:1.65; margin-bottom:20px;">
              Open source architect focusing on low-latency mobile graphics, Impeller GPU canvas shaders, cross-platform hardware bridges, and embedded Model Context Protocol (MCP) servers for on-device AI.
            </p>
            <div style="font-family:var(--mono); font-size:11.5px; color:var(--text-dim); display:flex; flex-direction:column; gap:6px;">
              <div>• <strong>VERIFIED PUBLISHER:</strong> <a href="https://pub.dev/publishers/govindtank.is-a.dev/packages" target="_blank" style="color:var(--green); text-decoration:none;">govindtank.is-a.dev (pub.dev) ↗</a></div>
              <div>• <strong>REPOSITORIES:</strong> <a href="https://github.com/govindtank" target="_blank" style="color:#ffffff; text-decoration:none;">514+ Open Source Repos (@govindtank) ↗</a></div>
              <div>• <strong>KOTLIN JITPACK:</strong> <a href="https://jitpack.io/#govindtank/cmp-biometrics" target="_blank" style="color:#ffffff; text-decoration:none;">JitPack Kotlin CMP Artifacts ↗</a></div>
            </div>
          </div>

          <div style="background:var(--card-bg); border:1px solid var(--border); padding:28px;">
            <div style="font-family:var(--mono); font-weight:700; color:#ffffff; font-size:13px; margin-bottom:14px; text-transform:uppercase;">SYSTEM CONSTRAINTS</div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
              <div style="background:#000; border:1px solid var(--border); padding:10px; font-size:11.5px; color:var(--text-muted);">
                <strong style="color:#fff; display:block; margin-bottom:2px;">01 // ZERO MOCK DATA</strong>
                Real sensor telemetry &amp; authentic crypto.
              </div>
              <div style="background:#000; border:1px solid var(--border); padding:10px; font-size:11.5px; color:var(--text-muted);">
                <strong style="color:#fff; display:block; margin-bottom:2px;">02 // 60 FPS FIDELITY</strong>
                Impeller GPU shader passes with zero frame drops.
              </div>
              <div style="background:#000; border:1px solid var(--border); padding:10px; font-size:11.5px; color:var(--text-muted);">
                <strong style="color:#fff; display:block; margin-bottom:2px;">03 // 140/140 TARGET</strong>
                100% null safety, lints/recommended, 0 warnings.
              </div>
              <div style="background:#000; border:1px solid var(--border); padding:10px; font-size:11.5px; color:var(--text-muted);">
                <strong style="color:#fff; display:block; margin-bottom:2px;">04 // OFFLINE AI MCP</strong>
                Local on-device Binder IPC &amp; loopback sockets.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- BLOG PREVIEW -->
    <section id="blog">
      <div class="wrapper">
        <div class="cli-tag reveal"><span>$</span> droidtank blog --recent</div>
        <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:24px; flex-wrap:wrap; gap:12px;" class="reveal delay-1">
          <div>
            <h2 class="section-title" style="margin-bottom:4px;">engineering deep dives</h2>
            <p style="font-size:13.5px; color:var(--text-muted);">120 architectural reports on mobile systems, on-device AI, and Kotlin CMP.</p>
          </div>
          <a href="blog/" class="btn btn-muted">view all 120 articles →</a>
        </div>

        <div class="reveal delay-2" id="blog-preview-list">
          <!-- Injected via JS with live view counters -->
        </div>

        <div style="text-align:center; margin-top:24px;" class="reveal delay-3">
          <a href="blog/" class="btn btn-primary" style="padding:0 24px;">explore all 120 articles in archive →</a>
        </div>
      </div>
    </section>
  </main>

  <div class="toast" id="toast">copied to clipboard</div>

  <footer>
    <div class="wrapper" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px;">
      <div>
        <div style="color:var(--text); font-weight:700; margin-bottom:4px;">govindtank.is-a.dev</div>
        <div>Total Verified Visits: <span id="footer-views" style="color:#fff; font-weight:700;">--</span> · © 2017–<span id="copy-year"></span> Govind Tank.</div>
      </div>
      <div style="display:flex; gap:16px;">
        <a href="blog/" style="color:var(--text-muted); text-decoration:none;">blog archive</a>
        <a href="https://pub.dev/publishers/govindtank.is-a.dev/packages" target="_blank" style="color:var(--green); text-decoration:none;">pub.dev publisher ↗</a>
        <a href="https://github.com/govindtank" target="_blank" style="color:var(--text-muted); text-decoration:none;">github ↗</a>
      </div>
    </div>
  </footer>

  <script>
    const packagesData = __PKGS__;
    const blogData = __BLGS__;
    document.getElementById('copy-year').textContent = new Date().getFullYear();

    // ─────────────────────────────────────────────────────────
    // REAL WORKING GOATCOUNTER TELEMETRY (100% Raw Data, Zero Fake Seeds)
    // ─────────────────────────────────────────────────────────
    function initSiteTelemetry() {
      fetch('https://govindtank.goatcounter.com/counter/%2Fdroidtank.json')
        .then(r => r.ok ? r.json() : { count: '0' })
        .then(d => {
          const live = parseInt(d.count || '0', 10);
          document.getElementById('nav-visitor-count').textContent = live.toLocaleString();
          document.getElementById('hero-visitor-count').textContent = live.toLocaleString();
          document.getElementById('footer-views').textContent = live.toLocaleString();
        })
        .catch(() => {
          document.getElementById('nav-visitor-count').textContent = '0';
          document.getElementById('hero-visitor-count').textContent = '0';
          document.getElementById('footer-views').textContent = '0';
        });
    }
    initSiteTelemetry();

    // ─────────────────────────────────────────────────────────
    // PACKAGES RENDERING
    // ─────────────────────────────────────────────────────────
    let curFilter = 'all';
    function setFilter(f) {
      curFilter = f;
      renderPkgs();
    }
    function filterPkgs() {
      renderPkgs();
    }

    function renderPkgs() {
      const q = (document.getElementById('pkg-search').value || '').toLowerCase().trim();
      const grid = document.getElementById('pkg-grid');
      grid.innerHTML = '';

      const filtered = packagesData.filter(p => {
        if (curFilter === 'demos' && !p.demoUrl) return false;
        if (curFilter === 'flutter' && p.type !== 'flutter') return false;
        if (curFilter === 'kotlin' && p.type !== 'kotlin') return false;
        if (!['all', 'demos', 'flutter', 'kotlin'].includes(curFilter)) {
          if (p.category !== curFilter) return false;
        }
        if (q) {
          return p.name.toLowerCase().includes(q) ||
                 p.tagline.toLowerCase().includes(q) ||
                 p.description.toLowerCase().includes(q) ||
                 p.highlights.some(h => h.toLowerCase().includes(q));
        }
        return true;
      });

      if (filtered.length === 0) {
        grid.innerHTML = '<div style="grid-column:1/-1; padding:40px; text-align:center; color:var(--text-dim); font-family:var(--mono);">0 packages found matching query.</div>';
        return;
      }

      filtered.forEach(p => {
        const isFlutter = p.type === 'flutter';
        const badgeEco = isFlutter 
          ? '<span class="badge-pill badge-cyan">pub.dev</span>' 
          : '<span class="badge-pill badge-purple">JitPack</span>';
        
        const badgeScore = `<span class="badge-pill badge-green">${p.score}</span>`;
        const plats = p.platforms.slice(0, 3).map(pl => `<span class="chip">${pl}</span>`).join('');

        const demoBtn = p.demoUrl 
          ? `<a href="${p.demoUrl}" target="_blank" rel="noopener" class="btn btn-green" style="flex:1;">⚡ live demo ↗</a>` 
          : '';

        const mainLinkText = isFlutter ? 'pub.dev ↗' : 'JitPack ↗';

        grid.innerHTML += `
          <div class="pkg-card">
            <div>
              <div class="pkg-header">
                <a href="${p.repoUrl}" target="_blank" rel="noopener" class="pkg-name">📦 ${p.name}</a>
                <div style="display:flex; gap:4px; flex-shrink:0;">${badgeEco} ${badgeScore}</div>
              </div>
              <div class="pkg-tagline">${p.tagline}</div>
              <div class="pkg-desc">${p.description}</div>
              <div class="pkg-chips">${plats}</div>
            </div>
            <div>
              <div class="cmd-bar">
                <span class="cmd-text">$ ${p.install}</span>
                <button class="cmd-copy" onclick="copySnippet('${p.install.replace(/'/g, "\\'")}', this)">copy</button>
              </div>
              <div class="pkg-actions">
                ${demoBtn}
                <a href="${p.pubUrl}" target="_blank" rel="noopener" class="btn btn-muted" style="flex:1;">${mainLinkText}</a>
                <a href="${p.repoUrl}" target="_blank" rel="noopener" class="btn btn-muted" style="flex:0.8;">github</a>
              </div>
            </div>
          </div>
        `;
      });
    }

    // ─────────────────────────────────────────────────────────
    // BLOG PREVIEW WITH REAL LIVE VIEW COUNTERS
    // ─────────────────────────────────────────────────────────
    function renderBlogPreview() {
      const bList = document.getElementById('blog-preview-list');
      bList.innerHTML = blogData.slice(0, 4).map(b => {
        return `
          <a href="blog/post.html?slug=${b.slug}" class="art-row">
            <div>
              <div class="art-tag-line">SYS / ${b.tag}</div>
              <div class="art-title">${b.title}</div>
              <div class="art-desc">${b.excerpt || ''}</div>
            </div>
            <div class="art-meta">
              <div>${b.date}</div>
              <div class="art-views-badge" id="preview-views-${b.slug}">👁 calculating · ${b.readTime || 8}m ↗</div>
            </div>
          </a>
        `;
      }).join('');

      // Fetch pure real counts for previews
      blogData.slice(0, 4).forEach(b => {
        fetch(`https://govindtank.goatcounter.com/counter/%2Fblog%2F${encodeURIComponent(b.slug)}.json`)
          .then(r => r.ok ? r.json() : { count: '0' })
          .then(d => {
            const live = parseInt(d.count || '0', 10);
            const el = document.getElementById(`preview-views-${b.slug}`);
            if (el) el.innerHTML = `👁 ${live.toLocaleString()} reads · ${b.readTime || 8}m ↗`;
          }).catch(() => {
            const el = document.getElementById(`preview-views-${b.slug}`);
            if (el) el.innerHTML = `👁 0 reads · ${b.readTime || 8}m ↗`;
          });
      });
    }

    // Toast and Copy helper
    let toastTimer;
    function copySnippet(text, btn) {
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(text).then(() => {
        const t = document.getElementById('toast');
        t.textContent = '✓ copied: ' + text;
        t.classList.add('show');
        if (btn) {
          const orig = btn.textContent;
          btn.textContent = 'ok';
          btn.style.color = 'var(--green)';
          setTimeout(() => { btn.textContent = orig; btn.style.color = ''; }, 1400);
        }
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => t.classList.remove('show'), 2000);
      });
    }

    renderPkgs();
    renderBlogPreview();
  </script>
</body>
</html>"""

    blog_index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Engineering Blog Archive | droidtank.is-a.dev</title>
  <meta name="description" content="120 architectural engineering deep dives into Android, Flutter, Kotlin Multiplatform, and AI systems by Govind Tank.">
  <meta name="google-site-verification" content="XgM7pPr1XAMYxTg37pXPzcTeW9-m0x96HRA65XtPBjM">
  <link rel="canonical" href="https://droidtank.is-a.dev/blog/">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">

  <script data-goatcounter="https://govindtank.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>

  <style>
    __CORE_CSS__

    .archive-header {
      padding-top: 110px;
      padding-bottom: 30px;
      border-bottom: 1px solid var(--border);
    }
    .breadcrumbs {
      font-family: var(--mono);
      font-size: 11.5px;
      color: var(--text-dim);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .breadcrumbs a { color: var(--text-muted); text-decoration: none; }
    .breadcrumbs a:hover { color: #ffffff; }

    .paginator {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 16px;
      margin: 40px 0 60px;
      font-family: var(--mono);
      font-size: 12px;
    }
  </style>
</head>
<body>
  <div class="bg-grid"></div>

  <!-- Nav -->
  <nav class="site-nav">
    <div class="nav-inner">
      <a href="../" class="nav-brand">
        govindtank<span style="color:var(--text-dim)">/blog/archive</span>
      </a>

      <ul class="nav-links">
        <li><a href="../" class="nav-link">home</a></li>
        <li><a href="../#packages" class="nav-link">packages</a></li>
        <li><a href="./" class="nav-link active">blog (120)</a></li>
        <li><a href="https://pub.dev/publishers/govindtank.is-a.dev/packages" target="_blank" rel="noopener" class="nav-link">publisher ↗</a></li>
        <li><a href="https://github.com/govindtank" target="_blank" rel="noopener" class="nav-link">github ↗</a></li>
      </ul>

      <div class="telemetry-badge" title="Live Verified Visits">
        <span class="pulse-dot"></span>
        <span>VISITS: <strong id="archive-views" style="color:#fff;">--</strong></span>
      </div>
    </div>
  </nav>

  <main>
    <div class="archive-header">
      <div class="wrapper reveal">
        <div class="breadcrumbs">
          <a href="../">&gt; home</a>
          <span>/</span>
          <span style="color:#ffffff;">blog</span>
        </div>
        <div class="cli-tag"><span>$</span> ls -la /var/log/engineering_reports/</div>
        <h1 class="display-title" style="font-size:clamp(2rem,4.5vw,3rem);">technical archive.</h1>
        <p style="color:var(--text-muted); font-size:14px; max-width:720px;">
          120 architectural deep dives into mobile systems, Kotlin Compose Multiplatform, on-device AI agents, and GPU CustomPainters.
        </p>

        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px; margin:32px 0 16px;" class="reveal delay-1">
          <div style="background:#000; border:1px solid var(--border); padding:6px 12px; flex:1; max-width:380px; display:flex; align-items:center;">
            <span style="color:var(--text-dim); margin-right:8px; font-family:var(--mono); font-size:12px;">&gt;</span>
            <input type="text" id="archive-search" style="background:transparent; border:none; outline:none; color:#fff; font-family:var(--mono); font-size:12px; width:100%;" placeholder="grep articles by keyword or topic..." oninput="filterArchive()">
          </div>

          <div style="display:flex; gap:6px; flex-wrap:wrap;">
            <button class="btn btn-muted" onclick="setArchiveTag('all')">[all: 120]</button>
            <button class="btn btn-muted" onclick="setArchiveTag('AI-Engineering')">[ai &amp; mcp]</button>
            <button class="btn btn-muted" onclick="setArchiveTag('Flutter')">[flutter]</button>
            <button class="btn btn-muted" onclick="setArchiveTag('Android')">[android]</button>
            <button class="btn btn-muted" onclick="setArchiveTag('Kotlin-CMP')">[kotlin cmp]</button>
          </div>
        </div>
      </div>
    </div>

    <div class="wrapper" style="padding-top:24px;">
      <div id="articles-list-container" class="reveal delay-2">
        <!-- Injected via JS with live view count for each post -->
      </div>

      <div class="paginator reveal delay-3" id="archive-paginator"></div>
    </div>
  </main>

  <footer>
    <div class="wrapper" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
      <div>© 2017–<span id="copy-year"></span> Govind Tank. All articles open source.</div>
      <a href="../" style="color:var(--text-dim); text-decoration:none;">[← Return to Homepage]</a>
    </div>
  </footer>

  <script>
    const blogData = __BLGS__;
    document.getElementById('copy-year').textContent = new Date().getFullYear();

    // Real Telemetry count for Archive page
    function initArchiveTelemetry() {
      fetch('https://govindtank.goatcounter.com/counter/%2Fdroidtank.json')
        .then(r => r.ok ? r.json() : { count: '0' })
        .then(d => {
          const live = parseInt(d.count || '0', 10);
          document.getElementById('archive-views').textContent = live.toLocaleString();
        })
        .catch(() => {
          document.getElementById('archive-views').textContent = '0';
        });
    }
    initArchiveTelemetry();

    const PER_PAGE = 10;
    let curPage = 1;
    let curTag = 'all';

    const container = document.getElementById('articles-list-container');
    const paginator = document.getElementById('archive-paginator');
    const searchInput = document.getElementById('archive-search');

    function getFiltered() {
      const q = (searchInput.value || '').toLowerCase().trim();
      return blogData.filter(b => {
        if (curTag !== 'all' && b.tag.toLowerCase() !== curTag.toLowerCase()) return false;
        if (q) {
          return b.title.toLowerCase().includes(q) ||
                 (b.excerpt && b.excerpt.toLowerCase().includes(q)) ||
                 b.tag.toLowerCase().includes(q);
        }
        return true;
      });
    }

    function renderArchive() {
      const filtered = getFiltered();
      const totalPages = Math.max(1, Math.ceil(filtered.length / PER_PAGE));
      if (curPage > totalPages) curPage = 1;

      const start = (curPage - 1) * PER_PAGE;
      const items = filtered.slice(start, start + PER_PAGE);

      container.innerHTML = '';
      if (items.length === 0) {
        container.innerHTML = '<div style="padding:60px; text-align:center; font-family:var(--mono); font-size:12px; color:var(--text-dim);">0 matching records found.</div>';
        paginator.innerHTML = '';
        return;
      }

      items.forEach(b => {
        container.innerHTML += `
          <a href="post.html?slug=${b.slug}" class="art-row">
            <div>
              <div class="art-tag-line">SYS / ${b.tag}</div>
              <div class="art-title">${b.title}</div>
              <div class="art-desc">${b.excerpt || ''}</div>
            </div>
            <div class="art-meta">
              <div>${b.date}</div>
              <div class="art-views-badge" id="art-view-${b.slug}">👁 calculating · ${b.readTime || 8}m ↗</div>
            </div>
          </a>
        `;
      });

      // Fetch pure live views for visible items
      items.forEach(b => {
        fetch(`https://govindtank.goatcounter.com/counter/%2Fblog%2F${encodeURIComponent(b.slug)}.json`)
          .then(r => r.ok ? r.json() : { count: '0' })
          .then(d => {
            const live = parseInt(d.count || '0', 10);
            const el = document.getElementById(`art-view-${b.slug}`);
            if (el) el.innerHTML = `👁 ${live.toLocaleString()} reads · ${b.readTime || 8}m ↗`;
          }).catch(() => {
            const el = document.getElementById(`art-view-${b.slug}`);
            if (el) el.innerHTML = `👁 0 reads · ${b.readTime || 8}m ↗`;
          });
      });

      paginator.innerHTML = `
        <button class="btn btn-muted" onclick="changePage(-1)" ${curPage === 1 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''}>&lt; prev</button>
        <span style="color:var(--text-dim);">page ${curPage} / ${totalPages}</span>
        <button class="btn btn-muted" onclick="changePage(1)" ${curPage === totalPages ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''}>next &gt;</button>
      `;
    }

    function changePage(d) {
      curPage += d;
      renderArchive();
      window.scrollTo({ top: 100, behavior: 'smooth' });
    }

    function setArchiveTag(tag) {
      curTag = tag;
      curPage = 1;
      renderArchive();
    }

    function filterArchive() {
      curPage = 1;
      renderArchive();
    }

    renderArchive();
  </script>
</body>
</html>"""

    blog_post_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="meta-post-title">Article Reader | droidtank.is-a.dev</title>
  <meta name="description" content="Engineering deep dive by Govind Tank.">
  <meta name="google-site-verification" content="XgM7pPr1XAMYxTg37pXPzcTeW9-m0x96HRA65XtPBjM">
  <link rel="canonical" id="meta-canonical" href="https://droidtank.is-a.dev/blog/post.html">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">

  <!-- GoatCounter Telemetry -->
  <script data-goatcounter="https://govindtank.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>

  <style>
    __CORE_CSS__

    .reader-wrap {
      max-width: 800px;
      margin: 0 auto;
      padding: 130px 24px 80px;
    }
    .breadcrumbs-post {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-dim);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .breadcrumbs-post a { color: var(--text-muted); text-decoration: none; }
    .breadcrumbs-post a:hover { color: #ffffff; }

    .post-header {
      border-bottom: 1px solid var(--border);
      padding-bottom: 24px;
      margin-bottom: 32px;
    }
    .post-tag {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--purple);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 10px;
    }
    .post-title {
      font-size: clamp(1.9rem, 4.5vw, 2.8rem);
      font-weight: 700;
      color: #ffffff;
      line-height: 1.15;
      letter-spacing: -1px;
      margin-bottom: 14px;
    }
    .post-meta-bar {
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: var(--mono);
      font-size: 12px;
      color: var(--text-dim);
      flex-wrap: wrap;
    }
    .post-views-highlight {
      color: var(--green);
      font-weight: 600;
    }

    .post-cover {
      width: 100%;
      max-height: 400px;
      object-fit: cover;
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }

    /* Markdown Article Typography */
    .post-content {
      font-size: 15px;
      line-height: 1.8;
      color: #d4d4d8;
    }
    .post-content h1, .post-content h2, .post-content h3 {
      color: #ffffff;
      font-family: var(--mono);
      font-weight: 700;
      margin: 36px 0 14px;
      text-transform: lowercase;
      letter-spacing: -0.5px;
    }
    .post-content h1 { font-size: 1.6rem; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
    .post-content h2 { font-size: 1.35rem; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
    .post-content h3 { font-size: 1.15rem; }
    .post-content p { margin-bottom: 20px; }
    .post-content ul, .post-content ol { margin: 14px 0 20px 22px; }
    .post-content li { margin-bottom: 6px; }
    .post-content strong { color: #ffffff; font-weight: 700; }
    .post-content blockquote {
      border-left: 2px solid var(--green);
      padding: 6px 0 6px 18px;
      margin: 20px 0;
      color: var(--text-muted);
    }
    .post-content pre {
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 18px;
      overflow-x: auto;
      font-family: var(--mono);
      font-size: 12.5px;
      margin: 24px 0;
      position: relative;
    }
    .post-content code {
      font-family: var(--mono);
      background: #111111;
      padding: 2px 5px;
      font-size: 0.9em;
      color: var(--green);
    }
    .post-content pre code {
      background: transparent;
      padding: 0;
      color: inherit;
    }

    .copy-btn-code {
      position: absolute;
      top: 10px;
      right: 10px;
      background: #111111;
      border: 1px solid var(--border);
      color: var(--text-dim);
      padding: 3px 8px;
      font-family: var(--mono);
      font-size: 10px;
      cursor: pointer;
      text-transform: uppercase;
      transition: all 0.15s;
    }
    .copy-btn-code:hover {
      color: #ffffff;
      border-color: var(--border-lit);
    }

    .pBar {
      position: fixed;
      top: 0; left: 0;
      height: 3px;
      background: var(--green);
      width: 0%;
      z-index: 2000;
      transition: width 0.1s;
    }
  </style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="pBar" id="readBar"></div>

  <!-- Nav -->
  <header class="site-nav">
    <div class="nav-inner">
      <a href="../" class="nav-brand">
        govindtank<span style="color:var(--text-dim)">/reader</span>
      </a>

      <ul class="nav-links">
        <li><a href="../" class="nav-link">home</a></li>
        <li><a href="./" class="nav-link active">blog archive</a></li>
        <li><a href="https://pub.dev/publishers/govindtank.is-a.dev/packages" target="_blank" rel="noopener" class="nav-link">publisher ↗</a></li>
        <li><a href="https://github.com/govindtank" target="_blank" rel="noopener" class="nav-link">github ↗</a></li>
      </ul>

      <a href="./" class="btn btn-muted" style="height:28px; font-size:10.5px;">← back to archive</a>
    </div>
  </header>

  <main>
    <article class="reader-wrap reveal">
      <div class="breadcrumbs-post">
        <a href="../">&gt; home</a>
        <span>/</span>
        <a href="./">blog</a>
        <span>/</span>
        <span id="post-breadcrumb" style="color:#ffffff; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; max-width:320px;">article</span>
      </div>

      <div class="post-header">
        <div class="post-tag" id="post-tag">TAG</div>
        <h1 class="post-title" id="post-title">Loading article...</h1>
        <div class="post-meta-bar">
          <span>AUTHOR: <strong>GOVIND TANK</strong></span>
          <span>·</span>
          <span id="post-date">DATE</span>
          <span>·</span>
          <span id="post-readtime">8 MIN READ</span>
          <span>·</span>
          <!-- Pure Real Individual Blog Post Visitor Counter -->
          <span class="post-views-highlight" id="individual-post-views">👁 calculating reads...</span>
        </div>
      </div>

      <img id="post-cover" class="post-cover" src="" alt="" style="display:none;">

      <div class="post-content" id="post-content">
        <!-- Injected via JS -->
      </div>

      <div style="margin-top:60px; padding-top:24px; border-top:1px solid var(--border); display:flex; justify-content:space-between; flex-wrap:wrap; gap:16px;">
        <a href="./" class="btn btn-muted">← Back to Blog Archive</a>
        <button class="btn btn-primary" onclick="sharePost()">🔗 Share Article</button>
      </div>
    </article>
  </main>

  <div class="toast" id="toast">copied to clipboard</div>

  <footer>
    <div class="wrapper" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
      <div>© 2017–<span id="copy-year"></span> Govind Tank. All articles open source.</div>
      <a href="./" style="color:var(--text-dim); text-decoration:none;">[← Blog Archive]</a>
    </div>
  </footer>

  <script>
    const blogData = __BLGS__;
    document.getElementById('copy-year').textContent = new Date().getFullYear();

    const urlParams = new URLSearchParams(window.location.search);
    const slug = urlParams.get('slug') || (blogData[0] ? blogData[0].slug : '');

    const article = blogData.find(b => b.slug === slug) || blogData[0];

    if (article) {
      document.title = `${article.title} | droidtank.is-a.dev`;
      document.getElementById('post-breadcrumb').textContent = article.title;
      document.getElementById('post-tag').textContent = `SYS / ${article.tag}`;
      document.getElementById('post-title').textContent = article.title;
      document.getElementById('post-date').textContent = article.date.toUpperCase();
      document.getElementById('post-readtime').textContent = `${article.readTime || 8} MIN READ`;

      const cover = document.getElementById('post-cover');
      if (article.coverImage) {
        cover.src = article.coverImage;
        cover.style.display = 'block';
      }

      document.getElementById('post-content').innerHTML = article.content;

      // Copy buttons for code blocks
      document.querySelectorAll('#post-content pre').forEach(pre => {
        const btn = document.createElement('button');
        btn.className = 'copy-btn-code';
        btn.textContent = 'copy';
        btn.onclick = () => {
          navigator.clipboard.writeText(pre.textContent.replace('copy', '').trim());
          btn.textContent = 'ok';
          btn.style.color = 'var(--green)';
          setTimeout(() => { btn.textContent = 'copy'; btn.style.color = ''; }, 1400);
        };
        pre.appendChild(btn);
      });

      // ─────────────────────────────────────────────────────────
      // REAL INDIVIDUAL BLOG POST VISITOR COUNTER (100% Raw Data)
      // ─────────────────────────────────────────────────────────
      // Track pageview with GoatCounter for this specific article path
      if (window.goatcounter && window.goatcounter.count) {
        window.goatcounter.count({
          path: '/blog/' + slug,
          title: article.title,
          event: false
        });
      }

      // Fetch pure live individual view count from GoatCounter API
      fetch(`https://govindtank.goatcounter.com/counter/%2Fblog%2F${encodeURIComponent(slug)}.json`)
        .then(r => r.ok ? r.json() : { count: '0' })
        .then(d => {
          const live = parseInt(d.count || '0', 10);
          document.getElementById('individual-post-views').textContent = `👁 ${live.toLocaleString()} verified reads`;
        })
        .catch(() => {
          document.getElementById('individual-post-views').textContent = `👁 0 verified reads`;
        });
    }

    // Reading bar
    window.addEventListener('scroll', () => {
      const doc = document.documentElement;
      document.getElementById('readBar').style.width = (doc.scrollTop / (doc.scrollHeight - doc.clientHeight) * 100) + '%';
    });

    let toastTimer;
    function sharePost() {
      if (navigator.clipboard) {
        navigator.clipboard.writeText(window.location.href).then(() => {
          const t = document.getElementById('toast');
          t.textContent = '✓ article link copied to clipboard';
          t.classList.add('show');
          clearTimeout(toastTimer);
          toastTimer = setTimeout(() => t.classList.remove('show'), 2000);
        });
      }
    }
  </script>
</body>
</html>"""

    # String replacements
    index_html = index_html.replace('__CORE_CSS__', core_css).replace('__PKGS__', packages_json).replace('__BLGS__', blogs_json)
    blog_index_html = blog_index_html.replace('__CORE_CSS__', core_css).replace('__BLGS__', blogs_json)
    blog_post_html = blog_post_html.replace('__CORE_CSS__', core_css).replace('__BLGS__', blogs_json)

    with open('/Users/govind/workspace/droidtank.is-a.dev/index.html', 'w') as f:
        f.write(index_html)
    with open('/Users/govind/workspace/droidtank.is-a.dev/blog/index.html', 'w') as f:
        f.write(blog_index_html)
    with open('/Users/govind/workspace/droidtank.is-a.dev/blog/post.html', 'w') as f:
        f.write(blog_post_html)

    print("Complete site rebuilt with 100% pure real telemetry.")

if __name__ == '__main__':
    build()
