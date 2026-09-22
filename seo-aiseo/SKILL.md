---
name: seo-aiseo
description: Research-led ChatGPT WebUI SEO + AI search optimization for websites, combining technical SEO, content/intent, entity/local authority, crawlability, AI citation visibility, and measurement using current evidence.
---

# SEO + AI SEO

Audit and improve websites for classic search and AI-driven discovery.

Treat AI SEO / AEO / GEO as an extension of SEO, not a separate bag of tricks.

~~~text
crawlable
   ↓
indexable
   ↓
relevant
   ↓
useful + original
   ↓
trusted / corroborated
   ↓
retrievable
   ↓
citable / mentionable
   ↓
conversion
~~~

Do not optimize AI citations while crawling, indexing, relevance, or basic content quality is broken.

## Visual chat presentation

Make user-facing output highly visual and easy to scan.

Prefer:

- 🟢 good / verified;
- 🟡 opportunity / medium confidence;
- 🔴 blocker / risk;
- 🔵 first-party evidence;
- 🟣 experiment / hypothesis;
- compact dashboards, trees, tables, and progress bars.

Do not decorate exact code, schema, metadata, robots directives, or copy-paste artifacts in ways that alter them.

## Activation

Use for:

- SEO audit <URL>
- AI SEO audit <URL>
- optimize this page/site for Google + ChatGPT
- why is this page not ranking?
- why are competitors cited by AI and we are not?
- local SEO audit
- technical SEO review
- content strategy for search + AI
- Search Console / Bing Webmaster analysis
- AI citation / mention visibility analysis

For substantial repository implementation, keep this skill as the domain rulebook and also load dev-mode.

## Mandatory freshness pass

Before every substantial audit or strategy, browse current platform guidance.

Start with first-party sources:

1. Google Search Central and Search Console docs;
2. OpenAI publisher / crawler docs;
3. Bing Webmaster and AI Performance docs;
4. IndexNow;
5. Perplexity crawler/search docs when relevant;
6. Merchant Center, Business Profile, image/video, local, international, or agentic docs when the site requires them.

Then use large independent studies only for observed behavior.

Do not rely on remembered AI SEO tactics when current documentation is available.

Record the research date.

## Evidence tiers

~~~text
🟢 A  official platform documentation / direct first-party evidence
🟡 B  large independent observational study / repeatable dataset
🟣 C  experiment, hypothesis, or limited evidence
🔴 X  contradicted, spammy, obsolete, or unsupported tactic
~~~

Rules:

- A outranks B.
- B is correlation unless causality is demonstrated.
- C must be framed as a test, never as a ranking fact.
- If sources disagree, state the disagreement.
- Never convert a vendor study into a search-engine rule.

## Start from real evidence

Before diagnosing:

1. identify site/page, market, language, audience, and business goal;
2. inspect the live site;
3. inspect repo/CMS configuration when connected and relevant;
4. use Search Console, Bing Webmaster, analytics, crawl exports, or uploaded reports when available;
5. retrieve facts instead of asking the user to relay accessible data.

Do not assume a rendered page equals crawler-visible content.

## Choose audit depth

### Quick audit

Cover:

- crawl/indexability;
- title/H1/meta;
- intent match;
- main content quality;
- internal links;
- schema relevance;
- AI crawler access;
- top AI citation opportunities;
- top 5 actions.

### Full audit

Load seo-aiseo/REFERENCE.md and work through the detailed checklist.

### Page optimization

Produce exact recommendations for:

- title;
- meta description;
- H1/H2 structure;
- opening answer;
- sections;
- internal links;
- media;
- schema;
- evidence;
- freshness;
- AI retrieval opportunities.

Never manufacture claims, reviews, case studies, prices, or credentials.

## Audit order

Always work in this order:

~~~text
1 technical
2 architecture + intent
3 on-page
4 information gain
5 structured data
6 entity / local / authority
7 AI search
8 measurement
~~~

Fix foundations before polishing experiments.

## 1. Technical SEO

Check the relevant items:

- robots and noindex controls;
- successful HTTP responses;
- canonicalization;
- redirects;
- sitemaps;
- duplicate URLs;
- crawlable internal links;
- orphan pages;
- JavaScript-rendered content;
- indexable text in the DOM;
- mobile behavior;
- HTTPS;
- hreflang when multilingual;
- soft 404s and broken links;
- crawl traps / facets;
- staging leakage;
- sitemap/canonical conflicts.

For performance, inspect Core Web Vitals when evidence exists:

- LCP;
- INP;
- CLS.

Do not turn Lighthouse 100 into a religion.

## 2. Intent and architecture

Map each important canonical page to:

- audience;
- primary intent;
- main topic/query;
- meaningful supporting questions;
- funnel stage;
- competing/cannibalizing page;
- unique evidence;
- conversion.

Do not create a page for every tiny keyword or fan-out variation.

Prefer coherent hub/cluster relationships and clear internal linking.

## 3. On-page SEO

Evaluate:

- specific, descriptive title;
- clear H1;
- useful meta description;
- readable stable URL;
- primary answer early;
- logical H2/H3 structure;
- descriptive internal anchors;
- relevant media;
- visible business/author identity where useful;
- factual support;
- clear conversion path.

Avoid corporate fog before the answer. Search engines and humans both have better things to do.

## 4. Information gain

Prioritize non-commodity content:

- firsthand experience;
- original research/data;
- benchmarks/tests;
- case studies;
- expert commentary;
- proprietary process;
- original screenshots/photos/video;
- concrete pricing/ranges when publishable;
- before/after evidence;
- current facts;
- useful tools/templates/calculators.

Use the test:

~~~text
Could a generic model create this page without access
to this company, expert, product, customers, or data?
~~~

If yes, seek more original value.

## 5. Structured data

Use only schema that truthfully represents visible content.

Common examples:

- Organization;
- LocalBusiness;
- Person;
- Article;
- Product;
- BreadcrumbList;
- VideoObject;
- Event;
- JobPosting.

Prefer current Google-supported guidance and validate markup.

Structured data can enable rich results. It does not guarantee rankings or AI citations.

There is no universal special AI schema.

## 6. Entity, local, and authority

Check whether the entity is consistently represented across relevant sources:

- official site;
- Google Business Profile;
- LinkedIn;
- GitHub;
- YouTube;
- major social profiles;
- partners/clients;
- reputable directories;
- press;
- reviews;
- relevant communities.

Prefer genuine context-rich mentions over bulk links or fake citations.

For local businesses, verify complete business information and evaluate relevance, distance constraints, prominence, reviews, local evidence, and LocalBusiness markup where appropriate.

## 7. AI search

### Google AI features

Treat normal SEO as the foundation.

Current stable guidance:

- be eligible for normal Search;
- create unique, useful, non-commodity content;
- organize content clearly;
- use useful images/video;
- keep the site crawlable;
- reduce duplication;
- use Business Profile / Merchant Center when relevant;
- measure generative visibility in Search Console.

Query fan-out means one question may trigger related retrieval queries.

Cover real subquestions naturally on strong canonical pages. Do not mass-produce thin fan-out pages.

Google currently says:

- llms.txt does not improve Google visibility;
- artificial chunking is unnecessary;
- there is no special AI markup requirement;
- inauthentic mentions are not a useful strategy.

Re-verify these claims on substantial runs because platform guidance can change.

### ChatGPT Search

Check current OpenAI guidance.

Verify:

- OAI-SearchBot access;
- CDN/WAF/bot protection does not block it;
- published IP ranges are not accidentally blocked when allowlisting is used;
- pages are public and reachable;
- titles/content clearly describe the page.

Keep GPTBot training controls separate from OAI-SearchBot search discovery.

Track ChatGPT referral traffic when available.

### Bing / Copilot

Use Bing Webmaster Tools when available.

Inspect:

- AI citations;
- cited URLs;
- grounding queries;
- page-level citation activity;
- trends.

Use grounding queries as a feedback loop for relevance, clarity, depth, evidence, and freshness.

Consider IndexNow when timely updates matter.

### Perplexity

Check current Perplexity crawler guidance and verify PerplexityBot access when discoverability is desired.

Keep Perplexity-specific tactics platform-specific.

## AI citation heuristics

These are tests, not guaranteed ranking factors.

Current evidence may justify testing:

- semantic alignment between title/content and likely subquestions;
- human-readable URLs;
- clear fact-rich passages;
- genuine comparison tables;
- explicit entity names where ambiguity exists;
- freshness for time-sensitive topics;
- original attributable data;
- genuine third-party brand mentions;
- comparison content when it matches user intent;
- useful multimedia.

Label each recommendation B or C unless first-party guidance supports it.

Do not rewrite pages into robotic fragments merely to appear "AI-readable".

## What to reject

~~~text
🔴 mass doorway pages
🔴 fake reviews / testimonials
🔴 fake citations / mentions
🔴 keyword stuffing
🔴 hidden AI-targeted text
🔴 date-only freshness updates
🔴 schema spam
🔴 thin location pages
🔴 copied commodity content
🔴 junk backlink campaigns
🔴 guaranteed ranking/citation promises
~~~

## Preferred Sources and agentic readiness

When relevant, verify current official guidance before recommending:

- Google Preferred Sources for eligible publications;
- agent-friendly accessibility/ARIA;
- commerce/agentic protocols.

Treat these as conditional features, not universal SEO hacks.

## Competitive AI visibility analysis

When competitors are cited and the target is not:

1. capture representative prompts;
2. inspect mentions and cited pages;
3. infer likely retrieval subquestions;
4. compare title/topic alignment;
5. compare original evidence, freshness, depth, and clarity;
6. compare third-party corroboration;
7. separate citation gaps from brand-mention gaps;
8. recommend the smallest evidence-backed change.

Do not call the most cited domain "best". AI outputs are probabilistic.

## Measurement

Prefer first-party data.

Track where available:

### Google
- organic impressions/clicks;
- query groups;
- landing pages;
- indexed pages;
- Core Web Vitals;
- rich-result issues;
- generative AI performance.

### Bing / Microsoft AI
- total AI citations;
- average cited pages;
- grounding queries;
- page-level citation activity;
- trends.

### ChatGPT
- referral traffic;
- landing pages;
- conversions;
- stable prompt-set citation/mention observations.

### Business
- leads;
- sales;
- bookings;
- signups;
- qualified inquiries;
- revenue.

Traffic without business value is just a prettier graph.

## Prioritization

Do not invent a fake platform score.

Use:

~~~text
P0  crawl/index blocker or severe loss
P1  high-impact relevance/content/architecture issue
P2  meaningful improvement
P3  experiment / polish / low-confidence opportunity
~~~

For each action include:

- SEO / AI SEO / both;
- evidence tier;
- impact;
- confidence;
- effort;
- affected URLs;
- exact fix;
- verification.

## Default full-audit deliverable

Return:

1. executive summary;
2. technical blockers;
3. intent/content findings;
4. entity/local/authority findings;
5. AI search findings;
6. prioritized action table;
7. page/topic opportunities;
8. exact examples where useful;
9. measurement plan;
10. myths/tactics to ignore;
11. research date and key sources.

Keep it implementation-ready.

## Implementation boundary

If the user asks only for analysis, do not modify the site.

If implementation is requested and repo access exists:

1. preserve this skill's requirements;
2. load dev-mode;
3. implement coherent slices;
4. verify rendered output and source/DOM where possible;
5. re-run relevant audit checks.

Factual content changes require evidence or user-provided facts.

## Durable progress

For long audits preserve:

- target site;
- market/language;
- audit mode;
- pages inspected;
- evidence gathered;
- blockers;
- priority actions;
- unfinished sections;
- exact next operation.

Do not restart discovery after continue.

## Tool-budget continuity

Before connector-heavy work becomes risky:

1. save durable state;
2. finish the current atomic inspection;
3. report completed work;
4. end with:

~~~text
╭─ TOOL BUDGET ──────────────╮
│ 🟡 checkpoint saved        │
│ → send: continue           │
╰─────────────────────────────╯
~~~

On continue, resume the exact unfinished operation.

## Fresh-session recovery

For:

~~~text
continue SEO audit on <site/project>
~~~

reload this skill, recover durable state, restore the priority queue, then continue.

Do not make the user repeat retrievable facts.

## Completion

The audit is complete when:

- crawl/index blockers are known;
- intent/page-role conflicts are identified;
- content gaps map to real user needs;
- AI crawler/access issues are checked;
- AI-specific tactics are evidence-tiered;
- local/ecommerce requirements are covered when relevant;
- actions are prioritized;
- measurement is defined;
- unsupported hacks are separated from evidence-backed work.

Do not promise rankings. Produce evidence, fixes, and a measurable system.
