import { useEffect, useState } from "react";
import { fetchProducts } from "../../api/products.js";
import { ProductCard } from "../../components/ui/ProductCard.jsx";

/**
 * Skeleton Loader Component
 */
function CatalogSkeleton() {
  return (
    <div className="animate-pulse">
      {/* Hero Skeleton */}
      <div className="mb-12 md:mb-16 rounded-2xl bg-[#eef1f3] h-[300px] md:h-[400px] w-full" />

      {/* Title Skeleton */}
      <div className="h-8 bg-[#dfe3e6] rounded-md w-48 mb-8" />

      {/* Grid Skeleton */}
      <div className="grid gap-6 md:gap-8 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {[1, 2, 3, 4, 5, 6, 7, 8].map((i) => (
          <div
            key={i}
            className="rounded-[0.75rem] bg-[#ffffff] p-4 flex flex-col gap-4"
          >
            <div className="h-64 sm:h-72 w-full bg-[#eef1f3] rounded-lg" />
            <div className="space-y-2">
              <div className="h-4 bg-[#dfe3e6] rounded w-3/4" />
              <div className="h-4 bg-[#dfe3e6] rounded w-1/4" />
            </div>
            <div className="h-10 bg-[#eef1f3] rounded-md mt-auto" />
          </div>
        ))}
      </div>
    </div>
  );
}

export function Catalog() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts()
      .then(setProducts)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <CatalogSkeleton />;

  return (
    <div className="w-full">
      {/* Hero Section */}
      <section className="mb-12 md:mb-20 overflow-hidden rounded-[1.25rem] bg-[#0050d4] bg-gradient-to-br from-[#0050d4] to-[#7b9cff] relative flex items-center min-h-[350px] md:min-h-[480px]">
        {/* Abstract decorative elements */}
        <div className="absolute top-0 right-0 -mr-32 -mt-32 w-96 h-96 rounded-full bg-[#ffffff] opacity-10 blur-3xl"></div>
        <div className="absolute bottom-0 left-0 -ml-24 -mb-24 w-72 h-72 rounded-full bg-[#ffffff] opacity-10 blur-2xl"></div>

        <div className="relative z-10 px-8 py-12 md:px-16 md:w-2/3 lg:w-1/2 text-left">
          <span className="inline-block text-[#f1f2ff] font-semibold tracking-wider uppercase text-sm mb-4 border border-[#f1f2ff]/30 px-3 py-1 rounded-full backdrop-blur-sm bg-white/10">
            Spring Collection 2026
          </span>
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight text-[#ffffff] font-['Manrope',sans-serif] leading-[1.1] mb-6">
            Curate Your Daily Aesthetic.
          </h1>
          <p className="text-lg md:text-xl text-[#edf3ff] mb-8 font-['Inter',sans-serif] max-w-lg leading-relaxed opacity-90">
            Discover our new arrivals featuring premium materials and
            uncompromising design language.
          </p>
          <button className="bg-[#ffffff] text-[#0050d4] font-medium text-base px-8 py-3.5 rounded-lg hover:bg-[#eef1f3] transition-colors shadow-[0_12px_40px_rgba(0,0,0,0.15)]">
            Explore Collection
          </button>
        </div>
      </section>

      {/* Product Grid Section */}
      <section>
        <div className="flex items-end justify-between mb-8">
          <h2 className="text-2xl md:text-3xl font-bold tracking-tight text-[#2c2f31] font-['Manrope',sans-serif]">
            Featured Pieces
          </h2>
          {/* Optional: Add a subtle sort/filter dropdown here later */}
        </div>

        {products.length === 0 ? (
          <div className="py-20 text-center text-[#595c5e] bg-[#ffffff] rounded-xl border border-[#eef1f3]">
            <p className="text-lg">No products currently available.</p>
          </div>
        ) : (
          <div className="grid gap-6 md:gap-8 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {products.map((p) => (
              <ProductCard
                key={p.id}
                name={p.name}
                price={`$${p.price.toFixed(2)}`}
                imageUrl="/placeholder.svg"
                onAddToCart={() => {}}
              />
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
