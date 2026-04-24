import fs from "node:fs";
import path from "node:path";

const README_FILE = process.env.README_FILE || "README.md";
const OPENAPI_FILE = process.env.OPENAPI_FILE || "";
const OPENAPI_URL =
  process.env.OPENAPI_URL?.trim() || "http://api.justserpapi.com/v3/api-docs/gateway";
const FETCH_TIMEOUT_MS = Number.parseInt(process.env.OPENAPI_FETCH_TIMEOUT_MS || "30000", 10);
const DOCS_BASE_URL = (process.env.DOCS_BASE_URL || "https://docs.justserpapi.com").replace(/\/+$/, "");
const UTM_CONTENT = process.env.UTM_CONTENT || "repo_readme_api_list";
const API_LIST_START = "<!-- API_LIST_START -->";
const API_LIST_END = "<!-- API_LIST_END -->";
const API_PATH_PREFIX = "/api/v1/";

const HTTP_METHODS = new Set(["get", "post", "put", "patch", "delete", "options", "head", "trace"]);
const UTM_CAMPAIGN = "justserpapi_justserpapi_python";

const SECTION_TITLES = {
  google: "Google API",
  web: "Web API",
  "google/search": "Google Search API",
  "google/ai-mode": "Google AI Mode API",
  "google/ai-overview": "Google AI Overview API",
  "google/maps": "Google Maps API",
  "google/images": "Google Images API",
  "google/news": "Google News API",
  "google/videos": "Google Videos API",
  "google/shorts": "Google Shorts API",
  "google/finance": "Google Finance API",
  "google/trends": "Google Trends API",
  "google/shopping": "Google Shopping API",
  "google/immersive": "Google Immersive Product API",
  "google/autocomplete": "Google Autocomplete API",
  "google/scholar": "Google Scholar API",
  "google/lens": "Google Lens API",
  "google/jobs": "Google Jobs API",
  "google/local": "Google Local API",
  "google/patents": "Google Patents API",
  "google/hotels": "Google Hotels API",
};

const OPERATION_TITLES = {
  "google/search": "Search API",
  "google/search/light": "Light Search API",
  "google/search/mobile": "Mobile Search API",
  "google/ai-mode": "AI Mode API",
  "google/ai-overview": "AI Overview API",
  "google/maps/search": "Maps Search API",
  "google/maps/posts": "Maps Posts API",
  "google/maps/photos": "Maps Photos API",
  "google/maps/reviews": "Maps Reviews API",
  "google/maps/places": "Maps Place Details API",
  "google/images/search": "Images Search API",
  "google/news/search": "News Search API",
  "google/videos/search": "Videos Search API",
  "google/shorts/search": "Shorts Search API",
  "google/finance/search": "Finance Search API",
  "google/trends/search": "Google Trends Search API",
  "google/trends/autocomplete": "Google Trends Autocomplete API",
  "google/trends/trending-now": "Google Trends Trending Now API",
  "google/shopping/search": "Shopping Search API",
  "google/immersive/product": "Immersive Product API",
  "google/autocomplete": "Autocomplete API",
  "google/scholar/search": "Google Scholar Search API",
  "google/scholar/profiles": "Google Scholar Profiles API",
  "google/scholar/author": "Google Scholar Author API",
  "google/scholar/cite/search": "Google Scholar Cite API",
  "google/lens": "Lens API",
  "google/jobs/search": "Jobs Search API",
  "google/local/search": "Local Search API",
  "google/patents/search": "Google Patents Search API",
  "google/patents/details": "Google Patents Details API",
  "google/hotels/search": "Hotels Search API",
  "web/html": "Crawl Webpage (HTML)",
  "web/rendered-html": "Crawl Webpage (Rendered HTML)",
  "web/markdown": "Crawl Webpage (Markdown)",
};

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function getEnvValue(...names) {
  for (const name of names) {
    const value = process.env[name]?.trim();
    if (value) return value;
  }
  return "";
}

function requireEnv(...names) {
  const value = getEnvValue(...names);
  if (!value) {
    throw new Error(`${names.join(" or ")} is required.`);
  }
  return value;
}

async function fetchOpenApi() {
  const username = requireEnv("OPENAPI_BASIC_AUTH_USER", "OPENAPI_BASIC_AUTH_USERNAME");
  const password = requireEnv("OPENAPI_BASIC_AUTH_PASS", "OPENAPI_BASIC_AUTH_PASSWORD");
  const auth = Buffer.from(`${username}:${password}`, "utf8").toString("base64");
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);

  try {
    const response = await fetch(OPENAPI_URL, {
      headers: {
        Accept: "application/json",
        Authorization: `Basic ${auth}`,
      },
      redirect: "follow",
      signal: controller.signal,
    });
    const body = await response.text();

    if (!response.ok) {
      const compactBody = body.replace(/\s+/g, " ").trim().slice(0, 200);
      throw new Error(
        `Failed to fetch OpenAPI: HTTP ${response.status} ${response.statusText}${
          compactBody ? ` - ${compactBody}` : ""
        }`,
      );
    }

    return JSON.parse(body);
  } catch (error) {
    if (error.name === "AbortError") {
      throw new Error(`OpenAPI fetch timed out after ${FETCH_TIMEOUT_MS}ms.`);
    }
    throw error;
  } finally {
    clearTimeout(timeout);
  }
}

async function loadOpenApi() {
  if (OPENAPI_FILE) {
    console.log(`Reading OpenAPI from ${OPENAPI_FILE}`);
    return readJson(OPENAPI_FILE);
  }

  console.log(`Fetching OpenAPI from ${OPENAPI_URL}`);
  return fetchOpenApi();
}

function titleCase(text = "") {
  return String(text)
    .split(/[-_\s]+/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function normalizeText(text = "") {
  return String(text).replace(/\s+/g, " ").trim();
}

function stripApiSuffix(text = "") {
  return normalizeText(text).replace(/\s+API$/i, "");
}

function getNumericOrder(value) {
  if (value === undefined || value === null || value === "") return null;
  const numeric = Number.parseInt(String(value), 10);
  return Number.isFinite(numeric) ? numeric : null;
}

function compareOrder(aOrder, bOrder, aIndex, bIndex) {
  const a = aOrder ?? Number.MAX_SAFE_INTEGER;
  const b = bOrder ?? Number.MAX_SAFE_INTEGER;
  if (a !== b) return a - b;
  return aIndex - bIndex;
}

function parseApiPath(apiPath = "") {
  const normalizedPath = String(apiPath);
  if (!normalizedPath.startsWith(API_PATH_PREFIX)) return null;

  const segments = normalizedPath.slice(API_PATH_PREFIX.length).split("/").filter(Boolean);
  if (segments.length < 2) return null;

  const [group, ...slugParts] = segments;
  const operationKey = `${group}/${slugParts.join("/")}`;
  const sectionKey = group === "google" && slugParts[0] ? `google/${slugParts[0]}` : group;

  return {
    operationKey,
    sectionKey,
    docsPath: `${API_PATH_PREFIX}${operationKey}`,
  };
}

function getSectionTitle(sectionKey) {
  if (SECTION_TITLES[sectionKey]) return SECTION_TITLES[sectionKey];

  if (sectionKey.startsWith("google/")) {
    return `Google ${titleCase(sectionKey.slice("google/".length))} API`;
  }

  return `${titleCase(sectionKey)} API`;
}

function getOperationTitle(operationKey, op, sectionKey) {
  if (OPERATION_TITLES[operationKey]) return OPERATION_TITLES[operationKey];

  const summary = normalizeText(op.summary || op.operationId || operationKey);
  if (!summary) return operationKey;
  if (/\bAPI$/i.test(summary)) return summary;

  const sectionBase = stripApiSuffix(getSectionTitle(sectionKey)).replace(/^Google\s+/i, "");
  const summaryTokens = summary.toLowerCase().split(/\s+/);
  const sectionTokens = sectionBase.toLowerCase().split(/\s+/);
  const startsWithSection = sectionTokens.every((token, index) => summaryTokens[index] === token);

  return startsWithSection ? `${summary} API` : `${sectionBase} ${summary} API`;
}

function collectApiGroups(api) {
  const groups = new Map();
  let operationIndex = 0;

  for (const [pathKey, methods] of Object.entries(api.paths || {})) {
    const parsedPath = parseApiPath(pathKey);
    if (!parsedPath) continue;

    for (const [method, op] of Object.entries(methods || {})) {
      if (!HTTP_METHODS.has(method.toLowerCase())) continue;

      if (!groups.has(parsedPath.sectionKey)) {
        groups.set(parsedPath.sectionKey, {
          sectionKey: parsedPath.sectionKey,
          title: getSectionTitle(parsedPath.sectionKey),
          index: groups.size,
          operations: [],
        });
      }

      groups.get(parsedPath.sectionKey).operations.push({
        title: getOperationTitle(parsedPath.operationKey, op, parsedPath.sectionKey),
        deprecated: Boolean(op.deprecated),
        docsPath: parsedPath.docsPath,
        order: getNumericOrder(op["x-order"]),
        index: operationIndex,
      });
      operationIndex += 1;
    }
  }

  return Array.from(groups.values())
    .map((group) => ({
      ...group,
      operations: group.operations.sort((a, b) => compareOrder(a.order, b.order, a.index, b.index)),
    }))
    .sort((a, b) =>
      compareOrder(a.operations[0]?.order ?? null, b.operations[0]?.order ?? null, a.index, b.index),
    );
}

function buildUtmQuery() {
  return new URLSearchParams({
    utm_source: "github.com",
    utm_medium: "referral",
    utm_campaign: UTM_CAMPAIGN,
    utm_content: UTM_CONTENT,
  });
}

function buildDocsHomeUrl() {
  return `${DOCS_BASE_URL}/?${buildUtmQuery().toString()}`;
}

function buildDocsUrl(docsPath, deprecated) {
  const fragment = deprecated ? "#deprecated" : "";
  return `${DOCS_BASE_URL}${docsPath}?${buildUtmQuery().toString()}${fragment}`;
}

function escapeMarkdownLinkText(text) {
  return String(text).replace(/([\\[\]])/g, "\\$1");
}

function renderApiList(groups) {
  return groups
    .map((group) => {
      const lines = [`### ${group.title}`, ""];
      for (const operation of group.operations) {
        const displayTitle = operation.deprecated ? `${operation.title} (Deprecated)` : operation.title;
        lines.push(
          `- [${escapeMarkdownLinkText(displayTitle)}](${buildDocsUrl(
            operation.docsPath,
            operation.deprecated,
          )})`,
        );
      }
      return lines.join("\n");
    })
    .join("\n\n");
}

function buildReadmeSection(apiList) {
  return `## Service Overview

The API list below is generated from OpenAPI and shows the current public API categories and endpoint names. See the [online API documentation](${buildDocsHomeUrl()}) for full request and response details.

${API_LIST_START}

${apiList}

${API_LIST_END}
`;
}

function replaceApiListSection(readme, section) {
  const headingRegex = /^##\s+Service\s+Overview\s*$/m;
  const headingMatch = readme.match(headingRegex);

  if (headingMatch && headingMatch.index !== undefined) {
    const start = headingMatch.index;
    const afterHeading = start + headingMatch[0].length;
    const rest = readme.slice(afterHeading);
    const nextHeadingOffset = rest.search(/\n##\s+/);
    const end = nextHeadingOffset === -1 ? readme.length : afterHeading + nextHeadingOffset;
    return `${readme.slice(0, start)}${section}${readme.slice(end)}`;
  }

  const startMarkerIndex = readme.indexOf(API_LIST_START);
  const endMarkerIndex = readme.indexOf(API_LIST_END);
  if (startMarkerIndex !== -1 && endMarkerIndex !== -1 && endMarkerIndex > startMarkerIndex) {
    const sectionStart = readme.lastIndexOf("\n## ", startMarkerIndex);
    const start = sectionStart === -1 ? startMarkerIndex : sectionStart + 1;
    const end = endMarkerIndex + API_LIST_END.length;
    return `${readme.slice(0, start)}${section}${readme.slice(end)}`;
  }

  const licenseMatch = readme.match(/^##\s+License\s*$/m);
  if (licenseMatch && licenseMatch.index !== undefined) {
    return `${readme.slice(0, licenseMatch.index)}${section}\n${readme.slice(licenseMatch.index)}`;
  }

  return `${readme.trimEnd()}\n\n${section}`;
}

async function main() {
  const readmePath = path.resolve(README_FILE);
  const readme = fs.readFileSync(readmePath, "utf8");
  const api = await loadOpenApi();
  const groups = collectApiGroups(api);
  const apiList = renderApiList(groups);
  const section = buildReadmeSection(apiList);
  const updatedReadme = replaceApiListSection(readme, section);

  if (updatedReadme === readme) {
    console.log(`${README_FILE} is already up to date.`);
    return;
  }

  fs.writeFileSync(readmePath, updatedReadme);
  console.log(`Updated ${README_FILE} with ${groups.length} API group(s).`);
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : error);
  process.exit(1);
});
