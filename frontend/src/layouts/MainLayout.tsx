import { Outlet, Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { logOut } from '../store/authSlice';
import { useAuth } from '../hooks/useAuth';

export function MainLayout() {
  const { user } = useAuth();
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logOut());
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100 flex flex-col">
      {/* Top Navbar */}
      <header className="bg-white dark:bg-gray-800 shadow-md px-6 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-blue-600 dark:text-blue-400">
          CivicFlow e-Gov
        </Link>
        <div className="flex items-center gap-4">
          {user && (
            <span className="text-sm font-medium">
              {user.username} ({user.role})
            </span>
          )}
          <button
            onClick={handleLogout}
            className="btn btn-sm btn-outline btn-error"
          >
            Logout
          </button>
        </div>
      </header>

      {/* Main Container */}
      <div className="flex flex-1">
        {/* Sidebar */}
        <aside className="w-64 bg-white dark:bg-gray-800 border-r border-gray-200 dark:border-gray-700 p-4 hidden md:block">
          <nav className="flex flex-col gap-2">
            <Link to="/" className="btn btn-ghost justify-start">
              Dashboard
            </Link>
            <Link to="/services" className="btn btn-ghost justify-start">
              Services Catalog
            </Link>
          </nav>
        </aside>

        {/* Content Area */}
        <main className="flex-1 p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
