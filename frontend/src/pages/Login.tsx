import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import { useLoginMutation } from '../services/authApi';
import { LanguageSwitcher } from '../components/LanguageSwitcher';
import { ThemeToggle } from '../components/ThemeToggle';

export const Login = () => {
  const { t } = useTranslation();
  const [login, { isLoading }] = useLoginMutation();

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
          <input type="email" placeholder={t('email')} className="w-full p-3 border rounded-lg dark:bg-gray-800" />
          <input type="password" placeholder={t('password')} className="w-full p-3 border rounded-lg" />
          <button type="submit" disabled={isLoading} className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition">
            {isLoading ? <Spinner /> : t('login')}
          </button>
        </form>
        <p className="text-center text-sm mt-4">
          <a href="/forgot-password" className="text-blue-600">{t('forgot_password')}</a>
        </p>
      </motion.div>
    </div>
  );
};