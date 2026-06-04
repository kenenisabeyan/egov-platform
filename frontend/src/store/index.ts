import { configureStore } from '@reduxjs/toolkit';
import authReducer from './authSlice';
import applicationReducer from './applicationSlice';
import { authApi } from '../services/authApi';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    applications: applicationReducer,
    [authApi.reducerPath]: authApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(authApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;