"use client"

import { useState } from "react"
import { NavigationProvider, useNavigation } from "@/components/navigation-context"
import { AuthPages } from "@/components/auth/auth-pages"
import { AppSidebar } from "@/components/app-sidebar"
import { AppHeader } from "@/components/app-header"
import { DashboardPage } from "@/components/dashboard/dashboard-page"
import { CampaignsPage } from "@/components/campaigns/campaigns-page"
import { CampaignResults } from "@/components/campaigns/campaign-results"
import { LeadsTable } from "@/components/leads/leads-table"
import { LeadDetail } from "@/components/leads/lead-detail"
import { PitchGenerator } from "@/components/pitches/pitch-generator"
import { AnalyticsPage } from "@/components/analytics/analytics-page"
import { SettingsPage } from "@/components/settings/settings-page"

function AppContent() {
  const { currentPage } = useNavigation()

  const pageMap: Record<string, React.ReactNode> = {
    dashboard: <DashboardPage />,
    campaigns: <CampaignsPage />,
    "campaign-results": <CampaignResults />,
    leads: <LeadsTable />,
    "lead-detail": <LeadDetail />,
    pitches: <PitchGenerator />,
    analytics: <AnalyticsPage />,
    settings: <SettingsPage />,
  }

  return (
    <div className="flex min-h-screen">
      <AppSidebar />
      <div className="flex flex-1 flex-col lg:ml-[260px]">
        <AppHeader />
        <main className="flex-1 p-4 lg:p-6">
          {pageMap[currentPage] || <DashboardPage />}
        </main>
      </div>
    </div>
  )
}

export default function Page() {
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  if (!isAuthenticated) {
    return <AuthPages onLogin={() => setIsAuthenticated(true)} />
  }

  return (
    <NavigationProvider>
      <AppContent />
    </NavigationProvider>
  )
}
