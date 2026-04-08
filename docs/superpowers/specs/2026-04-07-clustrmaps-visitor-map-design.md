# ClustrMaps Visitor Map — Design Spec

**Date:** 2026-04-07  
**Status:** Approved

## Goal

Embed a public world dot map at the bottom of the homepage that shows the geographic locations of all site visitors, powered by ClustrMaps.

## Background

The site is a Hugo static site using the HugoBlox Academic CV theme, deployed on Netlify. It has no server-side code. The homepage is defined by `content/_index.md` using HugoBlox's block system. There is already a `layouts/partials/` directory with custom partials in use.

## Architecture

ClustrMaps is a third-party service that handles all tracking and map rendering. When a visitor loads the page, the ClustrMaps `<script>` tag fires, their servers record the visit (IP-based geolocation), and the map renders inline showing accumulated visitor dots. No server-side code is required on this site.

**Data flow:**
```
Visitor loads page
  → ClustrMaps <script> executes
  → ClustrMaps servers log visit (IP → geo region)
  → Map SVG/canvas renders inline with all historical dots
```

## Components

### 1. `layouts/partials/blox/clustrmaps.html` (new file)

A custom HugoBlox block partial. HugoBlox automatically discovers block partials in `layouts/partials/blox/`. This file renders a centered container with the ClustrMaps embed script.

```html
<div class="col-12 text-center" style="padding: 2rem 0;">
  <script type="text/javascript" id="clstr_globe"
    src="//clustrmaps.com/map_v2.js?d=SITE_ID&cl=ffffff&w=a">
  </script>
</div>
```

`SITE_ID` is the unique identifier obtained from ClustrMaps after registering the site URL. The query params:
- `d=SITE_ID` — identifies the registered site
- `cl=ffffff` — cluster color (white, matches the theme)
- `w=a` — auto width (fills the container)

### 2. `content/_index.md` (modified)

Add the `clustrmaps` block as the last entry in the `sections:` list, after the existing "Recent Posts" block:

```yaml
  - block: clustrmaps
```

No `content:` or `design:` fields are needed — the partial is self-contained.

## Manual One-Time Setup Step

Before deploying, the site owner must:

1. Go to [clustrmaps.com](https://clustrmaps.com) and register the site's production URL (e.g., `https://jinxixiang.github.io` or the custom domain).
2. ClustrMaps generates a unique site ID and embed code.
3. Copy the site ID from the embed code URL (the value of the `d=` parameter).
4. Replace `SITE_ID` in `layouts/partials/blox/clustrmaps.html` with the actual value.

This step takes approximately 2 minutes and requires no account payment.

## Scope and Exclusions

- **In scope:** Homepage only. The map block is added only to `content/_index.md`.
- **Out of scope:** Per-page view counters, private analytics dashboards, server-side logging, real-time "online now" counts.
- **Not changed:** `hugo.yaml`, `params.yaml`, theme files, any other content pages.

## Privacy

ClustrMaps processes visitor IPs on their servers. IPs are not exposed to page visitors. The map displays dots by geographic region, not individual addresses. ClustrMaps' privacy policy governs data handling.

## Notes

- Netlify deploy preview visits will also count toward the map. ClustrMaps allows excluding IPs or subdomains from the dashboard if desired.
- The map auto-sizes to the block container width (typically full content width on desktop, full screen width on mobile).
- The small ClustrMaps logo appears on the map (standard for the free tier).
