import { useParams, useNavigate } from 'react-router-dom';
import { useState } from 'react';

export default function NewApplication() {
  const { serviceId } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ fullName: '', phone: '', remarks: '' });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    alert(`Application for service ID ${serviceId} submitted successfully!`);
    navigate('/');
  };

  return (
    <div className="max-w-xl mx-auto bg-white dark:bg-gray-800 rounded-2xl shadow p-8 space-y-6">
      <h1 className="text-3xl font-bold text-gray-900 dark:text-white">New Service Application</h1>
      <p className="text-sm text-gray-500 dark:text-gray-400">
        Service Code: <span className="font-semibold text-blue-600">{serviceId}</span>
      </p>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-1">Full Name</label>
          <input
            type="text"
            className="w-full p-3 border rounded-lg dark:bg-gray-700 dark:text-white"
            placeholder="John Doe"
            value={formData.fullName}
            onChange={e => setFormData({ ...formData, fullName: e.target.value })}
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Phone Number</label>
          <input
            type="tel"
            className="w-full p-3 border rounded-lg dark:bg-gray-700 dark:text-white"
            placeholder="+251-..."
            value={formData.phone}
            onChange={e => setFormData({ ...formData, phone: e.target.value })}
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Remarks / Details</label>
          <textarea
            className="w-full p-3 border rounded-lg dark:bg-gray-700 dark:text-white h-32"
            placeholder="Provide details about your application..."
            value={formData.remarks}
            onChange={e => setFormData({ ...formData, remarks: e.target.value })}
          />
        </div>
        <div className="flex gap-4 pt-2">
          <button type="submit" className="btn btn-primary flex-1">
            Submit Application
          </button>
          <button type="button" onClick={() => navigate('/services')} className="btn btn-outline">
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}
