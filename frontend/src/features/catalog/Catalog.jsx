import { useEffect, useState } from "react";
import { fetchProducts } from "../../api/products.js";
import { ProductCard } from "../../components/ui/ProductCard.jsx";

export function Catalog() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts()
      .then(setProducts)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

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