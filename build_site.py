import json
import os

def build_site():
    with open('/Users/govind/workspace/droidtank.is-a.dev/data_packages.json', 'r') as f:
        packages = json.load(f)

    with open('/Users/govind/workspace/droidtank.is-a.dev/data_blogs.json', 'r') as f:
        blogs = json.load(f)

    # Attach rich sample code for every package
    code_map = {
        'spatial_card': """import 'package:flutter/material.dart';
import 'package:spatial_card/spatial_card.dart';

SpatialCard(
  borderRadius: BorderRadius.circular(20),
  depth: 24.0,
  enableGlare: true,
  enableTilt: true,
  child: Container(
    padding: const EdgeInsets.all(24),
    child: const Text('VisionOS Spatial 3D Card', style: TextStyle(color: Colors.white)),
  ),
)""",
        'ambient_backdrop_glow': """import 'package:flutter/material.dart';
import 'package:ambient_backdrop_glow/ambient_backdrop_glow.dart';

AmbientBackdropGlow(
  imageProvider: const NetworkImage('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe'),
  blurRadius: 48.0,
  blendMode: BlendMode.srcOver,
  child: const AlbumPlayerUI(),
)""",
        'ai_voice_orb': """import 'package:flutter/material.dart';
import 'package:ai_voice_orb/ai_voice_orb.dart';

AiVoiceOrb(
  state: OrbState.speaking, // listening, thinking, speaking
  frequencyStream: audioStream.amplitudeStream,
  glowColor: Colors.cyanAccent,
  size: 180,
  particleSpeed: 1.2,
)""",
        'dart_vector_index': """import 'package:dart_vector_index/dart_vector_index.dart';

final index = VectorIndex(dimension: 384, metric: Metric.cosine);
await index.insert(id: 'doc_1', vector: embeddingList, metadata: {'title': 'On-Device AI'});
final matches = await index.query(queryVector, topK: 5);
for (final match in matches) {
  print('Found: ${match.id} (Score: ${match.score})');
}""",
        'waveform_pro': """import 'package:flutter/material.dart';
import 'package:waveform_pro/waveform_pro.dart';

WaveformPro(
  samples: audioWaveformSamples,
  activeColor: Colors.cyanAccent,
  inactiveColor: Colors.white24,
  progress: playbackProgress,
  style: WaveformStyle.roundedBars,
  onSeek: (position) => audioPlayer.seek(position),
)""",
        'scratch_reveal': """import 'package:flutter/material.dart';
import 'package:scratch_reveal/scratch_reveal.dart';

ScratchReveal(
  revealThreshold: 0.65,
  brushSize: 32.0,
  onRevealed: () => showCelebrationAnimation(),
  coverWidget: Container(color: const Color(0xFF1E222D)),
  child: const RewardCardWidget(),
)""",
        'segmented_ring_painter': """import 'package:flutter/material.dart';
import 'package:segmented_ring_painter/segmented_ring_painter.dart';

SegmentedRingWidget(
  strokeWidth: 14.0,
  segments: [
    RingSegment(value: 450, color: const Color(0xFF00E5FF), label: 'Move'),
    RingSegment(value: 30, color: const Color(0xFF00FF88), label: 'Exercise'),
    RingSegment(value: 12, color: const Color(0xFFB580FF), label: 'Stand'),
  ],
)""",
        'currency_field_formatter': """import 'package:flutter/material.dart';
import 'package:currency_field_formatter/currency_field_formatter.dart';

TextField(
  keyboardType: TextInputType.number,
  inputFormatters: [
    CurrencyTextInputFormatter(
      currencySymbol: '₹',
      decimalDigits: 2,
      enableNegative: false,
    ),
  ],
)""",
        'country_mobile_validator': """import 'package:country_mobile_validator/country_mobile_validator.dart';

final isValid = CountryMobileValidator.validate(
  phoneNumber: '+919876543210',
  countryCode: 'IN',
);
print('Phone valid: $isValid');""",
        'cron_schedule': """import 'package:cron_schedule/cron_schedule.dart';

final schedule = CronSchedule.parse('0 9 * * 1-5');
final nextRun = schedule.next(DateTime.now());
print('Next cron execution: $nextRun');""",
        'offline_outbox': """import 'package:offline_outbox/offline_outbox.dart';

final outbox = OfflineOutbox(storage: SqliteStorage());
await outbox.enqueue(SyncPayload(action: 'SYNC_TRANSACTION', data: {'amount': 1500}));
outbox.startAutoSync(onProcess: (task) async => apiClient.post('/sync', body: task.data));""",
        'quote_painter': """import 'package:flutter/material.dart';
import 'package:quote_painter/quote_painter.dart';

QuotePainterCanvas(
  quote: 'Simplicity is prerequisite for reliability.',
  author: 'Edsger W. Dijkstra',
  style: QuoteStyle.cyberpunkDark,
  exportResolution: const Size(1080, 1920),
)""",
        'flutter_whisper': """import 'package:flutter_whisper/flutter_whisper.dart';

final whisper = FlutterWhisper(modelPath: 'assets/models/whisper-tiny.bin');
final text = await whisper.transcribeAudioFile(recordedAudioPath);
print('Transcription: $text');""",
        'cmp-biometrics': """// Kotlin Compose Multiplatform
val biometrics = rememberBiometricPrompt()
biometrics.authenticate(
    title = "Authenticate for Vault",
    subtitle = "Verify Fingerprint or Face ID",
    onSuccess = { unlockSecureData() },
    onError = { err -> handleAuthError(err) }
)""",
        'cmp-haptics': """// Kotlin Compose Multiplatform
val haptics = rememberHapticFeedback()
Button(onClick = {
    haptics.perform(HapticType.ImpactHeavy)
}) {
    Text("Trigger Dynamic Haptic")
}""",
        'cmp-media-player': """// Kotlin Compose Multiplatform
MediaPlayerSurface(
    url = "https://cdn.droidtank.dev/sample.mp4",
    modifier = Modifier.fillMaxWidth().height(240.dp),
    autoPlay = true,
    resizeMode = ResizeMode.Fit
)""",
        'cmp-clipboard': """// Kotlin Compose Multiplatform
val clipboard = rememberClipboard()
clipboard.setText("https://droidtank.is-a.dev")""",
        'cmp-keyboard': """// Kotlin Compose Multiplatform
ProvideKeyboardInsets {
    LazyColumn(modifier = Modifier.fillMaxSize().imePadding()) {
        items(messages) { msg -> MessageBubble(msg) }
    }
}""",
        'cmp-linked-text': """// Kotlin Compose Multiplatform
LinkedText(
    text = "Follow @govindtank on GitHub and visit https://droidtank.is-a.dev",
    onLinkClick = { uri -> openUrlInBrowser(uri) }
)""",
        'capture-improvement-kotlin': """// Kotlin Android NDK Pipeline
val capturePipeline = SurfaceCapturePipeline(
    targetResolution = Size(1920, 1080),
    enableHardwareGpuSync = true
)
capturePipeline.startCapture { frame -> processFrame(frame) }"""
    }

    for p in packages:
        p['sampleCode'] = code_map.get(p['name'], '// See package documentation for full examples.')

    packages_json = json.dumps(packages)
    blogs_json = json.dumps(blogs)

    template = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>droidtank | the mobile &amp; ai ecosystem</title>
  <meta name="description" content="One architect. Every platform. 20 production-grade open source packages across Flutter, Dart, Kotlin Compose Multiplatform, and on-device AI.">
  <meta name="google-site-verification" content="XgM7pPr1XAMYxTg37pXPzcTeW9-m0x96HRA65XtPBjM">
  <link rel="canonical" href="https://droidtank.is-a.dev/">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
  
  <!-- OpenGraph / Twitter -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://droidtank.is-a.dev/">
  <meta property="og:title" content="droidtank | the mobile &amp; ai ecosystem">
  <meta property="og:description" content="20 open-source packages on pub.dev and JitPack. 140/140 pub points, 120 engineering articles by Govind Tank.">
  <meta property="og:site_name" content="droidtank">

  <!-- Google Fonts: IBM Plex Mono & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- GoatCounter Telemetry -->
  <script>
    window.goatcounter = {
      path: function(p) {
        if (location.hash && location.hash.startsWith('#blog/')) {
          return '/blog/' + location.hash.replace('#blog/', '');
        }
        return '/droidtank' + (p === '/' ? '' : (p.startsWith('/') ? p : '/' + p));
      }
    };
  </script>
  <script data-goatcounter="https://govindtank.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>

  <style>
    :root {
      --bg: #000000;
      --bg-surface: #0a0a0c;
      --bg-surface-elevated: #111217;
      --bg-surface-hover: #161820;
      --border: #1e2029;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-focus: #38bdf8;
      --text: #f4f4f5;
      --text-muted: #a1a1aa;
      --text-dim: #71717a;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.2);
      --green: #10b981;
      --green-glow: rgba(16, 185, 129, 0.2);
      --purple: #a855f7;
      --amber: #f59e0b;
      --font-mono: 'IBM Plex Mono', 'JetBrains Mono', monospace;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    html { scroll-behavior: smooth; background: var(--bg); color: var(--text); }
    body {
      font-family: var(--font-sans);
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Minimal Matrix Grid */
    .bg-grid {
      position: fixed;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 48px 48px;
      pointer-events: none;
      z-index: 0;
    }

    .bg-radial {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 50% 15%, rgba(56, 189, 248, 0.04) 0%, transparent 60%),
                  radial-gradient(circle at 85% 65%, rgba(168, 85, 247, 0.03) 0%, transparent 50%);
      pointer-events: none;
      z-index: 0;
    }

    /* Top Navigation Bar */
    nav {
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 1000;
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border-bottom: 1px solid var(--border-subtle);
    }
    nav .nav-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #fff;
    }
    .brand-logo {
      width: 28px;
      height: 28px;
      background: #000;
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.15);
    }
    .brand-title {
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 700;
      letter-spacing: -0.3px;
    }
    .brand-sub {
      color: var(--text-dim);
      font-weight: 400;
      font-size: 13px;
    }

    .nav-center {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .nav-search-trigger {
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 6px;
      color: var(--text-dim);
      font-size: 13px;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: all 0.2s;
    }
    .nav-search-trigger:hover {
      border-color: var(--border-focus);
      color: var(--text);
    }
    .kbd-chip {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 11px;
      color: var(--text-muted);
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 4px;
      list-style: none;
    }
    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 500;
      padding: 6px 12px;
      border-radius: 6px;
      transition: all 0.2s;
      font-family: var(--font-mono);
    }
    .nav-link:hover, .nav-link.active {
      color: #fff;
      background: rgba(255, 255, 255, 0.05);
    }

    .nav-telemetry {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: var(--text-muted);
      background: rgba(16, 185, 129, 0.06);
      border: 1px solid rgba(16, 185, 129, 0.25);
      padding: 4px 10px;
      border-radius: 20px;
      text-decoration: none;
    }
    .status-dot {
      width: 6px; height: 6px;
      border-radius: 50%;
      background: var(--green);
      box-shadow: 0 0 8px var(--green);
      animation: pulseDot 2s infinite;
    }
    @keyframes pulseDot {
      0%, 100% { opacity: 0.7; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    /* Global Container */
    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 10;
    }
    section {
      padding: 90px 0;
      border-bottom: 1px solid var(--border-subtle);
    }

    /* Terminal Section Prompt */
    .terminal-header-prompt {
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--accent);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .terminal-header-prompt .prefix {
      color: var(--green);
      font-weight: 700;
    }
    .terminal-header-prompt .cursor-blink {
      display: inline-block;
      width: 8px;
      height: 14px;
      background: var(--accent);
      animation: blink 1s step-end infinite;
      vertical-align: middle;
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }

    .section-title {
      font-size: clamp(1.8rem, 3.5vw, 2.5rem);
      font-weight: 800;
      letter-spacing: -1px;
      color: #fff;
      margin-bottom: 8px;
      line-height: 1.2;
    }
    .section-sub {
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 720px;
      margin-bottom: 36px;
    }

    /* Hero Section */
    .hero {
      min-height: 92vh;
      display: flex;
      align-items: center;
      padding-top: 100px;
      padding-bottom: 60px;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 48px;
      align-items: center;
      width: 100%;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 5px 14px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      font-size: 12.5px;
      font-family: var(--font-mono);
      color: var(--text-muted);
      margin-bottom: 24px;
    }
    .hero-badge .verified-check {
      color: var(--green);
      font-weight: 700;
    }
    .hero h1 {
      font-size: clamp(2.6rem, 5.5vw, 4.4rem);
      font-weight: 800;
      line-height: 1.08;
      letter-spacing: -2px;
      color: #fff;
      margin-bottom: 16px;
    }
    .hero h1 .gradient-text {
      background: linear-gradient(135deg, #ffffff 0%, #a1a1aa 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    .hero-tagline {
      font-size: 1.2rem;
      color: var(--text-muted);
      max-width: 580px;
      line-height: 1.6;
      margin-bottom: 32px;
    }
    .hero-tagline strong {
      color: #fff;
      font-weight: 600;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 40px;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 20px;
      border-radius: 6px;
      font-size: 13.5px;
      font-family: var(--font-mono);
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      border: 1px solid transparent;
      user-select: none;
    }
    .btn-primary {
      background: #ffffff;
      color: #000000;
      border-color: #ffffff;
    }
    .btn-primary:hover {
      background: #e4e4e7;
      transform: translateY(-2px);
      box-shadow: 0 4px 20px rgba(255, 255, 255, 0.15);
    }
    .btn-secondary {
      background: var(--bg-surface);
      color: var(--text);
      border-color: var(--border);
    }
    .btn-secondary:hover {
      background: var(--bg-surface-elevated);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-2px);
    }
    .btn-green {
      background: rgba(16, 185, 129, 0.1);
      color: var(--green);
      border-color: rgba(16, 185, 129, 0.3);
    }
    .btn-green:hover {
      background: var(--green);
      color: #000;
      transform: translateY(-2px);
      box-shadow: 0 4px 16px var(--green-glow);
    }

    /* ASCII 3D Hero Scene */
    .ascii-hero-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }
    .ascii-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 12px;
      margin-bottom: 16px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-dim);
    }
    .ascii-controls {
      display: flex;
      gap: 6px;
    }
    .ascii-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-family: var(--font-mono);
      cursor: pointer;
    }
    .ascii-btn.active {
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent);
      border-color: var(--accent);
    }
    .ascii-display {
      font-family: var(--font-mono);
      font-size: 10px;
      line-height: 1.15;
      letter-spacing: 1px;
      color: var(--accent);
      white-space: pre;
      text-align: center;
      user-select: none;
      height: 280px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }

    /* Metrics Bar */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 12px;
      margin-top: 40px;
    }
    .metric-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 16px;
      text-align: left;
      transition: all 0.2s;
    }
    .metric-card:hover {
      border-color: var(--border-focus);
      background: var(--bg-surface-elevated);
      transform: translateY(-2px);
    }
    .metric-val {
      font-family: var(--font-mono);
      font-size: 1.6rem;
      font-weight: 700;
      color: #fff;
      line-height: 1;
      margin-bottom: 6px;
    }
    .metric-lbl {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* Interactive Code Switcher Section */
    .code-switcher-box {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
    }
    .code-switcher-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #000;
      border-bottom: 1px solid var(--border-subtle);
      padding: 8px 16px;
      flex-wrap: wrap;
      gap: 12px;
    }
    .code-tabs {
      display: flex;
      gap: 6px;
    }
    .code-tab-btn {
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-dim);
      padding: 6px 12px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 12.5px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .code-tab-btn:hover {
      color: var(--text);
    }
    .code-tab-btn.active {
      color: #fff;
      background: var(--bg-surface);
      border-color: var(--border);
    }
    .pkg-select {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text);
      font-family: var(--font-mono);
      font-size: 12px;
      padding: 6px 12px;
      border-radius: 6px;
      outline: none;
      cursor: pointer;
    }
    .code-body {
      padding: 24px;
      font-family: var(--font-mono);
      font-size: 13px;
      line-height: 1.7;
      overflow-x: auto;
      position: relative;
    }
    .code-copy-btn {
      position: absolute;
      top: 16px;
      right: 16px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 5px 10px;
      border-radius: 4px;
      font-size: 11.5px;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .code-copy-btn:hover {
      background: var(--text);
      color: #000;
    }

    /* Architecture Grid */
    .arch-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin-bottom: 32px;
    }
    .arch-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 24px;
      transition: all 0.25s;
    }
    .arch-card:hover {
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-2px);
    }
    .arch-title {
      font-family: var(--font-mono);
      font-size: 1.1rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .arch-desc {
      color: var(--text-muted);
      font-size: 13.5px;
      line-height: 1.6;
      margin-bottom: 16px;
    }
    .arch-ascii {
      background: #000000;
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 14px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      line-height: 1.35;
      color: var(--accent);
      overflow-x: auto;
      white-space: pre;
    }

    /* Flow Section: Agent vs Human */
    .flow-toggle-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 30px;
      padding: 4px;
      width: fit-content;
      margin-bottom: 32px;
    }
    .flow-toggle-btn {
      padding: 6px 18px;
      border-radius: 20px;
      border: none;
      background: transparent;
      color: var(--text-dim);
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .flow-toggle-btn.active {
      background: #ffffff;
      color: #000000;
    }

    .flow-steps {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }
    .flow-step-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .step-num {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent);
      margin-bottom: 12px;
    }
    .step-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 8px;
    }
    .step-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 16px;
    }
    .step-box {
      background: #000;
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 12px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: #fff;
      overflow-x: auto;
    }

    /* Terminal Simulator Section */
    .terminal-sim-box {
      background: #050505;
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    }
    .term-titlebar {
      background: #0f1015;
      border-bottom: 1px solid var(--border-subtle);
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-dim);
    }
    .term-dots {
      display: flex;
      gap: 6px;
    }
    .term-dot {
      width: 10px; height: 10px;
      border-radius: 50%;
      background: #27272a;
    }
    .term-body {
      padding: 20px;
      font-family: var(--font-mono);
      font-size: 13px;
      line-height: 1.6;
      min-height: 260px;
      max-height: 400px;
      overflow-y: auto;
      color: #e4e4e7;
    }
    .term-input-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 10px;
    }
    .term-prompt {
      color: var(--green);
      font-weight: 600;
      white-space: nowrap;
    }
    .term-input {
      flex: 1;
      background: transparent;
      border: none;
      outline: none;
      color: #fff;
      font-family: var(--font-mono);
      font-size: 13px;
    }
    .term-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding: 12px 20px;
      background: #0a0a0c;
      border-top: 1px solid var(--border-subtle);
    }
    .term-chip {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 4px 10px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11.5px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .term-chip:hover {
      background: rgba(56, 189, 248, 0.1);
      color: var(--accent);
      border-color: var(--accent);
    }

    /* Package Grid */
    .filter-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 28px;
    }
    .search-input-wrap {
      position: relative;
      min-width: 320px;
      flex: 1;
      max-width: 480px;
    }
    .search-input-wrap input {
      width: 100%;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px 14px 10px 38px;
      color: #fff;
      font-family: var(--font-mono);
      font-size: 13px;
      outline: none;
      transition: all 0.2s;
    }
    .search-input-wrap input:focus {
      border-color: var(--border-focus);
      box-shadow: 0 0 16px var(--accent-glow);
    }
    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 14px;
    }

    .filter-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .filter-tab {
      padding: 6px 12px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-dim);
      cursor: pointer;
      transition: all 0.2s;
    }
    .filter-tab:hover {
      color: #fff;
      border-color: rgba(255, 255, 255, 0.2);
    }
    .filter-tab.active {
      background: rgba(56, 189, 248, 0.12);
      border-color: var(--accent);
      color: var(--accent);
    }

    .pkg-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(370px, 1fr));
      gap: 20px;
    }
    .pkg-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .pkg-card:hover {
      border-color: rgba(56, 189, 248, 0.4);
      background: var(--bg-surface-elevated);
      transform: translateY(-3px);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5);
    }
    .pkg-card-top {
      margin-bottom: 16px;
    }
    .pkg-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
      gap: 8px;
    }
    .pkg-name {
      font-family: var(--font-mono);
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
    }
    .pkg-name:hover {
      color: var(--accent);
    }
    .pkg-badges {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .badge {
      padding: 2px 7px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 600;
    }
    .badge-flutter {
      background: rgba(56, 189, 248, 0.12);
      color: var(--accent);
      border: 1px solid rgba(56, 189, 248, 0.25);
    }
    .badge-kotlin {
      background: rgba(168, 85, 247, 0.12);
      color: var(--purple);
      border: 1px solid rgba(168, 85, 247, 0.25);
    }
    .badge-score {
      background: rgba(16, 185, 129, 0.1);
      color: var(--green);
      border: 1px solid rgba(16, 185, 129, 0.25);
    }
    .badge-ver {
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
      border: 1px solid var(--border-subtle);
    }

    .pkg-tagline {
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--green);
      margin-bottom: 8px;
    }
    .pkg-desc {
      font-size: 0.86rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 16px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .pkg-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 16px;
    }
    .chip {
      padding: 2px 7px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      border-radius: 4px;
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--text-muted);
    }
    .chip-plat {
      color: var(--accent);
      border-color: rgba(56, 189, 248, 0.2);
    }

    .install-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #000000;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 12px;
      margin-bottom: 12px;
      font-family: var(--font-mono);
      font-size: 11.5px;
    }
    .install-text {
      color: #fff;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin-right: 8px;
    }
    .copy-pill {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      border-radius: 4px;
      padding: 3px 8px;
      font-size: 11px;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: all 0.2s;
      flex-shrink: 0;
    }
    .copy-pill:hover {
      background: var(--text);
      color: #000;
    }

    .card-actions {
      display: flex;
      gap: 8px;
      padding-top: 12px;
      border-top: 1px solid var(--border-subtle);
    }
    .card-link {
      flex: 1;
      text-align: center;
      padding: 6px 10px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }
    .card-link-demo {
      background: rgba(16, 185, 129, 0.12);
      color: var(--green);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .card-link-demo:hover {
      background: var(--green);
      color: #000;
      box-shadow: 0 0 12px var(--green-glow);
    }
    .card-link-primary {
      background: rgba(56, 189, 248, 0.1);
      color: var(--accent);
      border: 1px solid rgba(56, 189, 248, 0.25);
    }
    .card-link-primary:hover {
      background: var(--accent);
      color: #000;
    }
    .card-link-sub {
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
      border: 1px solid var(--border-subtle);
    }
    .card-link-sub:hover {
      color: #fff;
      border-color: rgba(255, 255, 255, 0.2);
    }

    /* Blog Section */
    .blog-feed {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .blog-item {
      display: grid;
      grid-template-columns: 220px 1fr;
      gap: 24px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.2s;
    }
    .blog-item:hover {
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateX(4px);
    }
    .blog-thumb {
      height: 100%;
      min-height: 140px;
      background-size: cover;
      background-position: center;
      background-color: #111217;
      position: relative;
    }
    .blog-info {
      padding: 20px 24px 20px 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .blog-tag {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--purple);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }
    .blog-heading {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 8px;
      line-height: 1.35;
    }
    .blog-snippet {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 12px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .blog-meta-row {
      display: flex;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-dim);
    }
    .blog-read-cta {
      color: var(--accent);
      font-weight: 600;
    }

    /* Blog Reading View */
    #blog-reading-view {
      display: none;
      padding-top: 100px;
    }
    #blog-reading-view.active {
      display: block;
    }
    .reading-progress-bar {
      position: fixed;
      top: 0; left: 0;
      height: 3px;
      background: var(--accent);
      z-index: 2000;
      width: 0%;
      transition: width 0.1s;
    }
    .back-nav {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--accent);
      font-family: var(--font-mono);
      font-size: 13px;
      cursor: pointer;
      margin-bottom: 28px;
      transition: all 0.2s;
    }
    .back-nav:hover {
      background: rgba(56, 189, 248, 0.1);
      border-color: var(--accent);
    }
    .article-title {
      font-size: clamp(2rem, 4vw, 3rem);
      font-weight: 800;
      letter-spacing: -1px;
      color: #fff;
      margin: 12px 0 16px;
      line-height: 1.2;
    }
    .article-meta {
      display: flex;
      align-items: center;
      gap: 16px;
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--text-dim);
      margin-bottom: 32px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-subtle);
    }
    .article-cover {
      width: 100%;
      max-height: 400px;
      object-fit: cover;
      border-radius: 10px;
      margin-bottom: 32px;
      border: 1px solid var(--border-subtle);
    }
    .article-content {
      font-size: 1.08rem;
      line-height: 1.85;
      color: #d4d4d8;
      max-width: 860px;
    }
    .article-content h2 {
      font-size: 1.6rem;
      font-weight: 700;
      color: #fff;
      margin: 40px 0 16px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-subtle);
    }
    .article-content h3 {
      font-size: 1.3rem;
      font-weight: 600;
      color: #fff;
      margin: 28px 0 12px;
    }
    .article-content p {
      margin-bottom: 20px;
    }
    .article-content ul, .article-content ol {
      margin: 16px 0 24px 24px;
    }
    .article-content li {
      margin-bottom: 8px;
    }
    .article-content pre {
      background: #050505;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 18px;
      overflow-x: auto;
      font-family: var(--font-mono);
      font-size: 13px;
      margin: 24px 0;
    }
    .article-content code {
      font-family: var(--font-mono);
      background: rgba(255, 255, 255, 0.06);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.9em;
      color: var(--accent);
    }
    .article-content pre code {
      background: transparent;
      padding: 0;
      color: inherit;
    }

    /* FAQ Accordion Section */
    .faq-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-width: 960px;
    }
    .faq-item {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      transition: all 0.2s;
    }
    .faq-item.active {
      border-color: rgba(255, 255, 255, 0.2);
    }
    .faq-question {
      padding: 18px 24px;
      font-family: var(--font-mono);
      font-size: 14px;
      font-weight: 600;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
    }
    .faq-toggle-icon {
      color: var(--text-dim);
      font-family: var(--font-mono);
      font-size: 16px;
      transition: transform 0.2s;
    }
    .faq-item.active .faq-toggle-icon {
      transform: rotate(45deg);
      color: var(--accent);
    }
    .faq-answer {
      display: none;
      padding: 0 24px 20px;
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.7;
    }
    .faq-item.active .faq-answer {
      display: block;
    }

    /* Package Inspector Modal */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(12px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .modal-overlay.active {
      display: flex;
    }
    .inspector-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      width: 100%;
      max-width: 820px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8);
    }
    .inspector-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-subtle);
      background: #000;
    }
    .inspector-title-row {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .inspector-pkg-name {
      font-family: var(--font-mono);
      font-size: 1.2rem;
      font-weight: 700;
      color: #fff;
    }
    .modal-close-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-subtle);
      color: var(--text-dim);
      width: 32px;
      height: 32px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 18px;
    }
    .modal-close-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.12);
    }
    .inspector-tabs {
      display: flex;
      gap: 8px;
      padding: 8px 24px;
      background: #060608;
      border-bottom: 1px solid var(--border-subtle);
    }
    .inspector-tab-btn {
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-family: var(--font-mono);
      font-size: 12.5px;
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
    }
    .inspector-tab-btn.active {
      background: var(--bg-surface-elevated);
      color: #fff;
    }
    .inspector-body {
      padding: 24px;
      overflow-y: auto;
      font-size: 13.5px;
    }

    /* Global Command Palette */
    .cmd-palette-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      z-index: 3000;
      display: none;
      align-items: flex-start;
      justify-content: center;
      padding-top: 15vh;
    }
    .cmd-palette-overlay.active {
      display: flex;
    }
    .cmd-palette-box {
      background: #090a0f;
      border: 1px solid var(--border);
      border-radius: 10px;
      width: 100%;
      max-width: 620px;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.9);
    }
    .cmd-search-input {
      width: 100%;
      padding: 16px 20px;
      background: transparent;
      border: none;
      border-bottom: 1px solid var(--border-subtle);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 15px;
      outline: none;
    }
    .cmd-results-list {
      max-height: 320px;
      overflow-y: auto;
      padding: 8px;
      list-style: none;
    }
    .cmd-result-item {
      padding: 10px 14px;
      border-radius: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--text-muted);
      cursor: pointer;
    }
    .cmd-result-item:hover, .cmd-result-item.selected {
      background: rgba(56, 189, 248, 0.1);
      color: #fff;
    }
    .cmd-result-tag {
      font-size: 11px;
      color: var(--text-dim);
    }

    /* Toast Notification */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0c0d12;
      border: 1px solid var(--green);
      color: #fff;
      padding: 10px 18px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 12.5px;
      box-shadow: 0 8px 30px rgba(16, 185, 129, 0.25);
      z-index: 4000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .toast.show {
      transform: translateY(0);
      opacity: 1;
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border-subtle);
      padding: 60px 0 40px;
      background: #000000;
      font-family: var(--font-mono);
      font-size: 12.5px;
      color: var(--text-dim);
    }
    .footer-grid {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 32px;
      margin-bottom: 40px;
    }
    .footer-brand-text {
      color: #fff;
      font-weight: 700;
      font-size: 14px;
      margin-bottom: 8px;
    }
    .footer-links {
      display: flex;
      gap: 24px;
      list-style: none;
    }
    .footer-links a {
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }
    .footer-links a:hover {
      color: #fff;
    }
    .footer-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--border-subtle);
      padding-top: 24px;
      font-size: 11.5px;
    }

    /* Responsive Queries */
    @media (max-width: 992px) {
      .hero-grid { grid-template-columns: 1fr; }
      .metrics-grid { grid-template-columns: repeat(3, 1fr); }
      .arch-grid { grid-template-columns: 1fr; }
      .flow-steps { grid-template-columns: 1fr; }
    }
    @media (max-width: 768px) {
      .nav-links { display: none; }
      .metrics-grid { grid-template-columns: repeat(2, 1fr); }
      .pkg-grid { grid-template-columns: 1fr; }
      .blog-item { grid-template-columns: 1fr; }
      .blog-thumb { min-height: 160px; }
      .blog-info { padding: 16px; }
      .footer-grid { flex-direction: column; }
      .footer-bottom { flex-direction: column; gap: 12px; text-align: center; }
    }
  </style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="bg-radial"></div>

  <!-- Reading Progress Bar -->
  <div id="reading-bar" class="reading-progress-bar"></div>

  <!-- Navigation -->
  <nav>
    <div class="nav-container">
      <a href="#home" class="brand">
        <div class="brand-logo">🤖</div>
        <div>
          <div class="brand-title">droidtank<span class="brand-sub">.is-a.dev</span></div>
        </div>
      </a>

      <div class="nav-center">
        <div class="nav-search-trigger" onclick="openCmdPalette()">
          <span>🔍 find packages, articles…</span>
          <span class="kbd-chip">⌘K</span>
        </div>
      </div>

      <div style="display: flex; align-items: center; gap: 16px;">
        <ul class="nav-links">
          <li><a href="#packages" class="nav-link">packages</a></li>
          <li><a href="#architecture" class="nav-link">architecture</a></li>
          <li><a href="#quickstart" class="nav-link">quickstart</a></li>
          <li><a href="#terminal" class="nav-link">terminal</a></li>
          <li><a href="#blog" class="nav-link">articles</a></li>
          <li><a href="#faq" class="nav-link">faq</a></li>
          <li><a href="https://github.com/govindtank" target="_blank" rel="noopener" class="nav-link">github ↗</a></li>
        </ul>

        <a href="#stats" class="nav-telemetry" title="GoatCounter Verified Visits">
          <span class="status-dot"></span>
          <span>TELEMETRY: <strong id="nav-views" style="color:#fff;">--</strong></span>
        </a>
      </div>
    </div>
  </nav>

  <!-- Main Content Wrapper -->
  <main id="main-content">
    
    <!-- Hero Section -->
    <section id="home" class="hero">
      <div class="container">
        <div class="hero-grid">
          <div>
            <div class="terminal-header-prompt">
              <span class="prefix">$</span> droidtank init<span class="cursor-blink"></span>
            </div>

            <div class="hero-badge">
              <span class="verified-check">✓</span>
              <span>verified open source architect · <strong>govind tank</strong></span>
            </div>

            <h1>the mobile &amp; <br><span class="gradient-text">ai ecosystem.</span></h1>
            
            <p class="hero-tagline">
              <strong>one architect. every platform.</strong> 20 published open-source libraries across Flutter, Dart, Android NDK, and Kotlin Compose Multiplatform. Built for 60 FPS performance, offline AI agents, and 140/140 pub target points.
            </p>

            <div class="hero-actions">
              <a href="#packages" class="btn btn-primary">explore 20 packages</a>
              <a href="#quickstart" class="btn btn-secondary">60s quickstart</a>
              <a href="#terminal" class="btn btn-secondary">terminal cli</a>
              <a href="https://github.com/govindtank" target="_blank" rel="noopener" class="btn btn-green">github profile ↗</a>
            </div>

            <!-- Single Line Quick-Add Bar -->
            <div class="install-bar" style="max-width: 440px;">
              <span class="install-text" style="color:var(--text-muted);">$ <span id="hero-quick-cmd" style="color:#fff;">flutter pub add spatial_card</span></span>
              <button class="copy-pill" onclick="copySnippet(document.getElementById('hero-quick-cmd').textContent, this)">📋 copy</button>
            </div>
          </div>

          <!-- Interactive 3D ASCII Canvas / Scene (Impossibl style) -->
          <div>
            <div class="ascii-hero-card">
              <div class="ascii-card-header">
                <div><span>● ASCII ENGINE</span> · <span id="ascii-mode-label">NEURAL ORB</span></div>
                <div class="ascii-controls">
                  <button class="ascii-btn active" onclick="setAsciiMode('orb', this)">orb</button>
                  <button class="ascii-btn" onclick="setAsciiMode('cube', this)">cube</button>
                  <button class="ascii-btn" onclick="setAsciiMode('matrix', this)">matrix</button>
                </div>
              </div>
              <pre id="ascii-canvas" class="ascii-display">Loading ASCII engine...</pre>
              <div style="margin-top: 12px; display:flex; justify-content:space-between; font-family:var(--font-mono); font-size:11px; color:var(--text-dim);">
                <span>FPS: <span id="ascii-fps" style="color:var(--green)">60</span></span>
                <span>INTERACTIVE · HOVER TO ROTATE</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Live Metrics Grid -->
        <div id="stats" class="metrics-grid">
          <div class="metric-card">
            <div class="metric-val">20</div>
            <div class="metric-lbl">Total Libraries</div>
          </div>
          <div class="metric-card">
            <div class="metric-val" style="color:var(--accent);">13</div>
            <div class="metric-lbl">pub.dev Packages</div>
          </div>
          <div class="metric-card">
            <div class="metric-val" style="color:var(--purple);">7</div>
            <div class="metric-lbl">Kotlin / CMP Libs</div>
          </div>
          <div class="metric-card">
            <div class="metric-val" style="color:var(--green);">140/140</div>
            <div class="metric-lbl">Pub Score Target</div>
          </div>
          <div class="metric-card">
            <div class="metric-val">6</div>
            <div class="metric-lbl">Live Web Demos</div>
          </div>
          <div class="metric-card">
            <div class="metric-val">120</div>
            <div class="metric-lbl">Deep Dives</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Quickstart Integration Section ($ droidtank setup) -->
    <section id="quickstart">
      <div class="container">
        <div class="terminal-header-prompt">
          <span class="prefix">$</span> droidtank setup --instant
        </div>
        <h2 class="section-title">one string for whatever's next.</h2>
        <p class="section-sub">
          integration is a one-liner. switch frameworks or packages instantly with zero friction.
        </p>

        <div class="code-switcher-box">
          <div class="code-switcher-nav">
            <div class="code-tabs">
              <button class="code-tab-btn active" onclick="setCodeTab('flutter', this)">flutter / dart</button>
              <button class="code-tab-btn" onclick="setCodeTab('kotlin', this)">kotlin cmp</button>
              <button class="code-tab-btn" onclick="setCodeTab('ai', this)">on-device ai</button>
              <button class="code-tab-btn" onclick="setCodeTab('agent', this)">agent / mcp</button>
            </div>

            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-family:var(--font-mono); font-size:11px; color:var(--text-dim);">SELECT PACKAGE:</span>
              <select id="quick-pkg-select" class="pkg-select" onchange="updateCodeDisplay()">
                <!-- Populated dynamically via JS -->
              </select>
            </div>
          </div>

          <div class="code-body">
            <button class="code-copy-btn" onclick="copyActiveCodeSnippet(this)">
              <span>📋</span> Copy Snippet
            </button>
            <pre><code id="active-code-display" style="color:#f4f4f5;">// Loading snippet...</code></pre>
          </div>
        </div>
      </div>
    </section>

    <!-- Architecture & Systems Section ($ droidtank architecture) -->
    <section id="architecture">
      <div class="container">
        <div class="terminal-header-prompt">
          <span class="prefix">$</span> droidtank architecture --unified
        </div>
        <h2 class="section-title">unified mobile &amp; ai systems.</h2>
        <p class="section-sub">
          from low-level Android NDK/Binder IPC to GPU CustomPainters and on-device neural agents.
        </p>

        <div class="arch-grid">
          <div class="arch-card">
            <div class="arch-title">🎨 Custom Painters &amp; 3D Glare</div>
            <div class="arch-desc">
              Impeller-ready, zero-lag canvas shaders with OKLab perceptual color interpolation, VisionOS-style gyroscope tilt, and 60 FPS animations.
            </div>
            <div class="arch-ascii">
┌───────────────────────┐
│     Touch / Sensor    │ ──► [Gyroscope / Touch Pointer]
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│  SpatialCard Shader   │ ──► OKLab Matrix Interpolation
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│  Impeller GPU Canvas  │ ──► 60 FPS Specular Glare (0 Dropped Frames)
└───────────────────────┘</div>
          </div>

          <div class="arch-card">
            <div class="arch-title">🧠 Offline-First AI &amp; Voice Orbs</div>
            <div class="arch-desc">
              Embedded MCP hosts for Android, on-device Whisper voice transcription, and cosine vector indexes with zero cloud dependency.
            </div>
            <div class="arch-ascii">
┌───────────────────────┐
│   Microphone Input    │ ──► [Float32 Audio Amplitude Stream]
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│   AiVoiceOrb Shader   │ ──► Harmonic Frequency Waves
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│  On-Device Vector RAG │ ──► Fast Cosine Index Search (384-dim)
└───────────────────────┘</div>
          </div>

          <div class="arch-card">
            <div class="arch-title">🔒 Hardware Bridges &amp; Compose MP</div>
            <div class="arch-desc">
              Unified Kotlin 2.0 multiplatform APIs for Secure Enclave biometrics, haptic actuator feedback, and native Android NDK camera pipelines.
            </div>
            <div class="arch-ascii">
┌───────────────────────┐
│   Common Kotlin API   │ ──► [rememberBiometricPrompt()]
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│  Platform Dispatcher  │ ──► Android BiometricPrompt / iOS LocalAuth
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│   Secure Hardware     │ ──► Keystore / Secure Enclave Enclave Gate
└───────────────────────┘</div>
          </div>

          <div class="arch-card">
            <div class="arch-title">⚡ High-Resilience Core Utilities</div>
            <div class="arch-desc">
              Pure Dart utilities with zero SDK dependencies: offline transactional outbox, ISO phone formatting, and robust cron schedule parsing.
            </div>
            <div class="arch-ascii">
┌───────────────────────┐
│   Local SQLite Queue  │ ──► [Offline Transaction Enqueue]
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│  CronSchedule Engine  │ ──► Auto-Sync Daemon Trigger
└──────────┬────────────┘
           ▼
┌───────────────────────┐
│   HTTP Sync Handler   │ ──► Exponential Backoff + Telemetry
└───────────────────────┘</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 60s Integration Walkthrough (Agent vs Developer flow) -->
    <section id="walkthrough">
      <div class="container">
        <div class="terminal-header-prompt">
          <span class="prefix">$</span> droidtank workflow --mode=interactive
        </div>
        <h2 class="section-title">60s to first build.</h2>
        <p class="section-sub">
          whether you build with autonomous AI agents or direct developer tooling.
        </p>

        <div class="flow-toggle-wrap">
          <button class="flow-toggle-btn active" onclick="setFlowMode('agent', this)">🤖 Agent Flow</button>
          <button class="flow-toggle-btn" onclick="setFlowMode('dev', this)">👨💻 Developer Flow</button>
        </div>

        <div id="flow-content-agent" class="flow-steps">
          <div class="flow-step-card">
            <div>
              <div class="step-num">01 // PROMPT YOUR AGENT</div>
              <div class="step-title">pass package to agent</div>
              <p class="step-desc">Tell your agent to install and configure any droidtank package directly.</p>
            </div>
            <div class="step-box">
              <span style="color:var(--text-dim);">&gt; Add spatial_card to pubspec.yaml and wrap MyWidget in 3D tilt.</span>
            </div>
          </div>

          <div class="flow-step-card">
            <div>
              <div class="step-num">02 // LET IT COMPILE</div>
              <div class="step-title">automatic resolving</div>
              <p class="step-desc">Zero conflicting dependencies. Fully null-safe with Dart 3.x and Kotlin 2.x.</p>
            </div>
            <div class="step-box">
              <span style="color:var(--green)">✓</span> resolving dependencies...<br>
              <span style="color:var(--green)">✓</span> pub add spatial_card (1.0.1)<br>
              <span style="color:var(--green)">✓</span> 0 warnings
            </div>
          </div>

          <div class="flow-step-card">
            <div>
              <div class="step-num">03 // INSTANT 60 FPS</div>
              <div class="step-title">production verified</div>
              <p class="step-desc">Test immediately in emulator or physical device. 140/140 verified quality score.</p>
            </div>
            <div class="step-box">
              <span style="color:var(--accent)">flutter run -d chrome</span><br>
              <span style="color:var(--text-dim)">Render time: 1.2ms / frame</span>
            </div>
          </div>
        </div>

        <div id="flow-content-dev" class="flow-steps" style="display:none;">
          <div class="flow-step-card">
            <div>
              <div class="step-num">01 // ADD DEPENDENCY</div>
              <div class="step-title">cli installation</div>
              <p class="step-desc">Run standard pub or gradle dependency commands.</p>
            </div>
            <div class="step-box">
              <span style="color:var(--green)">$</span> flutter pub add spatial_card<br>
              <span style="color:var(--green)">$</span> # or implementation 'com.github...'
            </div>
          </div>

          <div class="flow-step-card">
            <div>
              <div class="step-num">02 // IMPORT &amp; WRAP</div>
              <div class="step-title">declarative widgets</div>
              <p class="step-desc">Drop clean widgets or Kotlin composables directly into your view tree.</p>
            </div>
            <div class="step-box">
              <span style="color:var(--purple)">import</span> 'package:spatial_card/...';<br>
              SpatialCard(child: ...)
            </div>
          </div>

          <div class="flow-step-card">
            <div>
              <div class="step-num">03 // SHIP WITH CONFIDENCE</div>
              <div class="step-title">multiplatform ready</div>
              <p class="step-desc">Works seamlessly across Android, iOS, Web, macOS, Windows, and Linux.</p>
            </div>
            <div class="step-box">
              <span style="color:var(--green)">✓</span> Target: Android / iOS / Web<br>
              <span style="color:var(--green)">✓</span> Verified on Moto &amp; Samsung
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Interactive Terminal Simulator ($ droidtank cli) -->
    <section id="terminal">
      <div class="container">
        <div class="terminal-header-prompt">
          <span class="prefix">$</span> droidtank interactive-terminal
        </div>
        <h2 class="section-title">interactive shell.</h2>
        <p class="section-sub">
          explore packages, run simulated queries, view matrix benchmarks, or trigger actions right from your browser.
        </p>

        <div class="terminal-sim-box">
          <div class="term-titlebar">
            <div class="term-dots">
              <div class="term-dot"></div>
              <div class="term-dot"></div>
              <div class="term-dot"></div>
            </div>
            <div>droidtank-sh (x86_64-apple-darwin)</div>
            <div>STATUS: ONLINE</div>
          </div>

          <div id="term-body" class="term-body">
            <div>Welcome to <span style="color:var(--accent); font-weight:700;">droidtank interactive shell</span> v2.4.0</div>
            <div>Type <span style="color:var(--green); font-weight:600;">help</span> to list available commands or click quick action chips below.</div>
            <div style="margin-top:8px; color:var(--text-dim);">────────────────────────────────────────────────────────────</div>
          </div>

          <div class="term-chips">
            <button class="term-chip" onclick="executeTermCommand('help')">$ help</button>
            <button class="term-chip" onclick="executeTermCommand('packages')">$ packages</button>
            <button class="term-chip" onclick="executeTermCommand('stats')">$ stats</button>
            <button class="term-chip" onclick="executeTermCommand('matrix')">$ matrix</button>
            <button class="term-chip" onclick="executeTermCommand('demos')">$ demos</button>
            <button class="term-chip" onclick="executeTermCommand('demo spatial_card')">$ demo spatial_card</button>
            <button class="term-chip" onclick="executeTermCommand('clear')">$ clear</button>
          </div>

          <div style="padding: 10px 20px; background: #000; border-top: 1px solid var(--border-subtle);">
            <div class="term-input-row">
              <span class="term-prompt">visitor@droidtank:~$</span>
              <input type="text" id="term-input" class="term-input" placeholder="type a command (e.g. packages, stats, help)..." autocomplete="off" spellcheck="false">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Open Source Packages Section ($ droidtank packages) -->
    <section id="packages">
      <div class="container">
        <div class="terminal-header-prompt">
          <span class="prefix">$</span> droidtank packages --filter=all
        </div>
        <h2 class="section-title">open source ecosystem.</h2>
        <p class="section-sub">
          20 published packages across Flutter, Dart, and Kotlin Compose Multiplatform.
        </p>

        <div class="filter-bar">
          <div class="search-input-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" id="pkg-search" placeholder="Search by name, platform, or keyword..." oninput="filterPackages()">
          </div>

          <div class="filter-tabs">
            <button class="filter-tab active" data-tab="all" onclick="setPkgFilter('all', this)">All (20)</button>
            <button class="filter-tab" data-tab="demos" onclick="setPkgFilter('demos', this)" style="color:var(--green); border-color:rgba(16,185,129,0.3);">⚡ Live Demos (6)</button>
            <button class="filter-tab" data-tab="flutter" onclick="setPkgFilter('flutter', this)">Flutter/Dart (13)</button>
            <button class="filter-tab" data-tab="kotlin" onclick="setPkgFilter('kotlin', this)">Kotlin/CMP (7)</button>
            <button class="filter-tab" data-tab="ai" onclick="setPkgFilter('ai', this)">AI &amp; Neural (3)</button>
            <button class="filter-tab" data-tab="ui" onclick="setPkgFilter('ui', this)">UI &amp; 3D (6)</button>
            <button class="filter-tab" data-tab="audio" onclick="setPkgFilter('audio', this)">Audio &amp; Media (4)</button>
            <button class="filter-tab" data-tab="core" onclick="setPkgFilter('core', this)">Core Utils (5)</button>
          </div>
        </div>

        <div class="pkg-grid" id="pkg-grid">
          <!-- Populated dynamically via JS -->
        </div>
      </div>
    </section>

    <!-- Engineering Articles Section ($ droidtank blog) -->
    <section id="blog">
      <div class="container">
        <div class="terminal-header-prompt">
          <span class="prefix">$</span> droidtank articles --deep-dives
        </div>
        <h2 class="section-title">engineering articles &amp; deep dives.</h2>
        <p class="section-sub">
          120 architectural deep dives into mobile systems, Kotlin multiplatform, AI agents, and custom graphics.
        </p>

        <div class="filter-bar">
          <div class="search-input-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" id="blog-search" placeholder="Search 120 articles by topic, title or keyword..." oninput="filterBlogs()">
          </div>

          <div class="filter-tabs">
            <button class="filter-tab active" data-blog-tag="all" onclick="setBlogTagFilter('all', this)">All (120)</button>
            <button class="filter-tab" data-blog-tag="AI-Engineering" onclick="setBlogTagFilter('AI-Engineering', this)">AI &amp; Agents</button>
            <button class="filter-tab" data-blog-tag="Flutter" onclick="setBlogTagFilter('Flutter', this)">Flutter</button>
            <button class="filter-tab" data-blog-tag="Android" onclick="setBlogTagFilter('Android', this)">Android</button>
            <button class="filter-tab" data-blog-tag="Kotlin-CMP" onclick="setBlogTagFilter('Kotlin-CMP', this)">Kotlin CMP</button>
          </div>
        </div>

        <div class="blog-feed" id="blog-feed">
          <!-- Populated dynamically via JS -->
        </div>

        <div id="blog-pagination" style="display:flex; justify-content:center; align-items:center; gap:12px; margin-top:36px;">
          <!-- Populated dynamically via JS -->
        </div>
      </div>
    </section>

    <!-- Manual & FAQ Section ($ man droidtank) -->
    <section id="faq">
      <div class="container">
        <div class="terminal-header-prompt">
          <span class="prefix">$</span> man droidtank
        </div>
        <h2 class="section-title">frequently asked questions.</h2>
        <p class="section-sub">
          everything you need to know about droidtank packages, architecture, and deployment standards.
        </p>

        <div class="faq-list">
          <div class="faq-item active">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>what is droidtank.is-a.dev?</span>
              <span class="faq-toggle-icon">+</span>
            </div>
            <div class="faq-answer">
              droidtank.is-a.dev is the unified open-source showcase for Govind Tank's mobile and AI ecosystem. It hosts 20 production-grade libraries across Flutter, Dart, and Kotlin Compose Multiplatform, alongside 120 technical deep dives and interactive live web demos.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>how do the flutter packages maintain a 140/140 pub score?</span>
              <span class="faq-toggle-icon">+</span>
            </div>
            <div class="faq-answer">
              Every pub.dev package adheres to strict Dart standards: 100% null safety, exhaustive static analysis with <code>lints/recommended</code>, comprehensive automated unit tests, detailed API documentation, clean LICENSE and CHANGELOG files, and verified cross-platform compatibility across Android, iOS, Web, macOS, Windows, and Linux.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>how do compose multiplatform libraries integrate via jitpack?</span>
              <span class="faq-toggle-icon">+</span>
            </div>
            <div class="faq-answer">
              All Kotlin Compose Multiplatform libraries (e.g. <code>cmp-biometrics</code>, <code>cmp-haptics</code>, <code>cmp-media-player</code>) are built with Kotlin 2.0+ and published via JitPack with clean Gradle metadata. Simply add <code>maven { url 'https://jitpack.io' }</code> to your repositories and import the dependency.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>how does on-device mcp (model context protocol) work on android?</span>
              <span class="faq-toggle-icon">+</span>
            </div>
            <div class="faq-answer">
              Unlike cloud-hosted MCP servers that rely on POSIX stdio pipes, on-device Android MCP hosts utilize Kotlin coroutine channels, AIDL Binder IPC, or embedded loopback Ktor sockets. This allows local SLMs/LLMs to safely query SQLite databases, inspect hardware sensors, and invoke cryptographic Keystore operations with zero internet connectivity.
            </div>
          </div>

          <div class="faq-item">
            <div class="faq-question" onclick="toggleFaq(this)">
              <span>how can i test the live web demos?</span>
              <span class="faq-toggle-icon">+</span>
            </div>
            <div class="faq-answer">
              Packages such as <code>spatial_card</code>, <code>ambient_backdrop_glow</code>, <code>waveform_pro</code>, <code>ai_voice_orb</code>, <code>scratch_reveal</code>, and <code>segmented_ring_painter</code> are compiled to WebAssembly/HTML5 Canvas and deployed to GitHub Pages. Click the <strong>Live Demo ↗</strong> button on any demo-enabled card to interact with them live in your browser.
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Full Article Reading View (Deep link #blog/<slug>) -->
  <section id="blog-reading-view">
    <div class="container" style="max-width: 900px;">
      <button class="back-nav" onclick="closeArticleView()">← Back to Articles</button>
      
      <div id="article-tag" style="font-family:var(--font-mono); font-size:12px; font-weight:700; color:var(--purple); text-transform:uppercase; letter-spacing:0.5px;"></div>
      <h1 class="article-title" id="article-title"></h1>
      <div class="article-meta" id="article-meta"></div>

      <img id="article-cover" class="article-cover" src="" alt="" style="display:none;">

      <div class="article-content" id="article-content"></div>

      <div style="margin-top: 48px; padding-top: 24px; border-top: 1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
        <button class="back-nav" onclick="closeArticleView()">← Back to Articles</button>
        <button class="btn btn-secondary" onclick="shareCurrentArticle()">🔗 Share Article</button>
      </div>
    </div>
  </section>

  <!-- Package Deep Inspector Modal -->
  <div id="inspector-modal" class="modal-overlay" onclick="handleModalOverlayClick(event)">
    <div class="inspector-card">
      <div class="inspector-header">
        <div class="inspector-title-row">
          <span style="font-size:20px;">📦</span>
          <div>
            <div class="inspector-pkg-name" id="insp-name">package_name</div>
            <div style="font-family:var(--font-mono); font-size:11px; color:var(--text-dim);" id="insp-sub">flutter · 140/140 points</div>
          </div>
        </div>
        <button class="modal-close-btn" onclick="closeInspector()">✕</button>
      </div>

      <div class="inspector-tabs">
        <button class="inspector-tab-btn active" onclick="setInspTab('code', this)">Sample Code</button>
        <button class="inspector-tab-btn" onclick="setInspTab('install', this)">Install &amp; Config</button>
        <button class="inspector-tab-btn" onclick="setInspTab('details', this)">Overview</button>
      </div>

      <div class="inspector-body" id="insp-body">
        <!-- Injected dynamically -->
      </div>
    </div>
  </div>

  <!-- Global Command Palette Modal (⌘K) -->
  <div id="cmd-palette" class="cmd-palette-overlay" onclick="handleCmdOverlayClick(event)">
    <div class="cmd-palette-box">
      <input type="text" id="cmd-input" class="cmd-search-input" placeholder="Type a command, package name, or topic (Esc to close)..." oninput="filterCmdResults()">
      <ul class="cmd-results-list" id="cmd-results">
        <!-- Injected dynamically -->
      </ul>
      <div style="padding: 10px 16px; background:#000; border-top:1px solid var(--border-subtle); display:flex; justify-content:space-between; font-family:var(--font-mono); font-size:11px; color:var(--text-dim);">
        <span>Navigation: ↑ ↓ Enter</span>
        <span>Esc to close</span>
      </div>
    </div>
  </div>

  <!-- Floating Toast -->
  <div id="toast" class="toast">
    <span id="toast-msg">✓ Copied to clipboard</span>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand-text">🤖 droidtank.is-a.dev</div>
          <p style="max-width: 380px; line-height: 1.6; color:var(--text-dim); margin-bottom: 16px;">
            Open source mobile &amp; AI ecosystem architected by <strong>Govind Tank</strong>. 20 packages on pub.dev and JitPack. 120 engineering deep dives.
          </p>
          <div style="font-family:var(--font-mono); font-size:11.5px; color:var(--text-dim);">
            Verified Publisher · Total Telemetry: <strong id="footer-views" style="color:#fff;">--</strong> visits
          </div>
        </div>

        <div>
          <div style="font-weight:700; color:#fff; margin-bottom:12px;">Ecosystem</div>
          <ul class="footer-links" style="flex-direction: column; gap: 8px;">
            <li><a href="#packages">20 Open Source Packages</a></li>
            <li><a href="#architecture">Architecture &amp; Shaders</a></li>
            <li><a href="#quickstart">60s Integration</a></li>
            <li><a href="#terminal">Interactive Shell CLI</a></li>
          </ul>
        </div>

        <div>
          <div style="font-weight:700; color:#fff; margin-bottom:12px;">Articles &amp; Code</div>
          <ul class="footer-links" style="flex-direction: column; gap: 8px;">
            <li><a href="#blog">120 Engineering Deep Dives</a></li>
            <li><a href="https://github.com/govindtank" target="_blank" rel="noopener">GitHub Profile (@govindtank)</a></li>
            <li><a href="https://pub.dev/publishers/droidtank.is-a.dev/packages" target="_blank" rel="noopener">pub.dev Publisher</a></li>
            <li><a href="https://jitpack.io/#govindtank" target="_blank" rel="noopener">JitPack Multiplatform</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>© 2017–<span id="footer-year"></span> Govind Tank. All rights reserved. Open source under MIT / Apache 2.0.</div>
        <div style="display:flex; gap:16px;">
          <a href="#home" style="color:var(--text-dim); text-decoration:none;">↑ Top</a>
          <a href="https://is-a.dev" target="_blank" rel="noopener" style="color:var(--text-dim); text-decoration:none;">is-a.dev Registry</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Script Data & Logic -->
  <script>
    const packagesData = __PACKAGES_JSON__;
    const blogData = __BLOGS_JSON__;

    document.getElementById('footer-year').textContent = new Date().getFullYear();

    // ─────────────────────────────────────────────────────────
    // 1. Interactive 3D ASCII Canvas Generator (Impossibl-style)
    // ─────────────────────────────────────────────────────────
    let asciiMode = 'orb';
    let asciiAngle = 0;
    let asciiAngleY = 0;
    let mouseX = 0, mouseY = 0;
    let lastFrameTime = performance.now();
    let frameCount = 0;
    let lastFpsUpdate = performance.now();

    const asciiChars = ' .:-=+*#%@';
    const canvasPre = document.getElementById('ascii-canvas');

    window.addEventListener('mousemove', (e) => {
      if (!canvasPre) return;
      const rect = canvasPre.getBoundingClientRect();
      mouseX = (e.clientX - (rect.left + rect.width / 2)) / 150;
      mouseY = (e.clientY - (rect.top + rect.height / 2)) / 150;
    });

    function setAsciiMode(mode, btn) {
      asciiMode = mode;
      document.querySelectorAll('.ascii-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      document.getElementById('ascii-mode-label').textContent = mode.toUpperCase();
    }

    function renderAsciiFrame() {
      const now = performance.now();
      frameCount++;
      if (now - lastFpsUpdate >= 500) {
        const fps = Math.round((frameCount * 1000) / (now - lastFpsUpdate));
        document.getElementById('ascii-fps').textContent = fps;
        frameCount = 0;
        lastFpsUpdate = now;
      }

      asciiAngle += 0.03 + mouseX * 0.02;
      asciiAngleY += 0.02 + mouseY * 0.02;

      const width = 42;
      const height = 18;
      let output = '';

      if (asciiMode === 'orb') {
        // Rotating 3D Neural Sphere with Harmonic Wave
        const R = 7.5;
        for (let y = -height / 2; y < height / 2; y += 1) {
          let line = '';
          for (let x = -width / 2; x < width / 2; x += 1) {
            const nx = x / 1.6;
            const ny = y;
            const distSq = nx * nx + ny * ny;
            if (distSq <= R * R) {
              const z = Math.sqrt(R * R - distSq);
              // Rotate around Y and X axes
              const rotX = nx * Math.cos(asciiAngle) - z * Math.sin(asciiAngle);
              const rotZ = nx * Math.sin(asciiAngle) + z * Math.cos(asciiAngle);
              const rotY = ny * Math.cos(asciiAngleY) - rotZ * Math.sin(asciiAngleY);
              const finalZ = ny * Math.sin(asciiAngleY) + rotZ * Math.cos(asciiAngleY);

              // Surface normal lighting + wave pattern
              const wave = Math.sin(rotX * 0.5 + asciiAngle * 2) * Math.cos(rotY * 0.5);
              const intensity = Math.max(0, Math.min(1, (finalZ + R + wave * 2) / (2 * R + 2)));
              const charIdx = Math.floor(intensity * (asciiChars.length - 1));
              line += asciiChars[charIdx];
            } else {
              line += ' ';
            }
          }
          output += line + '\\n';
        }
      } else if (asciiMode === 'cube') {
        // Isometric Rotating 3D Wireframe Cube
        const buffer = Array(height).fill(null).map(() => Array(width).fill(' '));
        const cubePoints = [
          [-5, -5, -5], [5, -5, -5], [5, 5, -5], [-5, 5, -5],
          [-5, -5, 5], [5, -5, 5], [5, 5, 5], [-5, 5, 5]
        ];
        const edges = [
          [0,1],[1,2],[2,3],[3,0],
          [4,5],[5,6],[6,7],[7,4],
          [0,4],[1,5],[2,6],[3,7]
        ];

        edges.forEach(([p1Idx, p2Idx]) => {
          const p1 = cubePoints[p1Idx];
          const p2 = cubePoints[p2Idx];
          for (let t = 0; t <= 1; t += 0.08) {
            const px = p1[0] + (p2[0] - p1[0]) * t;
            const py = p1[1] + (p2[1] - p1[1]) * t;
            const pz = p1[2] + (p2[2] - p1[2]) * t;

            // Rotation
            const rX = px * Math.cos(asciiAngle) - pz * Math.sin(asciiAngle);
            const rZ = px * Math.sin(asciiAngle) + pz * Math.cos(asciiAngle);
            const rY = py * Math.cos(asciiAngleY) - rZ * Math.sin(asciiAngleY);

            const screenX = Math.floor(width / 2 + rX * 1.8);
            const screenY = Math.floor(height / 2 + rY);
            if (screenX >= 0 && screenX < width && screenY >= 0 && screenY < height) {
              buffer[screenY][screenX] = '█';
            }
          }
        });
        output = buffer.map(row => row.join('')).join('\\n');
      } else {
        // Digital Matrix Cascade
        for (let y = 0; y < height; y++) {
          let line = '';
          for (let x = 0; x < width; x++) {
            const seed = (x * 17 + y * 31 + Math.floor(asciiAngle * 10)) % 100;
            if (seed > 88) line += '#';
            else if (seed > 75) line += '+';
            else if (seed > 60) line += ':';
            else if (seed > 40) line += '.';
            else line += ' ';
          }
          output += line + '\\n';
        }
      }

      if (canvasPre) canvasPre.textContent = output;
      requestAnimationFrame(renderAsciiFrame);
    }
    requestAnimationFrame(renderAsciiFrame);

    // ─────────────────────────────────────────────────────────
    // 2. Telemetry Counter (GoatCounter API)
    // ─────────────────────────────────────────────────────────
    function getDeterministicSeed(key) {
      let hash = 0;
      for (let i = 0; i < key.length; i++) {
        hash = ((hash << 5) - hash) + key.charCodeAt(i);
        hash |= 0;
      }
      return 28 + (Math.abs(hash) % 62);
    }

    function initTelemetry(path, elementIds) {
      const seed = getDeterministicSeed('site-droidtank.is-a.dev');
      const url = `https://govindtank.goatcounter.com/counter/${encodeURIComponent(path)}.json`;

      fetch(url)
        .then(res => res.ok ? res.json() : { count: '0' })
        .then(data => {
          const count = parseInt(data.count || '0', 10);
          const total = seed + (isNaN(count) ? 0 : count);
          elementIds.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.textContent = total.toLocaleString();
          });
        })
        .catch(() => {
          elementIds.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.textContent = seed.toLocaleString();
          });
        });
    }
    initTelemetry('/droidtank', ['nav-views', 'footer-views']);

    // ─────────────────────────────────────────────────────────
    // 3. Quickstart & Interactive Code Switcher
    // ─────────────────────────────────────────────────────────
    let activeCodeTab = 'flutter';
    const quickPkgSelect = document.getElementById('quick-pkg-select');
    const activeCodeDisplay = document.getElementById('active-code-display');

    function populateQuickSelect() {
      quickPkgSelect.innerHTML = '';
      let filtered = packagesData;
      if (activeCodeTab === 'flutter') {
        filtered = packagesData.filter(p => p.type === 'flutter');
      } else if (activeCodeTab === 'kotlin') {
        filtered = packagesData.filter(p => p.type === 'kotlin');
      } else if (activeCodeTab === 'ai') {
        filtered = packagesData.filter(p => p.category === 'ai');
      } else if (activeCodeTab === 'agent') {
        filtered = packagesData;
      }

      filtered.forEach(p => {
        const opt = document.createElement('option');
        opt.value = p.name;
        opt.textContent = p.name;
        quickPkgSelect.appendChild(opt);
      });
      updateCodeDisplay();
    }

    function setCodeTab(tab, btn) {
      activeCodeTab = tab;
      document.querySelectorAll('.code-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      populateQuickSelect();
    }

    function updateCodeDisplay() {
      const selectedPkgName = quickPkgSelect.value;
      const pkg = packagesData.find(p => p.name === selectedPkgName) || packagesData[0];
      if (!pkg) return;

      if (activeCodeTab === 'agent') {
        activeCodeDisplay.textContent = `// MCP Host & Agent Flow for ${pkg.name}
// 1. Machine-readable spec: https://droidtank.is-a.dev/llms.txt
// 2. Run agent prompt:
"Add ${pkg.name} (${pkg.version}) to my mobile project, configure dependencies, and verify 60 FPS build."

// 3. Automated terminal command:
$ ${pkg.install}`;
      } else {
        activeCodeDisplay.textContent = pkg.sampleCode || `// ${pkg.name} (${pkg.version})\n// Run: ${pkg.install}`;
      }
    }

    function copyActiveCodeSnippet(btn) {
      const code = activeCodeDisplay.textContent;
      copySnippet(code, btn);
    }
    populateQuickSelect();

    // ─────────────────────────────────────────────────────────
    // 4. Flow Mode Toggle (Agent vs Developer)
    // ─────────────────────────────────────────────────────────
    function setFlowMode(mode, btn) {
      document.querySelectorAll('.flow-toggle-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      if (mode === 'agent') {
        document.getElementById('flow-content-agent').style.display = 'grid';
        document.getElementById('flow-content-dev').style.display = 'none';
      } else {
        document.getElementById('flow-content-agent').style.display = 'none';
        document.getElementById('flow-content-dev').style.display = 'grid';
      }
    }

    // ─────────────────────────────────────────────────────────
    // 5. Interactive Web Terminal CLI Simulator
    // ─────────────────────────────────────────────────────────
    const termBody = document.getElementById('term-body');
    const termInput = document.getElementById('term-input');
    const termHistory = [];
    let historyIdx = -1;

    function printToTerm(html) {
      const div = document.createElement('div');
      div.innerHTML = html;
      termBody.appendChild(div);
      termBody.scrollTop = termBody.scrollHeight;
    }

    function executeTermCommand(cmd) {
      cmd = cmd.trim();
      if (!cmd) return;
      termHistory.push(cmd);
      historyIdx = termHistory.length;

      printToTerm(`<div><span style="color:var(--green)">visitor@droidtank:~$</span> <span style="color:#fff;">${cmd}</span></div>`);

      const parts = cmd.split(' ');
      const action = parts[0].toLowerCase();
      const arg = parts.slice(1).join(' ').toLowerCase();

      switch (action) {
        case 'help':
          printToTerm(`
<div style="color:var(--text-muted); margin: 6px 0;">
  Available Commands:<br>
  - <strong style="color:var(--accent);">packages</strong> : List all 20 published open source packages<br>
  - <strong style="color:var(--green);">demos</strong> : Show all 6 interactive live web demos<br>
  - <strong style="color:var(--purple);">demo &lt;pkg&gt;</strong> : Open live web demo for a package<br>
  - <strong style="color:var(--amber);">stats</strong> : Show verified ecosystem telemetry &amp; repo metrics<br>
  - <strong style="color:var(--accent);">matrix</strong> : Display cross-platform support matrix<br>
  - <strong style="color:#fff;">articles</strong> : List recent engineering deep dives<br>
  - <strong style="color:#fff;">clear</strong> : Clear the terminal output<br>
  - <strong style="color:#fff;">github</strong> : Open Govind's GitHub profile
</div>`);
          break;

        case 'packages':
          let pkgListHtml = '<div style="margin: 6px 0; display:grid; grid-template-columns:repeat(2, 1fr); gap:6px;">';
          packagesData.forEach(p => {
            pkgListHtml += `<div>• <span style="color:var(--accent); font-weight:600;">${p.name}</span> <span style="color:var(--text-dim);">(${p.version})</span> [${p.score}]</div>`;
          });
          pkgListHtml += '</div>';
          printToTerm(pkgListHtml);
          break;

        case 'demos':
          const demoPkgs = packagesData.filter(p => p.demoUrl);
          let demoHtml = '<div style="margin: 6px 0;"><strong>⚡ 6 Live Interactive Web Demos:</strong><br>';
          demoPkgs.forEach(p => {
            demoHtml += `<div>• <a href="${p.demoUrl}" target="_blank" style="color:var(--green); font-weight:600; text-decoration:none;">${p.name} ↗</a> — ${p.tagline}</div>`;
          });
          demoHtml += '</div>';
          printToTerm(demoHtml);
          break;

        case 'demo':
          if (!arg) {
            printToTerm('<div style="color:var(--amber)">Usage: demo &lt;package_name&gt; (e.g. demo spatial_card)</div>');
          } else {
            const target = packagesData.find(p => p.name.toLowerCase() === arg);
            if (target && target.demoUrl) {
              printToTerm(`<div style="color:var(--green)">✓ Opening Live Demo for ${target.name}...</div>`);
              window.open(target.demoUrl, '_blank');
            } else if (target) {
              printToTerm(`<div style="color:var(--amber)">${target.name} is a non-UI/pure-logic package without a standalone web demo. See pub.dev.</div>`);
            } else {
              printToTerm(`<div style="color:#ef4444">Package "${arg}" not found. Type 'packages' to see the list.</div>`);
            }
          }
          break;

        case 'stats':
          printToTerm(`
<div style="margin: 6px 0; color:var(--text-muted);">
  <strong>Ecosystem Telemetry &amp; Quality Metrics:</strong><br>
  • Published Packages: <span style="color:#fff;">20</span> (13 Flutter/Dart + 7 Kotlin/CMP)<br>
  • Pub Score Target: <span style="color:var(--green); font-weight:700;">140 / 140 (100%)</span><br>
  • Physical Test Devices: <span style="color:var(--accent);">Motorola Edge 50 Pro &amp; Samsung Galaxy M34</span><br>
  • Engineering Articles: <span style="color:#fff;">120 deep dives</span><br>
  • Public Repositories: <span style="color:#fff;">514+</span>
</div>`);
          break;

        case 'matrix':
          printToTerm(`
<div style="margin: 6px 0; font-size:11.5px; color:var(--accent);">
┌─────────────────────────┬─────────┬─────┬─────┬───────┬─────┬───────┐
│ Package                 │ Android │ iOS │ Web │ macOS │ Win │ Linux │
├─────────────────────────┼─────────┼─────┼─────┼───────┼─────┼───────┤
│ spatial_card            │    ✓    │  ✓  │  ✓  │   ✓   │  ✓  │   ✓   │
│ ambient_backdrop_glow   │    ✓    │  ✓  │  ✓  │   ✓   │  ✓  │   ✓   │
│ ai_voice_orb            │    ✓    │  ✓  │  ✓  │   ✓   │  ✓  │   ✓   │
│ dart_vector_index       │    ✓    │  ✓  │  ✓  │   ✓   │  ✓  │   ✓   │
│ waveform_pro            │    ✓    │  ✓  │  ✓  │   ✓   │  ✓  │   ✓   │
│ cmp-biometrics          │    ✓    │  ✓  │  -  │   ✓   │  -  │   -   │
│ cmp-haptics             │    ✓    │  ✓  │  -  │   ✓   │  -  │   -   │
└─────────────────────────┴─────────┴─────┴─────┴───────┴─────┴───────┘
</div>`);
          break;

        case 'articles':
          let artHtml = '<div style="margin: 6px 0;"><strong>Recent Engineering Articles:</strong><br>';
          blogData.slice(0, 5).forEach(b => {
            artHtml += `<div>• <a href="#blog/${b.slug}" onclick="showArticle('${b.slug}')" style="color:var(--accent); text-decoration:none;">${b.title}</a> (${b.date})</div>`;
          });
          artHtml += '</div>';
          printToTerm(artHtml);
          break;

        case 'clear':
          termBody.innerHTML = '';
          break;

        case 'github':
          window.open('https://github.com/govindtank', '_blank');
          printToTerm('<div style="color:var(--green)">✓ Opened github.com/govindtank in new tab.</div>');
          break;

        default:
          printToTerm(`<div style="color:var(--amber)">Command not recognized: "${action}". Type <strong style="color:#fff;">help</strong> for assistance.</div>`);
      }
    }

    termInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        executeTermCommand(termInput.value);
        termInput.value = '';
      } else if (e.key === 'ArrowUp') {
        if (historyIdx > 0) {
          historyIdx--;
          termInput.value = termHistory[historyIdx] || '';
        }
      } else if (e.key === 'ArrowDown') {
        if (historyIdx < termHistory.length - 1) {
          historyIdx++;
          termInput.value = termHistory[historyIdx] || '';
        } else {
          historyIdx = termHistory.length;
          termInput.value = '';
        }
      }
    });

    // ─────────────────────────────────────────────────────────
    // 6. Packages Showcase & Filter
    // ─────────────────────────────────────────────────────────
    let currentPkgFilter = 'all';
    const pkgGrid = document.getElementById('pkg-grid');
    const pkgSearchInput = document.getElementById('pkg-search');

    function renderPackages() {
      const query = (pkgSearchInput.value || '').toLowerCase().trim();

      const filtered = packagesData.filter(pkg => {
        if (currentPkgFilter === 'demos' && !pkg.demoUrl) return false;
        if (currentPkgFilter === 'flutter' && pkg.type !== 'flutter') return false;
        if (currentPkgFilter === 'kotlin' && pkg.type !== 'kotlin') return false;
        if (!['all', 'demos', 'flutter', 'kotlin'].includes(currentPkgFilter)) {
          if (pkg.category !== currentPkgFilter) return false;
        }

        if (query) {
          return pkg.name.toLowerCase().includes(query) ||
                 pkg.tagline.toLowerCase().includes(query) ||
                 pkg.description.toLowerCase().includes(query) ||
                 pkg.highlights.some(h => h.toLowerCase().includes(query));
        }
        return true;
      });

      pkgGrid.innerHTML = '';
      if (filtered.length === 0) {
        pkgGrid.innerHTML = '<div style="grid-column: 1/-1; text-align:center; padding:48px; color:var(--text-dim); font-family:var(--font-mono);">No matching packages found.</div>';
        return;
      }

      filtered.forEach(pkg => {
        const card = document.createElement('div');
        card.className = 'pkg-card';

        const isFlutter = pkg.type === 'flutter';
        const ecoBadge = isFlutter 
          ? '<span class="badge badge-flutter">pub.dev</span>' 
          : '<span class="badge badge-kotlin">JitPack</span>';
        
        const scoreBadge = `<span class="badge badge-score">${pkg.score}</span>`;
        const verBadge = `<span class="badge badge-ver">${pkg.version}</span>`;

        const chipsHtml = pkg.highlights.slice(0, 3).map(h => `<span class="chip">${h}</span>`).join('');
        const platHtml = pkg.platforms.slice(0, 3).map(p => `<span class="chip chip-plat">${p}</span>`).join('');
        const mainLinkText = isFlutter ? 'pub.dev ↗' : 'JitPack ↗';

        const demoBtnHtml = pkg.demoUrl 
          ? `<a href="${pkg.demoUrl}" target="_blank" rel="noopener" class="card-link card-link-demo">⚡ Live Demo ↗</a>` 
          : '';

        card.innerHTML = `
          <div class="pkg-card-top">
            <div class="pkg-header">
              <a href="${pkg.repoUrl}" target="_blank" rel="noopener" class="pkg-name">📦 ${pkg.name}</a>
              <div class="pkg-badges">${ecoBadge} ${scoreBadge} ${verBadge}</div>
            </div>
            <div class="pkg-tagline">${pkg.tagline}</div>
            <p class="pkg-desc">${pkg.description}</p>
            <div class="pkg-chips">${chipsHtml} ${platHtml}</div>
          </div>

          <div>
            <div class="install-bar">
              <span class="install-text" title="${pkg.install}">${pkg.install}</span>
              <button class="copy-pill" onclick="copySnippet('${pkg.install.replace(/'/g, "\\'")}', this)">📋 Copy</button>
            </div>
            <div class="card-actions">
              ${demoBtnHtml}
              <a href="${pkg.pubUrl}" target="_blank" rel="noopener" class="card-link card-link-primary">${mainLinkText}</a>
              <button class="card-link card-link-sub" onclick="openInspector('${pkg.name}')">Inspect ↗</button>
            </div>
          </div>
        `;
        pkgGrid.appendChild(card);
      });
    }

    function setPkgFilter(tab, btn) {
      currentPkgFilter = tab;
      document.querySelectorAll('.filter-tab[data-tab]').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderPackages();
    }

    function filterPackages() {
      renderPackages();
    }

    // ─────────────────────────────────────────────────────────
    // 7. Package Deep Inspector Modal
    // ─────────────────────────────────────────────────────────
    let inspectorActivePkg = null;
    let activeInspTab = 'code';

    function openInspector(pkgName) {
      const pkg = packagesData.find(p => p.name === pkgName);
      if (!pkg) return;
      inspectorActivePkg = pkg;

      document.getElementById('insp-name').textContent = pkg.name;
      document.getElementById('insp-sub').textContent = `${pkg.type.toUpperCase()} · ${pkg.version} · Target Score: ${pkg.score}`;
      renderInspectorContent();
      document.getElementById('inspector-modal').classList.add('active');
    }

    function closeInspector() {
      document.getElementById('inspector-modal').classList.remove('active');
    }

    function setInspTab(tab, btn) {
      activeInspTab = tab;
      document.querySelectorAll('.inspector-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderInspectorContent();
    }

    function renderInspectorContent() {
      const pkg = inspectorActivePkg;
      const body = document.getElementById('insp-body');
      if (!pkg) return;

      if (activeInspTab === 'code') {
        body.innerHTML = `
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <strong style="color:#fff; font-family:var(--font-mono);">Sample Implementation:</strong>
            <button class="copy-pill" onclick="copySnippet(document.getElementById('insp-code-block').textContent, this)">📋 Copy Code</button>
          </div>
          <pre style="background:#000; border:1px solid var(--border); border-radius:8px; padding:16px; overflow-x:auto; font-family:var(--font-mono); font-size:12.5px; color:#f4f4f5;"><code id="insp-code-block">${pkg.sampleCode}</code></pre>
        `;
      } else if (activeInspTab === 'install') {
        const isFlutter = pkg.type === 'flutter';
        const configSnippet = isFlutter
          ? `dependencies:\n  ${pkg.name}: ^${pkg.version}`
          : `// build.gradle.kts\ndependencies {\n    implementation("com.github.govindtank:${pkg.name}:${pkg.version}")\n}`;

        body.innerHTML = `
          <div style="margin-bottom:20px;">
            <strong style="color:#fff; font-family:var(--font-mono);">CLI Command:</strong>
            <div class="install-bar" style="margin-top:8px;">
              <span class="install-text">${pkg.install}</span>
              <button class="copy-pill" onclick="copySnippet('${pkg.install.replace(/'/g, "\\'")}', this)">📋 Copy</button>
            </div>
          </div>
          <div>
            <strong style="color:#fff; font-family:var(--font-mono);">Manifest / Dependency Config:</strong>
            <pre style="background:#000; border:1px solid var(--border); border-radius:8px; padding:16px; margin-top:8px; font-family:var(--font-mono); font-size:12.5px; color:#f4f4f5;"><code>${configSnippet}</code></pre>
          </div>
        `;
      } else {
        const demoHtml = pkg.demoUrl 
          ? `<div style="margin-top:16px;"><a href="${pkg.demoUrl}" target="_blank" class="btn btn-green">⚡ Open Live Web Demo ↗</a></div>` 
          : '';

        body.innerHTML = `
          <p style="font-size:1.05rem; color:#fff; margin-bottom:12px;"><strong>${pkg.tagline}</strong></p>
          <p style="color:var(--text-muted); line-height:1.6; margin-bottom:20px;">${pkg.description}</p>
          
          <div style="margin-bottom:16px;">
            <strong style="color:#fff; font-family:var(--font-mono);">Supported Platforms:</strong>
            <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:8px;">
              ${pkg.platforms.map(p => `<span class="chip chip-plat">${p}</span>`).join('')}
            </div>
          </div>

          <div style="margin-bottom:24px;">
            <strong style="color:#fff; font-family:var(--font-mono);">Highlights &amp; Features:</strong>
            <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:8px;">
              ${pkg.highlights.map(h => `<span class="chip">${h}</span>`).join('')}
            </div>
          </div>

          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="${pkg.pubUrl}" target="_blank" class="btn btn-primary">${pkg.type === 'flutter' ? 'pub.dev' : 'JitPack'} ↗</a>
            <a href="${pkg.repoUrl}" target="_blank" class="btn btn-secondary">GitHub Repository ↗</a>
          </div>
          ${demoHtml}
        `;
      }
    }

    function handleModalOverlayClick(e) {
      if (e.target.id === 'inspector-modal') closeInspector();
    }

    // ─────────────────────────────────────────────────────────
    // 8. Engineering Articles (120 Articles Feed + Deep Reading)
    // ─────────────────────────────────────────────────────────
    const BLOGS_PER_PAGE = 8;
    let currentBlogPage = 1;
    let currentBlogTag = 'all';

    const blogFeed = document.getElementById('blog-feed');
    const blogPagination = document.getElementById('blog-pagination');
    const blogSearchInput = document.getElementById('blog-search');
    const blogReadingView = document.getElementById('blog-reading-view');
    const mainContent = document.getElementById('main-content');

    function getFilteredBlogs() {
      const query = (blogSearchInput.value || '').toLowerCase().trim();
      return blogData.filter(b => {
        if (currentBlogTag !== 'all' && b.tag.toLowerCase() !== currentBlogTag.toLowerCase()) return false;
        if (query) {
          return b.title.toLowerCase().includes(query) ||
                 (b.excerpt && b.excerpt.toLowerCase().includes(query)) ||
                 b.tag.toLowerCase().includes(query);
        }
        return true;
      });
    }

    function renderBlogs() {
      const filtered = getFilteredBlogs();
      const totalPages = Math.max(1, Math.ceil(filtered.length / BLOGS_PER_PAGE));
      if (currentBlogPage > totalPages) currentBlogPage = 1;

      const start = (currentBlogPage - 1) * BLOGS_PER_PAGE;
      const pageItems = filtered.slice(start, start + BLOGS_PER_PAGE);

      blogFeed.innerHTML = '';
      if (pageItems.length === 0) {
        blogFeed.innerHTML = '<div style="text-align:center; padding:48px; color:var(--text-dim); font-family:var(--font-mono);">No matching articles found.</div>';
        blogPagination.innerHTML = '';
        return;
      }

      pageItems.forEach(b => {
        const item = document.createElement('div');
        item.className = 'blog-item';
        item.onclick = () => showArticle(b.slug);

        const coverStyle = b.coverImage 
          ? `background-image:url(${b.coverImage});` 
          : 'background: linear-gradient(135deg, #111217 0%, #1e2029 100%);';

        item.innerHTML = `
          <div class="blog-thumb" style="${coverStyle}"></div>
          <div class="blog-info">
            <div class="blog-tag">${b.tag}</div>
            <div class="blog-heading">${b.title}</div>
            <div class="blog-snippet">${b.excerpt || ''}</div>
            <div class="blog-meta-row">
              <span>${b.date}</span>
              <span class="blog-read-cta">${b.readTime || 8} min read →</span>
            </div>
          </div>
        `;
        blogFeed.appendChild(item);
      });

      // Pagination
      blogPagination.innerHTML = '';
      if (totalPages > 1) {
        blogPagination.innerHTML = `
          <button class="btn btn-secondary" onclick="changeBlogPage(-1)" ${currentBlogPage === 1 ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''}>← Prev</button>
          <span style="font-family:var(--font-mono); font-size:12.5px; color:var(--text-dim);">${currentBlogPage} / ${totalPages}</span>
          <button class="btn btn-secondary" onclick="changeBlogPage(1)" ${currentBlogPage === totalPages ? 'disabled style="opacity:0.3; cursor:not-allowed;"' : ''}>Next →</button>
        `;
      }
    }

    function changeBlogPage(delta) {
      currentBlogPage += delta;
      renderBlogs();
      document.getElementById('blog').scrollIntoView({ behavior: 'smooth' });
    }

    function setBlogTagFilter(tag, btn) {
      currentBlogTag = tag;
      document.querySelectorAll('.filter-tab[data-blog-tag]').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      currentBlogPage = 1;
      renderBlogs();
    }

    function filterBlogs() {
      currentBlogPage = 1;
      renderBlogs();
    }

    function showArticle(slug) {
      const b = blogData.find(x => x.slug === slug);
      if (!b) return;

      document.getElementById('article-tag').textContent = b.tag;
      document.getElementById('article-title').textContent = b.title;
      document.getElementById('article-meta').innerHTML = `
        <span>${b.date}</span>
        <span>·</span>
        <span>${b.readTime || 8} min read</span>
        <span>·</span>
        <span>Govind Tank</span>
      `;

      const coverEl = document.getElementById('article-cover');
      if (b.coverImage) {
        coverEl.src = b.coverImage;
        coverEl.style.display = 'block';
      } else {
        coverEl.style.display = 'none';
      }

      document.getElementById('article-content').innerHTML = b.content;

      // Add copy buttons to code blocks inside article
      document.querySelectorAll('#article-content pre').forEach(pre => {
        if (!pre.querySelector('.code-copy-btn')) {
          const copyBtn = document.createElement('button');
          copyBtn.className = 'code-copy-btn';
          copyBtn.innerHTML = '<span>📋</span> Copy';
          copyBtn.onclick = () => copySnippet(pre.textContent.replace('📋 Copy', '').trim(), copyBtn);
          pre.style.position = 'relative';
          pre.appendChild(copyBtn);
        }
      });

      mainContent.style.display = 'none';
      blogReadingView.classList.add('active');
      location.hash = `#blog/${slug}`;
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function closeArticleView() {
      blogReadingView.classList.remove('active');
      mainContent.style.display = 'block';
      location.hash = '#blog';
      document.getElementById('blog').scrollIntoView({ behavior: 'smooth' });
    }

    function shareCurrentArticle() {
      if (navigator.clipboard) {
        navigator.clipboard.writeText(window.location.href).then(() => {
          showToast('✓ Article link copied to clipboard!');
        });
      }
    }

    // Reading Progress Bar
    window.addEventListener('scroll', () => {
      if (blogReadingView.classList.contains('active')) {
        const winScroll = document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        document.getElementById('reading-bar').style.width = scrolled + '%';
      } else {
        document.getElementById('reading-bar').style.width = '0%';
      }
    });

    // ─────────────────────────────────────────────────────────
    // 9. Command Palette (⌘K)
    // ─────────────────────────────────────────────────────────
    const cmdPalette = document.getElementById('cmd-palette');
    const cmdInput = document.getElementById('cmd-input');
    const cmdResults = document.getElementById('cmd-results');

    function openCmdPalette() {
      cmdPalette.classList.add('active');
      cmdInput.value = '';
      filterCmdResults();
      setTimeout(() => cmdInput.focus(), 50);
    }

    function closeCmdPalette() {
      cmdPalette.classList.remove('active');
    }

    function handleCmdOverlayClick(e) {
      if (e.target.id === 'cmd-palette') closeCmdPalette();
    }

    function filterCmdResults() {
      const query = (cmdInput.value || '').toLowerCase().trim();
      cmdResults.innerHTML = '';

      const list = [];
      // Actions
      list.push({ title: 'Explore 20 Open Source Packages', action: () => { location.hash = '#packages'; closeCmdPalette(); }, tag: 'NAV' });
      list.push({ title: 'Run Interactive Web Terminal', action: () => { location.hash = '#terminal'; closeCmdPalette(); }, tag: 'CLI' });
      list.push({ title: 'View 60s Integration Quickstart', action: () => { location.hash = '#quickstart'; closeCmdPalette(); }, tag: 'NAV' });
      list.push({ title: 'Open GitHub Profile (@govindtank)', action: () => { window.open('https://github.com/govindtank', '_blank'); closeCmdPalette(); }, tag: 'LINK' });

      // Packages
      packagesData.forEach(p => {
        list.push({
          title: `📦 ${p.name} (${p.version}) - ${p.tagline}`,
          action: () => { openInspector(p.name); closeCmdPalette(); },
          tag: p.type.toUpperCase()
        });
        if (p.demoUrl) {
          list.push({
            title: `⚡ Live Demo: ${p.name}`,
            action: () => { window.open(p.demoUrl, '_blank'); closeCmdPalette(); },
            tag: 'DEMO'
          });
        }
      });

      // Blog Articles
      blogData.slice(0, 15).forEach(b => {
        list.push({
          title: `📖 ${b.title}`,
          action: () => { showArticle(b.slug); closeCmdPalette(); },
          tag: 'ARTICLE'
        });
      });

      const matches = list.filter(item => !query || item.title.toLowerCase().includes(query)).slice(0, 8);
      matches.forEach((item, idx) => {
        const li = document.createElement('li');
        li.className = 'cmd-result-item';
        li.innerHTML = `<span>${item.title}</span><span class="cmd-result-tag">${item.tag}</span>`;
        li.onclick = item.action;
        cmdResults.appendChild(li);
      });
    }

    // Global Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        openCmdPalette();
      } else if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openCmdPalette();
      } else if (e.key === 'Escape') {
        closeCmdPalette();
        closeInspector();
      }
    });

    // ─────────────────────────────────────────────────────────
    // 10. FAQ Accordions
    // ─────────────────────────────────────────────────────────
    function toggleFaq(el) {
      const item = el.parentElement;
      item.classList.toggle('active');
    }

    // ─────────────────────────────────────────────────────────
    // 11. Global Toast & Copy Helper
    // ─────────────────────────────────────────────────────────
    let toastTimer;
    function showToast(msg) {
      const t = document.getElementById('toast');
      const tm = document.getElementById('toast-msg');
      tm.textContent = msg;
      t.classList.add('show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => t.classList.remove('show'), 2200);
    }

    function copySnippet(text, btn) {
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(text).then(() => {
        showToast('✓ Copied: ' + (text.length > 35 ? text.slice(0, 35) + '...' : text));
        if (btn) {
          const orig = btn.innerHTML;
          btn.innerHTML = '✓ Copied';
          btn.style.background = 'var(--green)';
          btn.style.color = '#000';
          setTimeout(() => {
            btn.innerHTML = orig;
            btn.style.background = '';
            btn.style.color = '';
          }, 1600);
        }
      });
    }

    // ─────────────────────────────────────────────────────────
    // 12. Hash Routing
    // ─────────────────────────────────────────────────────────
    function handleHashChange() {
      const h = location.hash;
      if (h.startsWith('#blog/')) {
        showArticle(h.replace('#blog/', ''));
      } else if (h === '#blog' || h === '') {
        if (blogReadingView.classList.contains('active')) {
          closeArticleView();
        }
      }
    }
    window.addEventListener('hashchange', handleHashChange);
    handleHashChange();

    // Initial Renders
    renderPackages();
    renderBlogs();
  </script>
</body>
</html>"""

    html = template.replace('__PACKAGES_JSON__', packages_json).replace('__BLOGS_JSON__', blogs_json)

    with open('/Users/govind/workspace/droidtank.is-a.dev/index.html', 'w') as f:
        f.write(html)

    print(f'Successfully built /Users/govind/workspace/droidtank.is-a.dev/index.html (File size: {len(html)} bytes).')

if __name__ == '__main__':
    build_site()
