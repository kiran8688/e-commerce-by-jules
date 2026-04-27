import { Link } from "react-router-dom";
import { ShoppingCart, User, Menu, X, Search } from "lucide-react";
import { useState } from "react";

export function AppShell({ children }) {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <div className="min-h-screen bg-[#f5f7f9] text-[#2c2f31] font-['Inter',sans-serif]">
      {/* Header */}
      <header className="sticky top-0 z-50 bg-[#f5f7f9]/80 backdrop-blur-xl border-b border-[#eef1f3]">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:py-5">
          {/* Logo */}
          <Link
            to="/"
            className="text-2xl font-bold tracking-tight text-[#2c2f31] font-['Manrope',sans-serif]"
          >
            ShopSphere
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex gap-8 text-[0.875rem] font-medium">
            <Link
              to="/"
              className="text-[#595c5e] hover:text-[#0050d4] transition-colors"
            >
              Home
            </Link>
            <Link
              to="/products"
              className="text-[#595c5e] hover:text-[#0050d4] transition-colors"
            >
              Products
            </Link>
          </nav>

          {/* Desktop Actions */}
          <div className="hidden md:flex items-center gap-6">
            <button
              aria-label="Search"
              title="Search"
              className="text-[#595c5e] hover:text-[#0050d4] transition-colors focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:outline-none rounded-sm"
            >
              <Search className="w-5 h-5" />
            </button>
            <Link
              to="/account"
              aria-label="Account"
              title="Account"
              className="text-[#595c5e] hover:text-[#0050d4] transition-colors focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:outline-none rounded-sm"
            >
              <User className="w-5 h-5" />
            </Link>
            <Link
              to="/cart"
              aria-label="Cart"
              title="Cart"
              className="relative text-[#595c5e] hover:text-[#0050d4] transition-colors focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:outline-none rounded-sm"
            >
              <ShoppingCart className="w-5 h-5" />
              {/* Optional Cart Badge */}
              {/* <span className="absolute -top-1.5 -right-1.5 flex h-4 w-4 items-center justify-center rounded-full bg-[#0050d4] text-[10px] font-bold text-white">2</span> */}
            </Link>
          </div>

          {/* Mobile Menu Toggle */}
          <button
            className="md:hidden text-[#2c2f31] focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:outline-none rounded-sm"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            aria-label={isMobileMenuOpen ? "Close Menu" : "Open Menu"}
            title={isMobileMenuOpen ? "Close Menu" : "Open Menu"}
            aria-expanded={isMobileMenuOpen}
          >
            {isMobileMenuOpen ? (
              <X className="w-6 h-6" />
            ) : (
              <Menu className="w-6 h-6" />
            )}
          </button>
        </div>

        {/* Mobile Navigation Dropdown */}
        {isMobileMenuOpen && (
          <div className="md:hidden absolute top-full left-0 w-full bg-[#ffffff] border-b border-[#eef1f3] shadow-lg">
            <nav className="flex flex-col px-6 py-4 gap-4 text-base font-medium">
              <Link
                to="/"
                onClick={() => setIsMobileMenuOpen(false)}
                className="text-[#2c2f31] hover:text-[#0050d4]"
              >
                Home
              </Link>
              <Link
                to="/products"
                onClick={() => setIsMobileMenuOpen(false)}
                className="text-[#2c2f31] hover:text-[#0050d4]"
              >
                Products
              </Link>
              <Link
                to="/cart"
                onClick={() => setIsMobileMenuOpen(false)}
                className="text-[#2c2f31] hover:text-[#0050d4] flex items-center justify-between"
              >
                Cart
                <ShoppingCart className="w-5 h-5" />
              </Link>
              <Link
                to="/account"
                onClick={() => setIsMobileMenuOpen(false)}
                className="text-[#2c2f31] hover:text-[#0050d4] flex items-center justify-between"
              >
                Account
                <User className="w-5 h-5" />
              </Link>
            </nav>
          </div>
        )}
      </header>

      {/* Main Content Area */}
      <main className="mx-auto max-w-7xl px-6 py-8 md:py-12 lg:py-16">
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
                  <Link to="/products" className="hover:text-[#0050d4]">
                    All Products
                  </Link>
                </li>
                <li>
                  <Link
                    to="/products?category=new"
                    className="hover:text-[#0050d4]"
                  >
                    New Arrivals
                  </Link>
                </li>
                <li>
                  <Link
                    to="/products?category=sale"
                    className="hover:text-[#0050d4]"
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
                  <a href="#" className="hover:text-[#0050d4]">
                    FAQ
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-[#0050d4]">
                    Shipping & Returns
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-[#0050d4]">
                    Contact Us
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold text-[#2c2f31] mb-4">Legal</h3>
              <ul className="space-y-3 text-[0.875rem] text-[#595c5e]">
                <li>
                  <a href="#" className="hover:text-[#0050d4]">
                    Privacy Policy
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-[#0050d4]">
                    Terms of Service
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div className="mt-12 border-t border-[#eef1f3] pt-8 flex flex-col md:flex-row items-center justify-between text-[0.875rem] text-[#abadaf]">
            <p>© 2026 ShopSphere. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
