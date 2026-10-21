import { Link, NavLink, useLocation } from "react-router-dom";
import { ShoppingCart, User, Menu, X, Search } from "lucide-react";
import { useState, useEffect, useRef } from "react";

export function AppShell({ children }) {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const location = useLocation();
  const isInitialMount = useRef(true);

  // Handle SPA routing accessibility (Title update & Focus management)
  useEffect(() => {
    const titles = {
      '/': 'ShopSphere - Curated Aesthetics',
      '/products': 'Products | ShopSphere',
      '/cart': 'Your Cart | ShopSphere',
      '/auth': 'Login | ShopSphere',
      '/account': 'Your Account | ShopSphere',
    };
    document.title = titles[location.pathname] || 'ShopSphere';

    if (isInitialMount.current) {
      isInitialMount.current = false;
      return;
    }

    // Reset scroll position to top on route change for predictable native-like navigation
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });

    const main = document.getElementById('main-content');
    if (main) {
      main.focus({ preventScroll: true });
    }

    setIsMobileMenuOpen(false);
  }, [location.pathname]);

  useEffect(() => {
    if (isMobileMenuOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }

    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isMobileMenuOpen) {
        setIsMobileMenuOpen(false);
        const toggleBtn = document.querySelector('[aria-controls="mobile-navigation-menu"]');
        if (toggleBtn) toggleBtn.focus();
      }

      // Global shortcut for Search
      if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(e.target.tagName)) {
        e.preventDefault();
        const searchBtn = document.querySelector('[aria-label^="Search"]');
        if (searchBtn) searchBtn.focus();
      }
    };

    const handleClickOutside = (e) => {
      const menu = document.getElementById('mobile-navigation-menu');
      const toggle = document.querySelector('[aria-controls="mobile-navigation-menu"]');
      if (isMobileMenuOpen && menu && !menu.contains(e.target) && toggle && !toggle.contains(e.target)) {
        setIsMobileMenuOpen(false);
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    document.addEventListener('mousedown', handleClickOutside);
    document.addEventListener('touchstart', handleClickOutside);
    return () => {
      document.body.style.overflow = "";
      document.removeEventListener('keydown', handleKeyDown);
      document.removeEventListener('mousedown', handleClickOutside);
      document.removeEventListener('touchstart', handleClickOutside);
    };
  }, [isMobileMenuOpen]);

  return (
    <div className="min-h-screen bg-[#f5f7f9] text-[#2c2f31] font-['Inter',sans-serif]">
      {/* Skip to main content link for accessibility */}
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-[100] focus:px-4 focus:py-2 focus:bg-[#0050d4] focus:text-[#ffffff] focus:font-medium focus:rounded-md focus:outline-none focus:ring-2 focus:ring-[#0050d4] focus:ring-offset-2"
      >
        Skip to main content
      </a>

      {/* Mobile Menu Backdrop */}
      {isMobileMenuOpen && (
        <div
          className="md:hidden fixed inset-0 z-40 bg-[#2c2f31]/20 backdrop-blur-sm transition-opacity"
          aria-hidden="true"
          onClick={() => setIsMobileMenuOpen(false)}
        />
      )}

      {/* Header */}
      <header className="sticky top-0 z-50 bg-[#f5f7f9]/80 backdrop-blur-xl border-b border-[#eef1f3]">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:py-5">
          {/* Logo */}
          <Link
            to="/"
            className="text-2xl font-bold tracking-tight text-[#2c2f31] font-['Manrope',sans-serif] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm"
          >
            ShopSphere
          </Link>

          {/* Desktop Navigation */}
          <nav aria-label="Desktop" className="hidden md:flex gap-8 text-[0.875rem] font-medium">
            <NavLink
              to="/"
              className={({ isActive }) => `transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm px-1 py-0.5 ${isActive ? "text-[#0050d4] font-semibold underline underline-offset-[6px] decoration-2" : "text-[#595c5e] hover:text-[#0050d4]"}`}
            >
              Home
            </NavLink>
            <NavLink
              to="/products"
              className={({ isActive }) => `transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm px-1 py-0.5 ${isActive ? "text-[#0050d4] font-semibold underline underline-offset-[6px] decoration-2" : "text-[#595c5e] hover:text-[#0050d4]"}`}
            >
              Products
            </NavLink>
          </nav>

          {/* Desktop Actions */}
          <div className="hidden md:flex items-center gap-2">
            <button
              aria-label="Search"
              title="Search (Press / to focus)"
              aria-keyshortcuts="/"
              className="group flex items-center gap-1.5 p-2 text-[#595c5e] hover:bg-[#eef1f3] hover:text-[#0050d4] transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md"
            >
              <Search className="w-5 h-5" aria-hidden="true" />
              <kbd className="hidden lg:inline-flex items-center justify-center px-1.5 py-0.5 rounded-[4px] border border-[#dfe3e6] text-[11px] font-sans font-medium text-[#595c5e] bg-[#f5f7f9] group-hover:border-[#0050d4]/30 group-hover:text-[#0050d4] group-hover:bg-[#ffffff] transition-colors" aria-hidden="true">
                /
              </kbd>
            </button>
            <NavLink
              to="/account"
              aria-label="Account"
              title="Account"
              className={({ isActive }) => `p-2 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md ${isActive ? "bg-[#eef1f3] text-[#0050d4]" : "text-[#595c5e] hover:bg-[#eef1f3] hover:text-[#0050d4]"}`}
            >
              <User className="w-5 h-5" aria-hidden="true" />
            </NavLink>
            <NavLink
              to="/cart"
              aria-label="Cart"
              title="Cart"
              className={({ isActive }) => `relative p-2 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md ${isActive ? "bg-[#eef1f3] text-[#0050d4]" : "text-[#595c5e] hover:bg-[#eef1f3] hover:text-[#0050d4]"}`}
            >
              <ShoppingCart className="w-5 h-5" aria-hidden="true" />
              {/* Optional Cart Badge */}
              {/* <span className="absolute top-0 right-0 flex h-4 w-4 items-center justify-center rounded-full bg-[#0050d4] text-[10px] font-bold text-white">2</span> */}
            </NavLink>
          </div>

          {/* Mobile Menu Toggle */}
          <button
            className="md:hidden p-2 text-[#2c2f31] hover:bg-[#eef1f3] transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            aria-label={isMobileMenuOpen ? "Close Menu" : "Open Menu"}
            title={isMobileMenuOpen ? "Close Menu" : "Open Menu"}
            aria-expanded={isMobileMenuOpen}
            aria-controls="mobile-navigation-menu"
          >
            {isMobileMenuOpen ? (
              <X className="w-6 h-6" aria-hidden="true" />
            ) : (
              <Menu className="w-6 h-6" aria-hidden="true" />
            )}
          </button>
        </div>

        {/* Mobile Navigation Dropdown */}
        {isMobileMenuOpen && (
          <div id="mobile-navigation-menu" className="md:hidden absolute top-full left-0 w-full bg-[#ffffff] border-b border-[#eef1f3] shadow-lg">
            <nav aria-label="Mobile" className="flex flex-col px-6 py-4 gap-4 text-base font-medium">
              <NavLink
                to="/"
                onClick={() => setIsMobileMenuOpen(false)}
                className={({ isActive }) => `transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md px-3 py-2 ${isActive ? "bg-[#eef1f3] text-[#0050d4] font-semibold" : "text-[#2c2f31] hover:bg-[#f5f7f9] hover:text-[#0050d4]"}`}
              >
                Home
              </NavLink>
              <NavLink
                to="/products"
                onClick={() => setIsMobileMenuOpen(false)}
                className={({ isActive }) => `transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md px-3 py-2 ${isActive ? "bg-[#eef1f3] text-[#0050d4] font-semibold" : "text-[#2c2f31] hover:bg-[#f5f7f9] hover:text-[#0050d4]"}`}
              >
                Products
              </NavLink>
              <NavLink
                to="/cart"
                onClick={() => setIsMobileMenuOpen(false)}
                className={({ isActive }) => `flex items-center justify-between transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md px-3 py-2 ${isActive ? "bg-[#eef1f3] text-[#0050d4] font-semibold" : "text-[#2c2f31] hover:bg-[#f5f7f9] hover:text-[#0050d4]"}`}
              >
                Cart
                <ShoppingCart className="w-5 h-5" aria-hidden="true" />
              </NavLink>
              <NavLink
                to="/account"
                onClick={() => setIsMobileMenuOpen(false)}
                className={({ isActive }) => `flex items-center justify-between transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-md px-3 py-2 ${isActive ? "bg-[#eef1f3] text-[#0050d4] font-semibold" : "text-[#2c2f31] hover:bg-[#f5f7f9] hover:text-[#0050d4]"}`}
              >
                Account
                <User className="w-5 h-5" aria-hidden="true" />
              </NavLink>
            </nav>
          </div>
        )}
      </header>

      {/* Main Content Area */}
      <main id="main-content" tabIndex={-1} className="mx-auto max-w-7xl px-6 py-8 md:py-12 lg:py-16 focus:outline-none">
        {children}
      </main>

      {/* Footer */}
      <footer className="mt-auto bg-[#ffffff]">
        <div className="mx-auto max-w-7xl px-6 py-12 lg:py-16">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div className="md:col-span-1">
              <span className="text-xl font-bold tracking-tight text-[#2c2f31] font-['Manrope',sans-serif]">
                ShopSphere
              </span>
              <p className="mt-4 text-[0.875rem] text-[#595c5e]">
                Curating the exceptional. Designed for the discerning digital
                native.
              </p>
            </div>
            <div>
              <h3 className="font-semibold text-[#2c2f31] mb-4">Shop</h3>
              <ul className="space-y-3 text-[0.875rem] text-[#595c5e]">
                <li>
                  <Link to="/products" className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block">
                    All Products
                  </Link>
                </li>
                <li>
                  <Link
                    to="/products?category=new"
                    className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block"
                  >
                    New Arrivals
                  </Link>
                </li>
                <li>
                  <Link
                    to="/products?category=sale"
                    className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block"
                  >
                    Sale
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold text-[#2c2f31] mb-4">Support</h3>
              <ul className="space-y-3 text-[0.875rem] text-[#595c5e]">
                <li>
                  <a href="#" className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block">
                    FAQ
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block">
                    Shipping & Returns
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block">
                    Contact Us
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold text-[#2c2f31] mb-4">Legal</h3>
              <ul className="space-y-3 text-[0.875rem] text-[#595c5e]">
                <li>
                  <a href="#" className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block">
                    Privacy Policy
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-[#0050d4] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] rounded-sm inline-block">
                    Terms of Service
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div className="mt-12 border-t border-[#eef1f3] pt-8 flex flex-col md:flex-row items-center justify-between text-[0.875rem] text-[#595c5e]">
            <p>© 2026 ShopSphere. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
