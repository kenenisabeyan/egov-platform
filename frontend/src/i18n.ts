import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import translationEN from './i18n/locales/en.json';

const resources = {
  en: {
    translation: translationEN
  },
  am: {
    translation: {
      "login": "ግባ",
      "logout": "ውጣ",
      "username": "የተጠቃሚ ስም",
      "password": "የይለፍ ቃል",
      "forgot_password": "የይለፍ ቃል ረሱ?",
      "login_failed": "የተሳሳተ መለያ",
      "dashboard": "ዳሽቦርድ",
      "services": "አገልግሎቶች",
      "applications": "ማመልከቻዎች",
      "profile": "ፕሮፋይል"
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
