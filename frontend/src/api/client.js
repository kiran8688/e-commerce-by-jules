// Resolve the API base URL from Vite environment variables (fallback to local dev if not set).
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000/api/v1";

/**
 * Central fetch abstraction wrapper.
 *
 * Design Decision:
 * Why wrap `fetch` instead of using a library like `axios` or calling `fetch` directly everywhere?
 * 1. Consistency: It ensures every outgoing request has the correct `Content-Type` and base URL.
 * 2. Error Handling: It intercepts non-2xx responses and throws them as standard JS Errors,
 *    allowing components to use simple `try/catch` blocks.
 * 3. Future Proofing: If we implement JWT Bearer tokens, we only have to inject the `Authorization`
 *    header in this one file, rather than across 50 different React components.
 */
export async function apiFetch(path, init = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init.headers ?? {}),
    },
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || "Request failed");
  }

  return await response.json();
}
