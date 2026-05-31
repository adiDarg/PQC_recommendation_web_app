import { createRoot } from 'react-dom/client'
import './styles/index.css'
import App from './App.jsx'
import { Analytics } from "@vercel/analytics/react"
import { SpeedInsights } from "@vercel/speed-insights/react"

createRoot(document.getElementById('root')).render(
    <>
        <App />
        <Analytics />
        <SpeedInsights />
    </>
)
