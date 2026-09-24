import { useState } from "react";
import { Eye, EyeOff } from "lucide-react";

export function Auth() {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Login</h1>
      <form className="space-y-4">
        <div>
          <label htmlFor="email" className="block text-sm font-medium">Email <span className="text-red-500" aria-hidden="true">*</span></label>
          <input id="email" name="email" type="email" required autoComplete="email" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2 focus:ring-2 focus:ring-slate-900 focus:border-slate-900 focus:outline-none transition-shadow" />
        </div>
        <div>
          <label htmlFor="password" className="block text-sm font-medium">Password <span className="text-red-500" aria-hidden="true">*</span></label>
          <div className="relative mt-1">
            <input
              id="password"
              name="password"
              type={showPassword ? "text" : "password"}
              required
              autoComplete="current-password"
              className="block w-full rounded-md border-gray-300 shadow-sm border p-2 pr-10 focus:ring-2 focus:ring-slate-900 focus:border-slate-900 focus:outline-none transition-shadow"
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              aria-label={showPassword ? "Hide password" : "Show password"}
              className="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-500 hover:text-gray-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-slate-900 rounded-md"
            >
              {showPassword ? <EyeOff className="h-5 w-5" aria-hidden="true" /> : <Eye className="h-5 w-5" aria-hidden="true" />}
            </button>
          </div>
        </div>
        <button type="submit" className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-slate-900 hover:bg-slate-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-900 transition-colors">
          Sign In
        </button>
      </form>
    </div>
  );
}