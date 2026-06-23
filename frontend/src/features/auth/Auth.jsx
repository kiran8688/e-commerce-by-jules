export function Auth() {
  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Login</h1>
      <form className="space-y-4">
        <div>
          <label htmlFor="email" className="block text-sm font-medium">Email</label>
          <input id="email" type="email" required autoComplete="email" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-slate-900" />
        </div>
        <div>
          <label htmlFor="password" className="block text-sm font-medium">Password</label>
          <input id="password" type="password" required autoComplete="current-password" className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-slate-900" />
        </div>
        <button type="submit" className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-slate-900 hover:bg-slate-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-slate-900 focus-visible:ring-offset-2">
          Sign In
        </button>
      </form>
    </div>
  );
}