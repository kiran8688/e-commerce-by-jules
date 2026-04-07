export function ProductCard({ name, price, imageUrl, onAddToCart }) {
  return (
    <div className="overflow-hidden rounded-2xl border shadow-sm">
      <img src={imageUrl} alt={name} className="h-56 w-full object-cover" />
      <div className="space-y-3 p-4">
        <h3 className="text-lg font-semibold">{name}</h3>
        <p className="text-sm text-slate-600">{price}</p>
        <button
          className="rounded-xl bg-slate-900 px-4 py-2 text-sm font-medium text-white"
          onClick={onAddToCart}
        >
          Add to cart
        </button>
      </div>
    </div>
  );
}