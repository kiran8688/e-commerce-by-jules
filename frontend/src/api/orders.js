import { apiFetch } from "./client.js";

export async function createOrder(userId, data) {
  return apiFetch(`/orders/${userId}`, {
    method: "POST",
    body: JSON.stringify(data),
  });
}

export async function fetchOrders(userId) {
  return apiFetch(`/orders/${userId}`);
}