export function Auth() {
  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Login</h1>
      <form className="space-y-4">
        <div>
          <label htmlFor="email" className="block text-sm font-medium">Email <span className="text-red-500">*</span></label>
          <input id="email" type="email" autoComplete="email" required className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2 focus:ring-2 focus:ring-slate-900 focus:outline-none" />
        </div>
        <div>
          <label htmlFor="password" className="block text-sm font-medium">Password <span className="text-red-500">*</span></label>
          <input id="password" type="password" autoComplete="current-password" required className="mt-1 block w-full rounded-md border-gray-300 shadow-sm border p-2 focus:ring-2 focus:ring-slate-900 focus:outline-none" />
        </div>
        <button type="submit" className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-slate-900 hover:bg-slate-800 focus:ring-2 focus:ring-slate-900 focus:ring-offset-2 focus:outline-none">
          Sign In
        </button>
      </form>
    </div>
  );
}