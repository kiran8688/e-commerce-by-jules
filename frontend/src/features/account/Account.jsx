import { Package } from "lucide-react";
import { Link } from "react-router-dom";

export function Account() {
  return (
    <div className="w-full max-w-4xl mx-auto">
      <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight text-[#2c2f31] font-['Manrope',sans-serif] mb-8 border-b border-[#eef1f3] pb-6">
        Your Account
      </h1>

      <div className="flex flex-col items-center justify-center py-16 md:py-24 px-6 text-center bg-[#ffffff] rounded-[1.25rem] shadow-[0_12px_40px_rgba(44,47,49,0.03)] border border-[#eef1f3]/50">
        <div className="w-20 h-20 bg-[#eef1f3] rounded-full flex items-center justify-center mb-6">
          <Package className="w-10 h-10 text-[#abadaf]" strokeWidth={1.5} aria-hidden="true" />
        </div>
        <h2 className="text-2xl font-bold text-[#2c2f31] mb-3 font-['Manrope',sans-serif]">
          Welcome to your dashboard
        </h2>
        <p className="text-[#595c5e] max-w-md mb-8 leading-relaxed font-['Inter',sans-serif]">
          You haven't placed any orders yet. Discover our latest arrivals and find something exceptional.
        </p>
        <Link
          to="/products"
          className="inline-flex items-center justify-center rounded-[0.375rem] bg-[#0050d4] bg-gradient-to-r from-[#0050d4] to-[#7b9cff] px-8 py-3.5 text-base font-medium text-[#f1f2ff] shadow-sm hover:from-[#0046bb] hover:to-[#658eff] transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:ring-offset-2"
        >
          Start Shopping
        </Link>
      </div>
    </div>
  );
}