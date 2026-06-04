import { Outlet } from 'react-router-dom';

export function AuthLayout() {
  return (
    <div className="auth-layout min-h-screen bg-gray-50 dark:bg-gray-900">
      <Outlet />
    </div>
  );
}
