export default function Offline() {
  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 flex items-center justify-center p-4">
      <div className="text-center space-y-4 max-w-md bg-white dark:bg-gray-800 p-8 rounded-2xl shadow">
        <h1 className="text-5xl">📡</h1>
        <h2 className="text-3xl font-bold text-gray-900 dark:text-white">You're Offline</h2>
        <p className="text-gray-600 dark:text-gray-400">
          We can't connect to CivicFlow e-Gov right now. Please check your internet connection and try again.
        </p>
        <button
          onClick={() => window.location.reload()}
          className="btn btn-primary"
        >
          Retry Connection
        </button>
      </div>
    </div>
  );
}
