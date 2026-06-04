import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Suspense, lazy } from 'react';
import { Provider } from 'react-redux';
import { store } from './store';
import { MainLayout } from './layouts/MainLayout';
import { AuthLayout } from './layouts/AuthLayout';
import { useAuth } from './hooks/useAuth';

const Login = lazy(() => import('./pages/Login'));
const Register = lazy(() => import('./pages/Register'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const ServiceCatalog = lazy(() => import('./pages/Services/ServiceCatalog'));
const NewApplication = lazy(() => import('./pages/Applications/NewApplication'));
const ApplicationDetail = lazy(() => import('./pages/Applications/ApplicationDetail'));
const Offline = lazy(() => import('./pages/Offline'));

function AppRoutes() {
  const { isAuthenticated } = useAuth();
  return (
    <Routes>
      <Route element={<AuthLayout />}>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Route>
      <Route element={<MainLayout />}>
        <Route path="/" element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />} />
        <Route path="/services" element={<ServiceCatalog />} />
        <Route path="/applications/new/:serviceId" element={<NewApplication />} />
        <Route path="/applications/:id" element={<ApplicationDetail />} />
      </Route>
      <Route path="/offline" element={<Offline />} />
    </Routes>
  );
}

function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <Suspense fallback={<div className="flex justify-center items-center h-screen"><span className="loading loading-spinner loading-lg"></span></div>}>
          <AppRoutes />
        </Suspense>
      </BrowserRouter>
    </Provider>
  );
}

export default App;