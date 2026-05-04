import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AppShell } from "./components/layout/AppShell.jsx";
import { Catalog } from "./features/catalog/Catalog.jsx";
import { Cart } from "./features/cart/Cart.jsx";
import { Auth } from "./features/auth/Auth.jsx";
import { Account } from "./features/account/Account.jsx";

export default function App() {
  return (
    <BrowserRouter>
      <AppShell>
        <Routes>
          <Route path="/" element={<Catalog />} />
          <Route path="/products" element={<Catalog />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/auth" element={<Auth />} />
          <Route path="/account" element={<Account />} />
        </Routes>
      </AppShell>
    </BrowserRouter>
  );
}
