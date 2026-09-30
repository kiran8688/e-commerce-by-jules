import { apiFetch } from "./client.js";

// ⚡ Bolt: Cache product list with a 5-minute TTL to prevent redundant network
// requests on navigation, while ensuring resilience against transient failures.
let productsCache = null;
let fetchPromise = null;
let cacheTimestamp = 0;
const CACHE_TTL = 5 * 60 * 1000; // 5 minutes

export async function fetchProducts() {
  const now = Date.now();
  if (productsCache && (now - cacheTimestamp < CACHE_TTL)) {
    return productsCache;
  }

  if (fetchPromise) return fetchPromise;

  fetchPromise = apiFetch("/products/")
    .then(data => {
      productsCache = data;
      cacheTimestamp = Date.now();
      return data;
    })
    .finally(() => {
      fetchPromise = null;
    });

  return fetchPromise;
}