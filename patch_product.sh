cat << 'DIFF' > patch.diff
--- frontend/src/components/ui/ProductCard.jsx
+++ frontend/src/components/ui/ProductCard.jsx
@@ -15,10 +15,10 @@
         />
         {/* Quick Add Overlay on Desktop */}
-        <div className="absolute inset-x-0 bottom-0 p-4 opacity-0 transition-opacity duration-300 group-hover:opacity-100 hidden lg:block bg-gradient-to-t from-black/60 to-transparent">
+        <div className="absolute inset-x-0 bottom-0 p-4 opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 hidden lg:block bg-gradient-to-t from-black/60 to-transparent">
           <button
             onClick={onAddToCart}
-            className="w-full rounded-[0.375rem] bg-[#0050d4] bg-gradient-to-r from-[#0050d4] to-[#7b9cff] px-4 py-3 text-sm font-medium text-[#f1f2ff] shadow-sm hover:from-[#0046bb] hover:to-[#658eff] transition-all flex items-center justify-center gap-2"
+            className="w-full rounded-[0.375rem] bg-[#0050d4] bg-gradient-to-r from-[#0050d4] to-[#7b9cff] px-4 py-3 text-sm font-medium text-[#f1f2ff] shadow-sm hover:from-[#0046bb] hover:to-[#658eff] transition-all flex items-center justify-center gap-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-[#0050d4]"
           >
             <ShoppingCart className="w-4 h-4" />
             Quick Add
@@ -35,7 +35,7 @@
         {/* Mobile Add to Cart (Visible on smaller screens, hidden on LG where quick add appears) */}
         <button
           onClick={onAddToCart}
-          className="mt-4 lg:hidden w-full rounded-[0.375rem] bg-[#eef1f3] px-4 py-2.5 text-sm font-medium text-[#2c2f31] hover:bg-[#dfe3e6] transition-colors flex items-center justify-center gap-2"
+          className="mt-4 lg:hidden w-full rounded-[0.375rem] bg-[#eef1f3] px-4 py-2.5 text-sm font-medium text-[#2c2f31] hover:bg-[#dfe3e6] transition-colors flex items-center justify-center gap-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0050d4] focus-visible:ring-offset-2"
         >
           <ShoppingCart className="w-4 h-4 text-[#595c5e]" />
           Add to Cart
DIFF
patch frontend/src/components/ui/ProductCard.jsx < patch.diff
