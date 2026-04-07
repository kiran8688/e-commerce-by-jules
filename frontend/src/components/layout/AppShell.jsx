export function AppShell({ children }) {
  return (
    <div className="min-h-screen bg-white text-slate-900">
      <header className="border-b px-6 py-4">
        <div className="mx-auto flex max-w-7xl items-center justify-between">
          <div className="text-xl font-bold">ShopSphere</div>
          <nav className="flex gap-4 text-sm">
            <a href="/">Home</a>
            <a href="/products">Products</a>
            <a href="/cart">Cart</a>
            <a href="/account">Account</a>
          </nav>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-6 py-8">{children}</main>

      <footer className="border-t px-6 py-6 text-sm text-slate-500">
        © 2026 ShopSphere
      </footer>
    </div>
  );
}