import { useEffect, useState } from "react";
import { fetchProducts } from "../../api/products.js";
import { ProductCard } from "../../components/ui/ProductCard.jsx";

/**
 * Renders the primary product catalog grid.
 *
 * Design Decision:
 * We fetch data on component mount using `useEffect`. For a production e-commerce site,
 * this would likely be replaced by Server-Side Rendering (SSR) via Next.js or Remix,
 * or client-side caching via React Query / SWR to improve SEO and time-to-interactive.
 */
export function Catalog() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Initiate the network request to fetch product data from the FastAPI backend.
    fetchProducts()
      .then(setProducts)
      .catch(console.error) // Edge Case: Network failures are logged but currently not shown to the user. Future enhancement: add an ErrorBoundary or error state.
      .finally(() => setLoading(false));
  }, []);

  // Provide a loading skeleton or message to prevent layout shift while data is fetching.
  if (loading) return <div>Loading products...</div>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Catalog</h1>
      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        {products.map((p) => (
          <ProductCard
            key={p.id}
            name={p.name}
            price={`$${p.price.toFixed(2)}`}
            imageUrl="/placeholder.svg"
            onAddToCart={() => console.log("Add to cart", p.id)}
          />
        ))}
      </div>
    </div>
  );
}