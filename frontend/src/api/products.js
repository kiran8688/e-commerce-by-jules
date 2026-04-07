import { apiFetch } from "./client.js";

export async function fetchProducts() {
  return apiFetch("/products/");
}