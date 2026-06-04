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
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800 flex items-center justify-center p-4">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-md bg-white dark:bg-gray-900 rounded-2xl shadow-xl p-8"
      >
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold text-gray-800 dark:text-white">e-Gov Platform</h1>
          <div className="flex gap-2">
            <LanguageSwitcher />
            <ThemeToggle />
          </div>
        </div>
        <form onSubmit={handleSubmit} className="space-y-5">
          <input 
            type="text" 
            placeholder={t('username')} 
            value={username} 
            onChange={e => setUsername(e.target.value)}
            className="w-full p-3 border rounded-lg dark:bg-gray-800 dark:text-white"
            required
          />
          <input 
            type="password" 
            placeholder={t('password')} 
            value={password} 
            onChange={e => setPassword(e.target.value)}
            className="w-full p-3 border rounded-lg dark:bg-gray-800 dark:text-white"
            required
          />
          <button 
            type="submit" 
            disabled={isLoading}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition"
          >
            {isLoading ? <span className="loading loading-spinner loading-sm"></span> : t('login')}
          </button>
        </form>
        <p className="text-center text-sm mt-4">
          <a href="/forgot-password" className="text-blue-600">{t('forgot_password')}</a>
        </p>
      </motion.div>
    </div>
  );
}