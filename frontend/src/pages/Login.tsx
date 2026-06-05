import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { motion } from 'framer-motion';
import { setCredentials } from '../store/authSlice';
import { useLoginMutation } from '../services/authApi';
import { ThemeToggle } from '../components/common/ThemeToggle';
import { LanguageSwitcher } from '../components/common/LanguageSwitcher';

export default function Login() {
  const { t } = useTranslation();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [login, { isLoading }] = useLoginMutation();
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await login({ username, password }).unwrap();
      dispatch(setCredentials(res));
      navigate('/');
    } catch (err) {
      alert(t('login_failed'));
    }
  };

  return (
    <div className="relative min-h-screen flex items-center justify-center p-4 overflow-hidden bg-slate-50 dark:bg-slate-950 transition-colors duration-300">
      {/* Background decorative glowing blobs */}
      <div className="absolute top-0 -left-4 w-96 h-96 bg-blue-400 dark:bg-blue-900 rounded-full mix-blend-multiply filter blur-3xl opacity-20 dark:opacity-30 animate-blob" />
      <div className="absolute -bottom-8 right-4 w-96 h-96 bg-indigo-400 dark:bg-indigo-900 rounded-full mix-blend-multiply filter blur-3xl opacity-20 dark:opacity-30 animate-blob animation-delay-2000" />
      <div className="absolute top-1/3 right-1/4 w-80 h-80 bg-purple-400 dark:bg-purple-900 rounded-full mix-blend-multiply filter blur-3xl opacity-10 dark:opacity-20 animate-blob animation-delay-4000" />

      {/* Floating control buttons (top right) */}
      <div className="absolute top-6 right-6 flex items-center gap-2 bg-white/70 dark:bg-slate-900/70 backdrop-blur-md px-3 py-1.5 rounded-full border border-slate-200/50 dark:border-slate-800/50 shadow-sm z-10">
        <LanguageSwitcher />
        <div className="w-px h-5 bg-slate-200 dark:bg-slate-800 mx-1" />
        <ThemeToggle />
      </div>

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: 'easeOut' }}
        className="w-full max-w-md bg-white/80 dark:bg-slate-900/80 backdrop-blur-xl rounded-3xl border border-slate-200/50 dark:border-slate-800/50 shadow-2xl p-8 relative z-10"
      >
        {/* Brand/Logo Section */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 text-white shadow-xl shadow-blue-500/20 dark:shadow-indigo-500/10 mb-4">
            <svg className="w-9 h-9" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 009 11.571V9a4 4 0 00-4-4H4m15.542 7.5c0 3.517-1.009 6.799-2.753 9.571M12 11c0-2.433-.917-4.647-2.423-6.31M12 11a14.07 14.07 0 003.578-9.429M12 11a14.07 14.07 0 013.578-9.429M12 11h1.071M12 2a9 9 0 100 18 9 9 0 000-18z" />
            </svg>
          </div>
          <h1 className="text-3xl font-extrabold tracking-tight bg-gradient-to-r from-slate-900 to-slate-700 dark:from-white dark:to-slate-300 bg-clip-text text-transparent">
            CivicFlow
          </h1>
          <p className="text-slate-500 dark:text-slate-400 mt-1.5 text-sm font-medium">
            e-Government Services Portal
          </p>
        </div>

        {/* Login Form */}
        <form onSubmit={handleSubmit} className="space-y-5">
          {/* Username/Email Input */}
          <div className="space-y-1">
            <label className="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 block px-1">
              Email or Username
            </label>
            <div className="relative">
              <span className="absolute inset-y-0 left-0 pl-3.5 flex items-center text-slate-400">
                <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </span>
              <input
                type="text"
                placeholder="Email or username"
                value={username}
                onChange={e => setUsername(e.target.value)}
                className="w-full pl-11 pr-4 py-3.5 bg-slate-100/50 dark:bg-slate-950/40 border border-slate-200 dark:border-slate-800 focus:border-blue-500 dark:focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 dark:focus:ring-blue-400/10 rounded-2xl outline-none text-slate-800 dark:text-white transition duration-200 font-medium placeholder-slate-400 dark:placeholder-slate-600"
                required
              />
            </div>
          </div>

          {/* Password Input */}
          <div className="space-y-1">
            <div className="flex justify-between items-center px-1">
              <label className="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400">
                {t('password')}
              </label>
              <a href="/forgot-password" className="text-xs font-semibold text-blue-600 hover:text-blue-500 dark:text-blue-400 transition-colors">
                {t('forgot_password')}
              </a>
            </div>
            <div className="relative">
              <span className="absolute inset-y-0 left-0 pl-3.5 flex items-center text-slate-400">
                <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
              </span>
              <input
                type={showPassword ? "text" : "password"}
                placeholder="••••••••"
                value={password}
                onChange={e => setPassword(e.target.value)}
                className="w-full pl-11 pr-12 py-3.5 bg-slate-100/50 dark:bg-slate-950/40 border border-slate-200 dark:border-slate-800 focus:border-blue-500 dark:focus:border-blue-400 focus:ring-2 focus:ring-blue-500/10 dark:focus:ring-blue-400/10 rounded-2xl outline-none text-slate-800 dark:text-white transition duration-200 font-medium placeholder-slate-400 dark:placeholder-slate-600"
                required
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 transition-colors"
              >
                {showPassword ? (
                  <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21" />
                  </svg>
                ) : (
                  <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                )}
              </button>
            </div>
          </div>

          {/* Action button */}
          <motion.button
            whileTap={{ scale: 0.98 }}
            type="submit"
            disabled={isLoading}
            className="w-full mt-2 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 disabled:from-blue-400 disabled:to-indigo-400 text-white font-semibold py-3.5 px-4 rounded-2xl shadow-lg shadow-blue-500/20 dark:shadow-indigo-500/10 hover:shadow-xl hover:shadow-blue-500/30 transition duration-200 flex items-center justify-center"
          >
            {isLoading ? (
              <span className="loading loading-spinner loading-sm"></span>
            ) : (
              <span className="flex items-center gap-2">
                {t('login')}
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
                </svg>
              </span>
            )}
          </motion.button>
        </form>

        {/* Secure connection footnote */}
        <div className="mt-8 pt-6 border-t border-slate-100 dark:border-slate-800/60 flex items-center justify-center gap-2 text-xs text-slate-400 dark:text-slate-500 font-medium">
          <svg className="w-4 h-4 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
          </svg>
          Secure 256-bit SSL encrypted connection
        </div>
      </motion.div>
    </div>
  );
}