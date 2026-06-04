import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Application {
  id: string;
  serviceId: string;
  status: string;
  submittedAt: string;
  details: any;
}

interface ApplicationState {
  items: Application[];
  loading: boolean;
  error: string | null;
}

const initialState: ApplicationState = {
  items: [],
  loading: false,
  error: null,
};

const applicationSlice = createSlice({
  name: 'applications',
  initialState,
  reducers: {
    setApplications: (state, action: PayloadAction<Application[]>) => {
      state.items = action.payload;
    },
    addApplication: (state, action: PayloadAction<Application>) => {
      state.items.push(action.payload);
    },
  },
});

export const { setApplications, addApplication } = applicationSlice.actions;
export default applicationSlice.reducer;
