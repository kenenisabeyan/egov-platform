import { Link } from 'react-router-dom';

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <div className="hero bg-white dark:bg-gray-800 rounded-2xl shadow p-8">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-4xl font-bold">Welcome to CivicFlow</h1>
            <p className="py-6 text-gray-600 dark:text-gray-400">
              Access decentralized municipal government services, track your active applications, and check document validity instantly.
            </p>
            <Link to="/services" className="btn btn-primary">
              Get Started
            </Link>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="card bg-white dark:bg-gray-800 shadow">
          <div className="card-body">
            <h2 className="card-title text-blue-600 dark:text-blue-400">Active Applications</h2>
            <p className="text-3xl font-extrabold">0</p>
            <div className="card-actions justify-end">
              <span className="badge badge-neutral">Up to date</span>
            </div>
          </div>
        </div>
        <div className="card bg-white dark:bg-gray-800 shadow">
          <div className="card-body">
            <h2 className="card-title text-green-600 dark:text-green-400">Approved Documents</h2>
            <p className="text-3xl font-extrabold">0</p>
            <div className="card-actions justify-end">
              <span className="badge badge-neutral">No files</span>
            </div>
          </div>
        </div>
        <div className="card bg-white dark:bg-gray-800 shadow">
          <div className="card-body">
            <h2 className="card-title text-purple-600 dark:text-purple-400">Notifications</h2>
            <p className="text-3xl font-extrabold">0</p>
            <div className="card-actions justify-end">
              <span className="badge badge-neutral">None</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
