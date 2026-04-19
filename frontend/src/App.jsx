import { lazy, Suspense } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AppShell } from "./components/layout/AppShell.jsx";

// ⚡ Bolt: Implemented code splitting for route components
// This prevents loading all feature bundles (Catalog, Cart, Auth, Account) on initial load,
// significantly reducing the initial JavaScript payload and improving Time to Interactive (TTI).
const Catalog = lazy(() =>
  import("./features/catalog/Catalog.jsx").then((module) => ({
    default: module.Catalog,
  }))
);
const Cart = lazy(() =>
  import("./features/cart/Cart.jsx").then((module) => ({
    default: module.Cart,
  }))
);
const Auth = lazy(() =>
  import("./features/auth/Auth.jsx").then((module) => ({
    default: module.Auth,
  }))
);
const Account = lazy(() =>
  import("./features/account/Account.jsx").then((module) => ({
    default: module.Account,
  }))
);

export default function App() {
  return (
    <BrowserRouter>
      <AppShell>
        <Suspense
          fallback={
            <div className="flex justify-center items-center py-20">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#0050d4]"></div>
            </div>
          }
        >
          <Routes>
            <Route path="/" element={<Catalog />} />
            <Route path="/products" element={<Catalog />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/auth" element={<Auth />} />
            <Route path="/account" element={<Account />} />
          </Routes>
        </Suspense>
      </AppShell>
    </BrowserRouter>
  );
}
