---
name: seo-aiseo
description: Research-led ChatGPT WebUI SEO + AI search optimization audits and strategy for websites, combining technical SEO, content/intent, local/entity authority, crawlability, AI citation visibility, and measurement using current evidence.
---

# SEO + AI SEO

Audit and improve a website for both traditional search and AI-driven discovery.

This skill treats AI SEO / AEO / GEO as an extension of SEO, not a separate bag of tricks. The job is to make a site easy to crawl, understand, trust, retrieve, cite, recommend, and convert from.

## Visual chat presentation

Make user-facing output highly visual and easy to scan.

Prefer:

- semantic markers: 🟢 good, 🟡 opportunity, 🔴 blocker, 🔵 evidence, 🟣 experiment;
- compact progress bars;
- short tables for findings and priorities;
- ASCII/Unicode trees and flows;
- concise dashboards instead of walls of prose.

Useful pattern:

~~~text
╭─ SEARCH VISIBILITY ─────────────╮
│ 🟢 crawlability   █████████░ 90% │
│ 🟡 content depth  ██████░░░░ 60% │
│ 🔴 entity signals ███░░░░░░░ 30% │
│ 🟣 AI tests       █████░░░░░ 50% │
╰─────────────────────────────────╯
~~~

Do not decorate exact code, robots.txt directives, schema, metadata, URLs, or copy-paste artifacts in ways that alter them.

## Activation

Use this skill for requests such as:

- SEO audit <URL>
- AI SEO audit <URL>
- optimize this site/page for Google + ChatGPT
- why is this page not ranking?
- why are competitors cited by AI and we are not?
- create an SEO/AEO/GEO strategy
- build a content plan for search + AI visibility
- local SEO audit
- technical SEO review
- review Search Console / Bing Webmaster exports
- prepare a page to be more retrievable or citable by AI search

For substantial implementation in a code repository, keep this skill as the domain rulebook and also load dev-mode for repository execution, verification, and handoff.

## Core principle

Use this model:

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

Do not optimize citation visibility while basic crawlability, indexing, or relevance is broken.

## Mandatory freshness pass

SEO changes slowly. AI search changes quickly.

Before every substantial audit or strategy, browse current sources and verify material platform behavior.

Start with official sources:

1. Google Search Central
2. Google Search Console documentation
3. OpenAI publisher / crawler documentation
4. Bing Webmaster guidance and AI Performance documentation
5. IndexNow documentation
6. Perplexity crawler/search documentation when relevant
7. official ecommerce, local, image, video, or agentic documentation when the site type requires it

Then optionally use large third-party studies for observed behavior.

Do not rely on remembered AI SEO tactics when fresh documentation is available.

Record the research date in the final audit.

## Evidence tiers

Classify important recommendations.

~~~text
🟢 A  official platform documentation or direct first-party evidence
🟡 B  large independent observational study or repeatable industry dataset
🟣 C  plausible experiment, hypothesis, or weak/limited evidence
🔴 X  contradicted, spammy, obsolete, or unsupported tactic
~~~

Rules:

- A outranks B.
- B is correlation unless causality is demonstrated.
- C must be presented as an experiment, never as a ranking fact.
- Never upgrade a third-party correlation into a search-engine rule.
- If sources disagree, state the disagreement and prefer direct platform evidence for platform-specific behavior.

## Start from real evidence

Before diagnosing:

1. identify the site, page, market, language, audience, and business goal;
2. inspect the live website when available;
3. inspect the repository/CMS configuration when connected and relevant;
4. use Search Console, Bing Webmaster, analytics, crawl exports, or uploaded reports when supplied;
5. inspect competitors only when they materially help explain the gap;
6. retrieve facts rather than asking the user to relay data that connected tools can provide.

Do not assume a rendered page equals what crawlers can access.

## Audit modes

Choose the smallest mode that satisfies the request.

### Quick audit

Use for one page or a fast diagnosis.

Cover:

- indexability;
- title/H1/meta;
- search intent;
- core content quality;
- internal links;
- schema relevance;
- AI crawler access;
- major AI-citation opportunities;
- top 5 actions.

### Full audit

Use for a domain or serious strategy.

Cover all phases below.

### Page optimization

Produce exact replacement recommendations for:

- title;
- meta description;
- H1/H2 structure;
- opening answer;
- sections;
- internal links;
- structured data;
- media;
- evidence;
- freshness;
- AI-retrieval opportunities.

Do not keyword-stuff or manufacture claims.

### Local SEO

Add:

- Google Business Profile completeness;
- business name/address/phone consistency where applicable;
- categories/services;
- local landing-page relevance;
- reviews and review velocity;
- local citations and genuine mentions;
- LocalBusiness schema where appropriate;
- maps/local intent;
- location-specific evidence and case studies.

### Ecommerce

Add:

- Merchant Center / product feeds;
- Product structured data;
- variants, price, availability, shipping/returns where relevant;
- canonical handling for faceted/variant URLs;
- crawl traps;
- product review quality;
- comparison and category content;
- agentic/commerce protocols only when current official guidance supports them.

## Phase 1: Technical SEO

Inspect the foundations first.

### Crawl and index

Check:

- robots.txt;
- robots meta / X-Robots-Tag;
- HTTP status codes;
- redirects and chains;
- canonical tags;
- XML sitemap quality and freshness;
- orphan URLs;
- duplicate and near-duplicate URLs;
- pagination/facets where relevant;
- indexable text in the DOM;
- JavaScript rendering dependence;
- mobile rendering;
- HTTPS;
- hreflang for multilingual sites;
- accidental staging/dev indexation;
- crawl traps;
- soft 404s;
- broken internal links;
- canonical/sitemap conflicts.

A page intended for Google Search must be accessible, return a successful status, and contain indexable content.

### Architecture

Check:

- clear hierarchy;
- shallow access to important pages;
- crawlable anchor links;
- descriptive anchor text;
- logical hub → cluster relationships;
- orphaned money pages;
- cannibalization;
- URL clarity and stability.

Prefer architecture that makes entity/topic relationships obvious to humans and machines.

### Page experience

Inspect Core Web Vitals where evidence is available:

- LCP;
- INP;
- CLS.

Also consider mobile usability, intrusive overlays, visual stability, accessibility, and whether primary content is easy to identify.

Do not turn Lighthouse 100 into a religion. Relevance and usefulness still matter more than polishing a score from 97 to 100 because humans enjoy inventing side quests.

## Phase 2: Search intent and information architecture

Build a query/topic map.

For each important page identify:

- target audience;
- primary intent;
- main query/topic;
- meaningful subquestions;
- funnel stage;
- competing/cannibalizing page;
- evidence the page can uniquely provide;
- desired conversion.

Use this structure:

~~~text
topic
├─ primary intent
├─ supporting questions
├─ comparison questions
├─ local/commercial modifiers
├─ evidence users need
└─ best canonical page
~~~

Do not create one page for every tiny query variation.

Google can understand synonyms and related concepts. Scaled pages created mainly to manipulate rankings or generative responses are a risk.

## Phase 3: On-page SEO

For every important page evaluate:

- descriptive, specific title;
- clear H1;
- useful meta description;
- natural-language URL;
- strong first screen;
- answer to the primary intent early;
- logical H2/H3 hierarchy;
- meaningful internal links;
- descriptive image alt text where appropriate;
- relevant image/video support;
- visible authorship or business identity when useful;
- dates only when meaningful;
- factual claims supported by evidence;
- strong conversion path.

The first paragraphs should establish what the page is about and answer the central question without making the reader survive six paragraphs of corporate mist.

## Phase 4: Content quality and information gain

Prioritize non-commodity content.

Look for:

- firsthand experience;
- original research;
- original measurements;
- case studies;
- benchmarks;
- tests;
- expert commentary;
- proprietary process;
- real screenshots;
- original photos/video;
- concrete pricing or ranges where the business can publish them;
- specific constraints and tradeoffs;
- before/after evidence;
- current data;
- useful tools/calculators/templates.

Ask:

~~~text
Could a generic model produce this page without access
to the company, expert, product, customers, or data?
~~~

If yes, the page probably needs more information gain.

Do not manufacture data, reviews, experience, credentials, or case studies.

## Phase 5: Structured data and machine clarity

Use structured data when it truthfully represents visible page content.

Prefer the most specific applicable schema and current Google-supported types.

Common examples:

- Organization;
- LocalBusiness;
- Person;
- Article;
- Product;
- BreadcrumbList;
- VideoObject;
- Event;
- JobPosting;
- other relevant supported types.

Rules:

- JSON-LD is usually the easiest format to maintain;
- validate against current Google requirements;
- do not mark up hidden or nonexistent content;
- do not add schema merely because a plugin can generate it;
- structured data can enable rich results but does not guarantee them;
- there is no special schema required for Google generative AI results.

## Phase 6: Entity, authority, and corroboration

Evaluate whether the web can confidently understand the entity.

Check consistency across:

- official website;
- Google Business Profile where relevant;
- LinkedIn;
- GitHub;
- YouTube;
- major social profiles;
- industry directories;
- partner/client pages;
- reputable press;
- reviews;
- relevant community discussions;
- professional profiles.

Prefer genuine, context-rich mentions over bulk link building or fake citations.

For local businesses, verify complete and accurate business information. Local visibility depends heavily on relevance, distance, and prominence.

## Phase 7: AI search optimization

### Google AI Overviews / AI Mode

Treat foundational SEO as mandatory.

Current official Google guidance should be checked on each substantial run, but the stable principles are:

- pages must be eligible for normal Search;
- create unique, useful, non-commodity content;
- organize content clearly;
- use relevant high-quality images/video;
- keep technical structure crawlable;
- reduce duplication;
- use Business Profile / Merchant Center where appropriate;
- monitor generative visibility in Search Console when available.

Google query fan-out means one user question can trigger several related retrieval queries.

Optimize for this by covering the real supporting questions on a strong canonical page, not by mass-producing thin pages for every fan-out variation.

### ChatGPT Search

Check current OpenAI publisher guidance.

At minimum verify:

- OAI-SearchBot is not blocked where citation/search inclusion is desired;
- robots.txt is not the only access layer;
- CDN/WAF/bot protection does not return 403/challenges to the crawler;
- published OpenAI searchbot IP ranges are not accidentally blocked when allowlisting is required;
- pages are public and directly reachable;
- titles and content clearly describe the page.

Keep GPTBot training controls conceptually separate from OAI-SearchBot search discovery.

Track ChatGPT referrals when available. OpenAI currently appends a ChatGPT referral UTM parameter to search-result traffic.

### Bing / Copilot

Use Bing Webmaster Tools when available.

Inspect:

- indexing/crawl health;
- AI Performance;
- cited URLs;
- citation trends;
- grounding queries;
- pages that are indexed but rarely cited.

Use grounding-query data as a feedback loop for improving relevance, clarity, depth, and evidence.

Consider IndexNow for sites where timely updates matter.

### Perplexity

Check current Perplexity crawler guidance.

Verify PerplexityBot access when the owner wants discoverability.

Treat Perplexity-specific recommendations as platform-specific, not universal SEO rules.

### AI retrieval / citation heuristics

These are not guaranteed ranking factors.

Use current evidence tier B/C to test:

- strong semantic alignment between page title, page content, and likely subquestions;
- human-readable URL slugs;
- concise passages that state useful facts clearly;
- tables for genuinely tabular comparisons;
- explicit entity names where ambiguity would otherwise exist;
- freshness for time-sensitive topics;
- original data and attributable facts;
- genuine third-party brand mentions;
- comparison content where it matches real user intent;
- multimedia where it adds unique evidence.

Do not contort prose into robotic fragments merely to make it "AI-readable".

## What not to do

Flag these aggressively:

~~~text
🔴 mass-generated doorway pages
🔴 fake reviews or testimonials
🔴 fake citations / fake brand mentions
🔴 keyword stuffing
🔴 hidden AI-targeted text
🔴 changing only the publish date to appear fresh
🔴 schema spam
🔴 thin location pages
🔴 copied product/service descriptions
🔴 buying junk backlinks at scale
🔴 claiming guaranteed rankings or guaranteed AI citations
~~~

Also:

- llms.txt may be used by services that support it, but Google currently says it neither helps nor hurts Google Search visibility;
- artificial content chunking is not required for Google generative search;
- there is no universal "AI schema";
- do not create pages for every long-tail wording;
- do not chase inauthentic mentions.

## Preferred Sources

When the site is an eligible publication and current Google documentation supports it, evaluate Google Preferred Sources.

Do not recommend it blindly to every business.

Check:

- eligibility;
- whether the domain/subdomain appears in the source preference tool;
- whether generative-AI inclusion is enabled where required;
- whether an Add to Preferred Sources button or deeplink fits the site's audience strategy.

Treat this as an audience preference mechanism, not a universal ranking hack.

## Agentic readiness

When relevant to the business, inspect whether browser agents can understand and operate the site.

Look at:

- semantic structure;
- accessibility tree;
- ARIA labels/roles/states;
- form labels;
- stable interactive controls;
- clear pricing/product/action states;
- authentication/payment boundaries;
- current platform-specific agentic protocols.

This is secondary to SEO unless agents are part of the business goal.

## Competitive AI visibility analysis

When competitors appear in AI answers and the target site does not:

1. capture representative prompts;
2. inspect which competitors are mentioned;
3. inspect which pages are cited;
4. identify the likely retrieval subquestions;
5. compare title/topic alignment;
6. compare evidence, freshness, depth, and original information;
7. compare third-party corroboration;
8. distinguish citation gaps from brand-mention gaps;
9. propose the smallest content or authority change that closes the gap.

Do not assume the most cited domain is "best". AI responses are probabilistic and platform behavior varies.

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
- generative AI performance;
- AI-visible pages;
- country/device trends.

### Bing / Microsoft AI

- total AI citations;
- average cited pages;
- grounding queries;
- page-level citation activity;
- trends.

### ChatGPT

- referral traffic;
- landing pages;
- conversions from ChatGPT referrals;
- observed citation/mention coverage across a stable prompt set.

### Business outcomes

Always connect search visibility to:

- leads;
- sales;
- bookings;
- qualified inquiries;
- signups;
- revenue;
- other meaningful conversions.

Traffic without business value is a graph humans admire before asking why revenue is flat.

## Prioritization

Do not invent a fake search-engine score.

Use priority levels:

~~~text
P0  blocks crawling/indexing or causes severe search loss
P1  high-impact relevance/content/architecture problem
P2  meaningful improvement opportunity
P3  experiment, polish, or low-confidence opportunity
~~~

For each action include:

- SEO / AI SEO / both;
- evidence tier;
- impact;
- confidence;
- effort;
- affected URLs;
- exact fix;
- verification method.

## Default deliverable

For a full audit, return:

1. executive summary;
2. technical blockers;
3. content/intent findings;
4. entity/local/authority findings;
5. AI search findings;
6. prioritized action table;
7. page/topic opportunities;
8. exact examples of improved titles/sections/schema only where useful;
9. measurement plan;
10. myths/tactics to ignore;
11. research date and key current sources.

Keep the action list implementation-ready.

## Implementation boundary

If the user asks only for analysis, do not modify their site.

If the user asks for implementation and repository access exists:

1. preserve this skill's SEO requirements;
2. load dev-mode;
3. implement in coherent slices;
4. verify rendered output and source/DOM where possible;
5. re-run the relevant audit checks after changes.

Content edits that change factual claims, offers, pricing, credentials, or legal promises require source evidence or user-provided facts.

## Durable progress

Long audits may span multiple WebUI turns.

Preserve:

- target site;
- market/language;
- audit mode;
- pages already inspected;
- evidence already gathered;
- confirmed blockers;
- priority actions;
- unfinished sections;
- exact next operation.

Prefer an existing project issue/spec/document when writes are authorized.

Do not restart discovery after the user says continue.

## Tool-budget continuity

For connector-heavy work, checkpoint before the WebUI limit becomes risky.

Around the repository convention's preferred checkpoint:

1. save durable state;
2. finish the current atomic inspection;
3. report what is complete;
4. end with:

~~~text
╭─ TOOL BUDGET ──────────────╮
│ 🟡 checkpoint saved        │
│ → send: continue           │
╰─────────────────────────────╯
~~~

On continue, resume the exact unfinished operation.

## Fresh-session recovery

When invoked as:

~~~text
continue SEO audit on <site/project>
~~~

first reload this skill.

Then recover the latest durable state from the named project, issue, report, repository, or conversation-accessible artifact.

Restore:

- site and scope;
- pages inspected;
- findings;
- evidence sources;
- priority queue;
- next action.

Do not make the user repeat information that is already retrievable.

## Completion

An SEO + AI SEO audit is complete when:

- important crawl/index blockers are known;
- intent and page-role conflicts are identified;
- content gaps are tied to real user/search needs;
- AI crawler/access issues are checked;
- AI-specific tactics are labeled by evidence strength;
- local/ecommerce requirements are covered when relevant;
- recommendations are prioritized and actionable;
- measurement is defined;
- unsupported hacks are separated from evidence-backed work.

Do not promise rankings. Produce evidence, fixes, and a system that can be measured.
