import { Link } from 'react-router-dom';

const SERVICES = [
  { id: '1', name: 'Business License Registration', dept: 'Trade & Industry', description: 'Apply for or renew your local business operating license.' },
  { id: '2', name: 'ID / Passport Issuance', dept: 'Vital Statistics', description: 'Schedule appointment or apply for national ID/Passport renewals.' },
  { id: '3', name: 'Land & Property Registry', dept: 'Urban Development', description: 'Register property transfers, land usage, or deeds.' },
  { id: '4', name: 'Municipal Tax Payment', dept: 'Finance & Revenue', description: 'View statements and submit payments for property or sales taxes.' }
];

export default function ServiceCatalog() {
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Municipal Services Catalog</h1>
      <p className="text-gray-600 dark:text-gray-400">
        Choose a government service to launch an online application.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {SERVICES.map(service => (
          <div key={service.id} className="card bg-white dark:bg-gray-800 shadow hover:shadow-lg transition">
            <div className="card-body">
              <span className="text-xs uppercase tracking-wider font-semibold text-blue-600 dark:text-blue-400">
                {service.dept}
              </span>
              <h2 className="card-title text-xl font-bold mt-1">{service.name}</h2>
              <p className="text-sm text-gray-600 dark:text-gray-400 mt-2">{service.description}</p>
              <div className="card-actions justify-end mt-4">
                <Link to={`/applications/new/${service.id}`} className="btn btn-primary btn-sm">
                  Apply Now
                </Link>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
