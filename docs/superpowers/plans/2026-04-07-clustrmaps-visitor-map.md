# ClustrMaps Visitor Map Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Embed a ClustrMaps world dot map at the bottom of the homepage to publicly display visitor locations.

**Architecture:** A new custom HugoBlox block partial (`layouts/partials/blox/clustrmaps.html`) renders the ClustrMaps `<script>` tag inline. The homepage `content/_index.md` references this block as the last section. HugoBlox automatically discovers partials in `layouts/partials/blox/`, so no theme files need to be changed.

**Tech Stack:** Hugo static site, HugoBlox Academic CV theme, ClustrMaps (third-party embed service).

---

## File Map

| Action | Path | Purpose |
|--------|------|---------|
| Create | `layouts/partials/blox/clustrmaps.html` | Custom block partial that renders the ClustrMaps script tag |
| Modify | `content/_index.md` | Add `- block: clustrmaps` as the last homepage section |

---

### Task 1: Create the ClustrMaps block partial

**Files:**
- Create: `layouts/partials/blox/clustrmaps.html`

- [ ] **Step 1: Create the partial file**

Create `layouts/partials/blox/clustrmaps.html` with the following content:

```html
<div class="container">
  <div class="row justify-content-center">
    <div class="col-12 col-md-8 text-center" style="padding: 2rem 0 3rem;">
      <script type="text/javascript" id="clstr_globe"
        src="//clustrmaps.com/map_v2.js?d=SITE_ID&cl=ffffff&w=a">
      </script>
    </div>
  </div>
</div>
```

`SITE_ID` is a placeholder — it will be replaced in Task 3 after registering with ClustrMaps.

- [ ] **Step 2: Verify the file was created**

Run:
```bash
cat layouts/partials/blox/clustrmaps.html
```

Expected: file contents print with the script tag visible and `SITE_ID` as a literal string.

- [ ] **Step 3: Commit**

```bash
git add layouts/partials/blox/clustrmaps.html
git commit -m "feat: add ClustrMaps block partial with placeholder site ID"
```

---

### Task 2: Add the ClustrMaps block to the homepage

**Files:**
- Modify: `content/_index.md`

- [ ] **Step 1: Add the block at the end of the sections list**

Open `content/_index.md`. Find the last active (uncommented) block. It currently ends with the "Recent Posts" block which looks like:

```yaml
  - block: collection
    id: posts
    content:
      title: Recent Posts
      ...
    design:
      view: compact
      columns: '2'
```

After it (before the closing `---`), add:

```yaml
  - block: clustrmaps
```

The end of `content/_index.md` should now look like:

```yaml
  - block: collection
    id: posts
    content:
      title: Recent Posts
      subtitle: ''
      text: ''
      count: 5
      filters:
        folders:
          - post
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: desc
    design:
      view: compact
      columns: '2'
  - block: clustrmaps
---
```

- [ ] **Step 2: Verify the site builds without errors**

Run:
```bash
hugo server --buildDrafts 2>&1 | head -30
```

Expected: Hugo starts successfully with output like `Web Server is available at http://localhost:1313/`. No `ERROR` lines. If you see `partial "blox/clustrmaps.html" not found`, double-check the file path from Task 1.

- [ ] **Step 3: Verify the block renders in the built HTML**

With `hugo server` running, check the built HTML contains the script tag:

```bash
curl -s http://localhost:1313/ | grep -i clustrmaps
```

Expected output contains:
```
clustrmaps.com/map_v2.js?d=SITE_ID
```

- [ ] **Step 4: Commit**

```bash
git add content/_index.md
git commit -m "feat: add ClustrMaps visitor map block to homepage"
```

---

### Task 3: Register with ClustrMaps and set the real site ID

**Files:**
- Modify: `layouts/partials/blox/clustrmaps.html`

> This task requires a browser and takes ~2 minutes.

- [ ] **Step 1: Register your site with ClustrMaps**

1. Go to `https://clustrmaps.com`
2. Enter your site's production URL (e.g. the URL shown in `config/_default/hugo.yaml` under `baseURL`, or your actual deployed domain such as `https://jinxixiang.github.io`)
3. Complete registration (no payment required for the free tier)
4. ClustrMaps will show you an embed code that looks like:

```html
<script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/map_v2.js?d=XXXXXXXXXX&cl=ffffff&w=a"></script>
```

5. Copy the value of the `d=` parameter (e.g. `XXXXXXXXXX` — it will be a string of letters and numbers)

- [ ] **Step 2: Replace SITE_ID in the partial**

Open `layouts/partials/blox/clustrmaps.html` and replace `SITE_ID` with the actual value from the `d=` parameter you copied. The `src` attribute should look like:

```
//clustrmaps.com/map_v2.js?d=your_actual_id_here&cl=ffffff&w=a
```

- [ ] **Step 3: Verify the updated partial**

```bash
cat layouts/partials/blox/clustrmaps.html
```

Expected: `SITE_ID` no longer appears — it is replaced by your actual site ID string.

- [ ] **Step 4: Build and verify the final HTML**

```bash
hugo server 2>&1 | head -5
```

Then in a separate terminal:
```bash
curl -s http://localhost:1313/ | grep -i "clustrmaps.com/map_v2.js"
```

Expected: the script tag appears with your real site ID in the `d=` parameter, not the placeholder.

- [ ] **Step 5: Commit and push**

```bash
git add layouts/partials/blox/clustrmaps.html
git commit -m "feat: set ClustrMaps site ID for visitor map"
git push
```

After Netlify deploys (usually under 2 minutes), visit your live site and scroll to the bottom — the ClustrMaps world map should render. Your first visit will appear as a dot.

---

## Verification Checklist

After deployment:

- [ ] Map renders visually at the bottom of the homepage on desktop
- [ ] Map renders visually at the bottom of the homepage on mobile (auto-width should handle this)
- [ ] Scrolling to the bottom of the homepage shows the map without layout breaks
- [ ] No JavaScript console errors related to ClustrMaps (open DevTools → Console)
- [ ] After a few minutes, your visit appears as a dot on the map (ClustrMaps updates are not always instant)
