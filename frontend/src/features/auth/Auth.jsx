export function Auth() {
  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Login</h1>
      <form className="space-y-4">
        <div>
          <label htmlFor="email" className="block text-sm font-medium">
            Email{" "}
            <span className="text-red-500" aria-hidden="true">
              *
            </span>
          </label>
          <input
            id="email"
            type="email"
            required
            autoComplete="email"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2 focus:ring-2 focus:ring-slate-900 focus:border-slate-900 focus:outline-none transition-shadow"
          />
        </div>
        <div>
          <label htmlFor="password" className="block text-sm font-medium">
            Password{" "}
            <span className="text-red-500" aria-hidden="true">
              *
            </span>
          </label>
          <input
            id="password"
            type="password"
            required
            autoComplete="current-password"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2 focus:ring-2 focus:ring-slate-900 focus:border-slate-900 focus:outline-none transition-shadow"
          />
        </div>
        <button
          type="submit"
          className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-slate-900 hover:bg-slate-800 focus:ring-2 focus:ring-offset-2 focus:ring-slate-900 focus:outline-none transition-all"
        >
          Sign In
        </button>
      </form>
    </div>
  );
}
