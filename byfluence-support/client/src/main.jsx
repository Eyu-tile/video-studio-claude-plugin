import { StrictMode, Suspense, lazy } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import './index.css';
import { AuthProvider, useAuth } from './lib/auth.jsx';
import { ConfirmProvider, Loading, ToastProvider } from './components/ui.jsx';
import Layout from './components/Layout.jsx';
import Login, { ForcePasswordChange } from './pages/Login.jsx';
import Dashboard from './pages/Dashboard.jsx';

const KnowledgeBase = lazy(() => import('./pages/KnowledgeBase.jsx'));
const KbCategory = lazy(() => import('./pages/KbCategory.jsx'));
const DocView = lazy(() => import('./pages/DocView.jsx'));
const DocList = lazy(() => import('./pages/DocList.jsx'));
const Faqs = lazy(() => import('./pages/Faqs.jsx'));
const Templates = lazy(() => import('./pages/Templates.jsx'));
const Tickets = lazy(() => import('./pages/Tickets.jsx'));
const TicketDetail = lazy(() => import('./pages/TicketDetail.jsx'));
const Escalations = lazy(() => import('./pages/Escalations.jsx'));
const Training = lazy(() => import('./pages/Training.jsx'));
const TrainingModule = lazy(() => import('./pages/TrainingModule.jsx'));
const Announcements = lazy(() => import('./pages/Announcements.jsx'));
const Policies = lazy(() => import('./pages/Policies.jsx'));
const Manage = lazy(() => import('./pages/Manage.jsx'));
const DocEditor = lazy(() => import('./pages/DocEditor.jsx'));
const TemplateEditor = lazy(() => import('./pages/TemplateEditor.jsx'));
const VersionHistory = lazy(() => import('./pages/VersionHistory.jsx'));
const Reports = lazy(() => import('./pages/Reports.jsx'));
const SettingsPage = lazy(() => import('./pages/Settings.jsx'));
const SearchResults = lazy(() => import('./pages/SearchResults.jsx'));

function Gate() {
  const { user } = useAuth();
  if (user === undefined) return <div className="h-full grid place-items-center"><Loading label="Loading Byfluence Support…" /></div>;
  if (!user) return <Login />;
  if (user.must_change_password) return <ForcePasswordChange />;
  return (
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="kb" element={<KnowledgeBase />} />
          <Route path="kb/c/:cat" element={<KbCategory />} />
          <Route path="kb/:slug" element={<DocView />} />
          <Route path="faqs" element={<Faqs />} />
          <Route path="templates" element={<Templates />} />
          <Route path="templates/:slug" element={<Templates />} />
          <Route path="troubleshooting" element={<DocList type="troubleshooting" />} />
          <Route path="sops" element={<DocList type="sop" />} />
          <Route path="communication" element={<DocList type="guide" />} />
          <Route path="policies" element={<Policies />} />
          <Route path="tickets" element={<Tickets />} />
          <Route path="tickets/:id" element={<TicketDetail />} />
          <Route path="escalations" element={<Escalations />} />
          <Route path="training" element={<Training />} />
          <Route path="training/:slug" element={<TrainingModule />} />
          <Route path="announcements" element={<Announcements />} />
          <Route path="manage" element={<Manage />} />
          <Route path="manage/docs/new" element={<DocEditor />} />
          <Route path="manage/docs/:slug" element={<DocEditor />} />
          <Route path="manage/templates/new" element={<TemplateEditor />} />
          <Route path="manage/templates/:slug" element={<TemplateEditor />} />
          <Route path="manage/history/:kind/:slug" element={<VersionHistory />} />
          <Route path="reports" element={<Reports />} />
          <Route path="settings" element={<SettingsPage />} />
          <Route path="search" element={<SearchResults />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </Suspense>
  );
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <ToastProvider>
        <ConfirmProvider>
          <AuthProvider>
            <Gate />
          </AuthProvider>
        </ConfirmProvider>
      </ToastProvider>
    </BrowserRouter>
  </StrictMode>,
);
