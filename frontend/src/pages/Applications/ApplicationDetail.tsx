import { useParams, Link } from 'react-router-dom';

export default function ApplicationDetail() {
  const { id } = useParams();

  return (
    <div className="max-w-xl mx-auto bg-white dark:bg-gray-800 rounded-2xl shadow p-8 space-y-6">
      <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Application Tracking</h1>
      <p className="text-sm text-gray-500 dark:text-gray-400">
        Application ID: <span className="font-semibold text-blue-600">{id}</span>
      </p>

      <div className="border border-gray-200 dark:border-gray-700 rounded-xl p-4 space-y-3 bg-gray-50 dark:bg-gray-700">
        <div className="flex justify-between">
          <span className="font-medium text-gray-500 dark:text-gray-400">Status</span>
          <span className="badge badge-success font-semibold text-white">Submitted</span>
        </div>
        <div className="flex justify-between">
          <span className="font-medium text-gray-500 dark:text-gray-400">Submitted On</span>
          <span>{new Date().toLocaleDateString()}</span>
        </div>
        <div className="flex justify-between">
          <span className="font-medium text-gray-500 dark:text-gray-400">Office Assignment</span>
          <span>Municipal Trade Department</span>
        </div>
      </div>

      <div className="flex gap-4">
        <Link to="/" className="btn btn-outline flex-1">
          Back to Dashboard
        </Link>
      </div>
    </div>
  );
}
