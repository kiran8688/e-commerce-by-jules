import { ShoppingCart } from "lucide-react";

export function ProductCard({ name, price, imageUrl, onAddToCart }) {
  return (
    <div className="group flex flex-col overflow-hidden rounded-[0.75rem] bg-[#ffffff] transition-all duration-300 hover:shadow-[0_12px_40px_rgba(44,47,49,0.06)] hover:-translate-y-1 h-full">
      {/* Image Container with 4:5 Aspect Ratio for Editorial Feel */}
      <div
        className="relative w-full overflow-hidden bg-[#eef1f3]"
        style={{ paddingBottom: "125%" }}
      >
        <img
          src={imageUrl}
          alt={name}
          className="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
          loading="lazy"
        />
        {/* Quick Add Overlay on Desktop */}
        <div className="absolute inset-x-0 bottom-0 p-4 opacity-0 transition-opacity duration-300 group-hover:opacity-100 hidden lg:block bg-gradient-to-t from-black/60 to-transparent">
          <button
            onClick={onAddToCart}
            className="w-full rounded-[0.375rem] bg-[#0050d4] bg-gradient-to-r from-[#0050d4] to-[#7b9cff] px-4 py-3 text-sm font-medium text-[#f1f2ff] shadow-sm hover:from-[#0046bb] hover:to-[#658eff] transition-all flex items-center justify-center gap-2"
          >
            <ShoppingCart className="w-4 h-4" />
            Quick Add
          </button>
        </div>
      </div>

      {/* Product Info */}
      <div className="flex flex-1 flex-col p-5">
        <h3 className="text-lg font-semibold text-[#2c2f31] font-['Inter',sans-serif] leading-tight mb-1.5 group-hover:text-[#0050d4] transition-colors line-clamp-2">
          {name}
        </h3>
        <p className="text-base font-medium text-[#595c5e] mt-auto">{price}</p>

        {/* Mobile Add to Cart (Visible on smaller screens, hidden on LG where quick add appears) */}
        <button
          onClick={onAddToCart}
          className="mt-4 lg:hidden w-full rounded-[0.375rem] bg-[#eef1f3] px-4 py-2.5 text-sm font-medium text-[#2c2f31] hover:bg-[#dfe3e6] transition-colors flex items-center justify-center gap-2"
        >
          <ShoppingCart className="w-4 h-4 text-[#595c5e]" />
          Add to Cart
        </button>
      </div>
    </div>
  );
}
