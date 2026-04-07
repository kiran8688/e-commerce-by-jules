import { apiFetch } from "./client.js";

export async function login(credentials) {
  return apiFetch("/auth/login", {
    method: "POST",
    body: JSON.stringify(credentials),
  });
}

export async function register(data) {
  return apiFetch("/auth/register", {
    method: "POST",
    body: JSON.stringify(data),
  });
}